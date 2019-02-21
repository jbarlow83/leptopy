# Copyright (c) 2013-2019, James R. Barlow
# All rights reserved.

# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:

# 1. Redistributions of source code must retain the above copyright notice, this
#    list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.

# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
# ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import argparse
import logging
import os
import re
import sys
import warnings
from collections.abc import Sequence
from contextlib import suppress
from ctypes.util import find_library
from functools import lru_cache, partial, partialmethod
from io import BytesIO
from os import fspath
from tempfile import TemporaryFile

from PIL import Image

from ._leptonica import ffi

try:
    from ._leptonica import lib as lept
except ImportError:
    lept = ffi.dlopen(find_library('lept'))


# pylint: disable=protected-access

log = logging.getLogger("leptonica")

lept.setMsgSeverity(lept.L_SEVERITY_WARNING)


def stderr(*objs):
    """Shorthand print to stderr."""
    print("leptonica.py:", *objs, file=sys.stderr)


class _LeptonicaErrorTrap:
    """
    Context manager to trap errors reported by Leptonica.

    Leptonica's error return codes don't provide much informatino about what
    went wrong. Leptonica does, however, write more detailed errors to stderr
    (provided this is not disabled at compile time). The Leptonica source
    code is very consistent in its use of macros to generate errors.

    This context manager redirects stderr to a temporary file which is then
    read and parsed for error messages.  As a side benefit, debug messages
    from Leptonica are also suppressed.

    """

    def __init__(self):
        self.tmpfile = None
        self.copy_of_stderr = -1

    def __enter__(self):
        from io import UnsupportedOperation

        self.tmpfile = TemporaryFile()

        # Save the old stderr, and redirect stderr to temporary file
        sys.stderr.flush()
        try:
            self.copy_of_stderr = os.dup(sys.stderr.fileno())
            os.dup2(self.tmpfile.fileno(), sys.stderr.fileno(), inheritable=False)
        except UnsupportedOperation:
            self.copy_of_stderr = None
        return

    def __exit__(self, exc_type, exc_value, traceback):
        # Restore old stderr
        sys.stderr.flush()
        if self.copy_of_stderr is not None:
            os.dup2(self.copy_of_stderr, sys.stderr.fileno())
            os.close(self.copy_of_stderr)

        # Get data from tmpfile (in with block to ensure it is closed)
        with self.tmpfile as tmpfile:
            tmpfile.seek(0)  # Cursor will be at end, so move back to beginning
            leptonica_output = tmpfile.read().decode(errors='replace')

        assert self.tmpfile.closed
        assert not sys.stderr.closed

        # If there are Python errors, let them bubble up
        if exc_type is LeptonicaNullResultError:
            raise LeptonicaError(leptonica_output) from exc_value
        elif exc_type:
            log.warning(leptonica_output)
            return False

        # If there are Leptonica errors, wrap them in Python excpetions
        if 'Error' in leptonica_output:
            if 'image file not found' in leptonica_output:
                raise FileNotFoundError()
            if 'pixWrite: stream not opened' in leptonica_output:
                raise LeptonicaIOError()
            if 'index not valid' in leptonica_output:
                raise IndexError()
            raise LeptonicaError(leptonica_output)

        return False


class LeptonicaError(Exception):
    pass


class LeptonicaNullResultError(Exception):
    pass


class LeptonicaIOError(LeptonicaError):
    pass


re_bindable = re.compile(
    r"""^(
    bbuffer|
    bmf|
    box|
    boxa|
    boxaa|
    ccb|
    ccba|
    dewarp|
    dewarpa|
    dpix|
    fpix|
    gplot|
    kernel|
    l_amap|
    l_aset|
    l_dna|
    l_dnaa|
    l_rbtree|
    list|
    numa|
    numaa|
    pix|
    pixa|
    pixaa|
    pixacc|
    pixacomp|
    pixc|
    pixcmap|
    pta|
    ptra|
    ptraa|
    recog|
    reg|
    sarray|
    sela|
    strcode|
    sudoku
    )
    ([A-Z]\w+)$""",
    flags=re.VERBOSE,
)

re_decamel = re.compile(
    r"""
    (WebP|
    RGBA32|
    RGBA|
    RGB|
    VShear|
    HShear|
    TRC|
    CMYK|
    UL|
    WH|
    LS|
    SVG|
    HSV|
    XYZ|
    LAB|
    FHMT|
    HMT|
    FPix|
    LR|
    TB|
    XY[12N]|
    [A-Z][a-z0-9]+)""",
    flags=re.VERBOSE,
)

from collections import defaultdict

FUNCTIONS = defaultdict(lambda: {})


def decamel(method):
    return '_'.join(s.lower() for s in re_decamel.split(method) if s)


for name in dir(lept):
    m = re_bindable.match(name)
    if m:
        prefix, method = m.group(1), m.group(2)
        FUNCTIONS[prefix][decamel(method)] = getattr(lept, name)


TYPEMAP = {}


def lept_call(fn, *args, prepend=None):
    if prepend:
        args = [*prepend, *args]
    c_args = [(arg._cdata if hasattr(arg, '_cdata') else arg) for arg in args]
    log.debug(c_args)
    typeof_fn = ffi.typeof(fn)
    with _LeptonicaErrorTrap():
        result = fn(*c_args)
    log.debug(typeof_fn.result.cname)
    wrapper_class = TYPEMAP.get(typeof_fn.result, lambda passthru: passthru)
    return wrapper_class(result)


def lept_method(self, fn, *args, prepend=None):
    return lept_call(fn, self, *args, prepend=prepend)


def make_binding(leptfn):
    typeof_fn = ffi.typeof(leptfn)
    expected_args = typeof_fn.args

    typeof_pix = ffi.typeof('PIX*')
    try:
        if expected_args[0] == typeof_pix and expected_args[1] == typeof_pix:
            # For functions with the signature
            #   pixFunction(pixd, pixs, ...)
            # set pixd=NULL
            # TODO not true in general
            return partialmethod(lept_method, leptfn, prepend=[ffi.NULL])
    except IndexError:
        pass

    self_class = TYPEMAP.get(expected_args[0])
    if self_class:
        return partialmethod(lept_method, leptfn)

    return partialmethod(staticmethod(lept_method), leptfn)


def bind(ctypedef, prefix, destroyer=''):
    def cls_wrapper(cls, ctypedef=ctypedef, prefix=prefix, destroyer=destroyer):
        typeof = ffi.typeof(f'{ctypedef} *')
        TYPEMAP[typeof] = cls
        cls._ctypedef = ctypedef
        cls._prefix = prefix
        if not destroyer:
            destroyer = getattr(lept, f'{cls._prefix}Destroy')
        cls._destroyer = destroyer
        cls._typeof = typeof
        if prefix in FUNCTIONS:
            for methodname, fn in FUNCTIONS[prefix].items():
                if hasattr(cls, methodname):
                    continue
                setattr(cls, methodname, make_binding(fn))

        return cls

    return cls_wrapper


class LeptonicaObject:
    """General wrapper for Leptonica objects

    When Leptonica returns an object, we bundled it in a wrapper class, which
    manages its memory. The wrapper class assumes that it will be calling some
    sort of lept.thingDestroy() function when the instance is deleted. Most
    Leptonica objects are reference counted, and destroy decrements the
    refcount.

    Most of the time, when Leptonica returns something, we wrap and it the job
    is done. When wrapping objects that came from a Leptonica container, like
    a PIXA returning PIX, the subclass must clone the object before passing it
    here, to maintain the reference count.

    CFFI ensures that the destroy function is called at garbage collection time
    so we do not need to mess with __del__.
    """

    _ctypedef, _prefix, _typeof = None, None, None
    _destroyer = lambda x: None

    def __init__(self, cdata):
        if not cdata:
            raise LeptonicaNullResultError(f'Tried to wrap a NULL {self._ctypedef}')
        self._cdata = ffi.gc(cdata, self._destroy)

    @classmethod
    def _destroy(cls, cdata):
        """Destroy some cdata"""
        # Leptonica API uses double-pointers for its destroy APIs to prevent
        # dangling pointers. This means we need to append a '*' to whatever
        # ctype this class is associated with, to create a double-pointer.
        pp = ffi.new(f'{cls._ctypedef}**', cdata)
        cls._destroyer(pp)


@bind('PIX', 'pix')
class Pix(LeptonicaObject):
    """
    Wrapper around leptonica's PIX object.

    Leptonica uses referencing counting on PIX objects. Also, many Leptonica
    functions return the original object with an increased reference count
    if the operation had no effect (for example, image skew was found to be 0).
    This has complications for memory management in Python. Whenever Leptonica
    returns a PIX object (new or old), we wrap it in this class, which
    registers it with the FFI garbage collector. pixDestroy() decrements the
    reference count and only destroys when the last reference is removed.

    Leptonica's reference counting is not threadsafe. This class can be used
    in a threadsafe manner if a Python threading.Lock protects the data.

    This class treats Pix objects as immutable.  All methods return new
    modified objects.  This allows convenient chaining:

    >>>   Pix.open('filename.jpg').scale((0.5, 0.5)).deskew().show()

    The API follows the style of Pillow (Python Imaging Library) in many respects.
    """

    def __repr__(self):
        if self._cdata:
            s = "<leptonica.Pix image size={0}x{1} depth={2}{4} at 0x{3:x}>"
            return s.format(
                self._cdata.w,
                self._cdata.h,
                self._cdata.d,
                int(ffi.cast('intptr_t', self._cdata)),
                '(colormapped)' if self._cdata.colormap else '',
            )
        else:
            return "<leptonica.Pix image NULL>"

    def _repr_png_(self):
        """IPython display hook

        returns png version of image
        """

        data = ffi.new('l_uint8 **')
        size = ffi.new('size_t *')

        err = lept.pixWriteMemPng(data, size, self._cdata, 0)
        if err != 0:
            raise LeptonicaIOError("pixWriteMemPng")

        char_data = ffi.cast('char *', data[0])
        return ffi.buffer(char_data, size[0])[:]

    def __getstate__(self):
        data = ffi.new('l_uint32 **')
        size = ffi.new('size_t *')

        err = lept.pixSerializeToMemory(self._cdata, data, size)
        if err != 0:
            raise LeptonicaIOError("pixSerializeToMemory")

        char_data = ffi.cast('char *', data[0])

        # Copy from C bytes to python bytes()
        data_bytes = ffi.buffer(char_data, size[0])[:]

        # Can now free C bytes
        lept.lept_free(char_data)
        return dict(data=data_bytes)

    def __setstate__(self, state):
        cdata_bytes = ffi.new('char[]', state['data'])
        cdata_uint32 = ffi.cast('l_uint32 *', cdata_bytes)

        pix = lept.pixDeserializeFromMemory(cdata_uint32, len(state['data']))
        Pix.__init__(self, pix)

    def __eq__(self, other):
        if not isinstance(other, Pix):
            return NotImplemented
        same = ffi.new('l_int32 *', 0)
        with _LeptonicaErrorTrap():
            err = lept.pixEqual(self._cdata, other._cdata, same)
            if err:
                raise TypeError()
        return bool(same[0])

    @property
    def width(self):
        return self._cdata.w

    @property
    def height(self):
        return self._cdata.h

    @property
    def depth(self):
        return self._cdata.d

    @property
    def size(self):
        return (self._cdata.w, self._cdata.h)

    @property
    def info(self):
        return {'dpi': (self._cdata.xres, self._cdata.yres)}

    @property
    def mode(self):
        "Return mode like PIL.Image"
        if self.depth == 1:
            return '1'
        elif self.depth >= 16:
            return 'RGB'
        elif not self._cdata.colormap:
            return 'L'
        else:
            return 'P'

    @classmethod
    def read(cls, path):
        warnings.warn('Use Pix.open() instead', DeprecationWarning)
        return cls.open(path)

    @classmethod
    def open(cls, path):
        """Load an image file into a PIX object.

        Leptonica can load TIFF, PNM (PBM, PGM, PPM), PNG, and JPEG.  If
        loading fails then the object will wrap a C null pointer.
        """
        filename = fspath(path)
        with _LeptonicaErrorTrap():
            return cls(lept.pixRead(os.fsencode(filename)))

    def write_implied_format(self, path, jpeg_quality=0, jpeg_progressive=0):
        """Write pix to the filename, with the extension indicating format.

        jpeg_quality -- quality (iff JPEG; 1 - 100, 0 for default)
        jpeg_progressive -- (iff JPEG; 0 for baseline seq., 1 for progressive)
        """
        filename = fspath(path)
        with _LeptonicaErrorTrap():
            lept.pixWriteImpliedFormat(
                os.fsencode(filename), self._cdata, jpeg_quality, jpeg_progressive
            )

    @classmethod
    def frompil(self, pillow_image):
        """Create a copy of a PIL.Image from this Pix"""
        bio = BytesIO()
        pillow_image.save(bio, format='png', compress_level=1)
        py_buffer = bio.getbuffer()
        c_buffer = ffi.from_buffer(py_buffer)
        with _LeptonicaErrorTrap():
            pix = Pix(lept.pixReadMem(c_buffer, len(c_buffer)))
            return pix

    def topil(self):
        """Returns a PIL.Image version of this Pix"""
        from PIL import Image

        # Leptonica manages data in words, so it implicitly does an endian
        # swap.  Tell Pillow about this when it reads the data.
        pix = self
        if sys.byteorder == 'little':
            if self.mode == 'RGB':
                raw_mode = 'XBGR'
            elif self.mode == 'RGBA':
                raw_mode = 'ABGR'
            elif self.mode == '1':
                raw_mode = '1;I'
                pix = Pix(lept.pixEndianByteSwapNew(pix._cdata))
            else:
                raw_mode = self.mode
                pix = Pix(lept.pixEndianByteSwapNew(pix._cdata))
        else:
            raw_mode = self.mode  # no endian swap needed

        size = (pix._cdata.w, pix._cdata.h)
        bytecount = pix._cdata.wpl * 4 * pix._cdata.h
        buf = ffi.buffer(pix._cdata.data, bytecount)
        stride = pix._cdata.wpl * 4

        im = Image.frombytes(self.mode, size, buf, 'raw', raw_mode, stride)

        return im

    def show(self):
        return self.topil().show()

    def deskew(self, reduction_factor=0):
        """Returns the deskewed pix object.

        A clone of the original is returned when the algorithm cannot find a
        skew angle with sufficient confidence.

        reduction_factor -- amount to downsample (0 for default) when searching
            for skew angle
        """
        with _LeptonicaErrorTrap():
            return Pix(lept.pixDeskew(self._cdata, reduction_factor))

    def scale(self, scale_xy):
        """Returns the pix object rescaled according to the proportions given."""
        with _LeptonicaErrorTrap():
            return Pix(lept.pixScale(self._cdata, scale_xy[0], scale_xy[1]))

    def rotate180(self):
        with _LeptonicaErrorTrap():
            return Pix(lept.pixRotate180(ffi.NULL, self._cdata))

    def rotate_orth(self, quads):
        """Orthographic rotation, quads: 0-3, number of clockwise rotations"""
        with _LeptonicaErrorTrap():
            return Pix(lept.pixRotateOrth(self._cdata, quads))

    def find_skew(self):
        """Returns a tuple (deskew angle in degrees, confidence value).

        Returns (None, None) if no angle is available.
        """
        with _LeptonicaErrorTrap():
            angle = ffi.new('float *', 0.0)
            confidence = ffi.new('float *', 0.0)
            result = lept.pixFindSkew(self._cdata, angle, confidence)
            if result == 0:
                return (angle[0], confidence[0])
            else:
                return (None, None)

    def convert_rgb_to_luminance(self):
        with _LeptonicaErrorTrap():
            gray_pix = lept.pixConvertRGBToLuminance(self._cdata)
            if gray_pix:
                return Pix(gray_pix)
            return None

    def remove_colormap(self, removal_type):
        """Remove a palette (colormap); if no colormap, returns a copy of this
        image

            removal_type - any of lept.REMOVE_CMAP_*

        """
        with _LeptonicaErrorTrap():
            return Pix(
                lept.pixRemoveColormapGeneral(self._cdata, removal_type, lept.L_COPY)
            )

    def otsu_adaptive_threshold(
        self, tile_size=(300, 300), kernel_size=(4, 4), scorefract=0.1
    ):
        with _LeptonicaErrorTrap():
            sx, sy = tile_size
            smoothx, smoothy = kernel_size
            p_pix = ffi.new('PIX **')

            pix = Pix(lept.pixConvertTo8(self._cdata, 0))
            result = lept.pixOtsuAdaptiveThreshold(
                pix._cdata, sx, sy, smoothx, smoothy, scorefract, ffi.NULL, p_pix
            )
            if result == 0:
                return Pix(p_pix[0])
            else:
                return None

    def otsu_threshold_on_background_norm(
        self,
        mask=None,
        tile_size=(10, 15),
        thresh=100,
        mincount=50,
        bgval=255,
        kernel_size=(2, 2),
        scorefract=0.1,
    ):
        with _LeptonicaErrorTrap():
            sx, sy = tile_size
            smoothx, smoothy = kernel_size
            mask = ffi.NULL
            if isinstance(mask, Pix):
                mask = mask._cdata

            pix = Pix(lept.pixConvertTo8(self._cdata, 0))
            thresh_pix = lept.pixOtsuThreshOnBackgroundNorm(
                pix._cdata,
                mask,
                sx,
                sy,
                thresh,
                mincount,
                bgval,
                smoothx,
                smoothy,
                scorefract,
                ffi.NULL,
            )
            return Pix(thresh_pix)

    def masked_threshold_on_background_norm(
        self,
        mask=None,
        tile_size=(10, 15),
        thresh=100,
        mincount=50,
        kernel_size=(2, 2),
        scorefract=0.1,
    ):
        with _LeptonicaErrorTrap():
            sx, sy = tile_size
            smoothx, smoothy = kernel_size
            mask = ffi.NULL
            if isinstance(mask, Pix):
                mask = mask._cdata

            pix = Pix(lept.pixConvertTo8(self._cdata, 0))
            thresh_pix = lept.pixMaskedThreshOnBackgroundNorm(
                pix._cdata,
                mask,
                sx,
                sy,
                thresh,
                mincount,
                smoothx,
                smoothy,
                scorefract,
                ffi.NULL,
            )
            return Pix(thresh_pix)

    def crop_to_foreground(
        self, threshold=128, mindist=70, erasedist=30, showmorph=0, debugpdf=''
    ):
        if debugpdf:
            pixac = PixCompArray(4)
        else:
            pixac = ffi.NULL
        with _LeptonicaErrorTrap():
            cropbox = lept_call(
                lept.pixFindPageForeground,
                self,
                threshold,
                mindist,
                erasedist,
                showmorph,
                pixac,
            )

            if debugpdf:
                pixac.convert_to_pdf(
                    300, 1.0, lept.L_DEFAULT_ENCODE, 0, b"debug", os.fsencode(debugpdf)
                )

            cropped_pix = lept.pixClipRectangle(self._cdata, cropbox._cdata, ffi.NULL)
            return Pix(cropped_pix)

    def clean_background_to_white(
        self, mask=None, grayscale=None, gamma=1.0, black=0, white=255
    ):
        with _LeptonicaErrorTrap():
            return Pix(
                lept.pixCleanBackgroundToWhite(
                    self._cdata,
                    mask or ffi.NULL,
                    grayscale or ffi.NULL,
                    gamma,
                    black,
                    white,
                )
            )

    def gamma_trc(self, gamma=1.0, minval=0, maxval=255):
        with _LeptonicaErrorTrap():
            return Pix(lept.pixGammaTRC(ffi.NULL, self._cdata, gamma, minval, maxval))

    def background_norm(
        self,
        mask=None,
        grayscale=None,
        tile_size=(10, 15),
        fg_threshold=60,
        min_count=40,
        bg_val=200,
        smooth_kernel=(2, 1),
    ):
        # Background norm doesn't work on color mapped Pix, so remove colormap
        target_pix = self.remove_colormap(lept.REMOVE_CMAP_BASED_ON_SRC)
        with _LeptonicaErrorTrap():
            return Pix(
                lept.pixBackgroundNorm(
                    target_pix._cdata,
                    mask or ffi.NULL,
                    grayscale or ffi.NULL,
                    tile_size[0],
                    tile_size[1],
                    fg_threshold,
                    min_count,
                    bg_val,
                    smooth_kernel[0],
                    smooth_kernel[1],
                )
            )

    @staticmethod
    @lru_cache(maxsize=1)
    def make_pixel_sum_tab8():
        return lept.makePixelSumTab8()

    @staticmethod
    def correlation_binary(pix1, pix2):
        if get_leptonica_version() < 'leptonica-1.72':
            # Older versions of Leptonica (pre-1.72) have a buggy
            # implementation of pixCorrelationBinary that overflows on larger
            # images.  Ubuntu 14.04/trusty has 1.70. Ubuntu PPA
            # ppa:alex-p/tesseract-ocr has leptonlib 1.75.
            raise LeptonicaError("Leptonica version is too old")

        correlation = ffi.new('float *', 0.0)
        result = lept.pixCorrelationBinary(pix1._cdata, pix2._cdata, correlation)
        if result != 0:
            raise LeptonicaError("Correlation failed")
        return correlation[0]

    def generate_pdf_ci_data(self, type_, quality):
        "Convert to PDF data, with transcoding"
        p_compdata = ffi.new('L_COMP_DATA **')
        result = lept.pixGenerateCIData(self._cdata, type_, quality, 0, p_compdata)
        if result != 0:
            raise LeptonicaError("Generate PDF data failed")
        return CompressedData(p_compdata[0])

    def invert(self):
        return Pix(lept.pixInvert(ffi.NULL, self._cdata))

    def locate_barcodes(self):
        try:
            with _LeptonicaErrorTrap():
                pix = Pix(lept.pixConvertTo8(self._cdata, 0))
                pixa_candidates = PixArray(lept.pixExtractBarcodes(pix._cdata, 0))
                if not pixa_candidates:
                    return
                sarray = StringArray(
                    lept.pixReadBarcodes(
                        pixa_candidates._cdata,
                        lept.L_BF_ANY,
                        lept.L_USE_WIDTHS,
                        ffi.NULL,
                        0,
                    )
                )
        except (LeptonicaError, ValueError, IndexError):
            return
        finally:
            with suppress(FileNotFoundError):
                os.unlink('junkpixt.png')  # leptonica may produce this
                os.unlink('junkpixt')

        for n, s in enumerate(sarray):
            decoded = s.decode()
            if decoded.strip() == '':
                continue
            box = pixa_candidates.get_box(n)
            left, top = box.x, box.y
            right, bottom = box.x + box.w, box.y + box.h
            yield (decoded, (left, top, right, bottom))

    def despeckle(self, size):
        if size == 2:
            speckle2 = """
                oooo
                oC o
                o  o
                oooo
                """
            sel1 = Sel.from_selstr(speckle2, 'speckle2')
            sel2 = Sel.create_brick(2, 2, 0, 0, lept.SEL_HIT)
        elif size == 3:
            speckle3 = """
                ooooo
                oC  o
                o   o
                o   o
                ooooo
                """
            sel1 = Sel.from_selstr(speckle3, 'speckle3')
            sel2 = Sel.create_brick(3, 3, 0, 0, lept.SEL_HIT)
        else:
            raise ValueError(size)

        pixhmt = Pix(lept.pixHMT(ffi.NULL, self._cdata, sel1._cdata))
        pixdilated = Pix(lept.pixDilate(ffi.NULL, pixhmt._cdata, sel2._cdata))

        pixsub = Pix(lept.pixSubtract(ffi.NULL, self._cdata, pixdilated._cdata))
        return pixsub


@bind('L_COMP_DATA', prefix=None, destroyer=lept.l_CIDataDestroy)
class CompressedData(LeptonicaObject):
    """Wrapper for L_COMP_DATA - abstract compressed image data"""

    @classmethod
    def open(cls, path, jpeg_quality=75):
        "Open compressed data, without transcoding"
        filename = fspath(path)

        p_compdata = ffi.new('L_COMP_DATA **')
        result = lept.l_generateCIDataForPdf(
            os.fsencode(filename), ffi.NULL, jpeg_quality, p_compdata
        )
        if result != 0:
            raise LeptonicaError("CompressedData.open")
        return CompressedData(p_compdata[0])

    def __len__(self):
        return self._cdata.nbytescomp

    def read(self):
        buf = ffi.buffer(self._cdata.datacomp, self._cdata.nbytescomp)
        return bytes(buf)

    def __getattr__(self, name):
        if hasattr(self._cdata, name):
            return getattr(self._cdata, name)
        raise AttributeError(name)

    def get_palette_pdf_string(self):
        "Returns palette pre-formatted for use in PDF"
        buflen = len('< ') + len(' rrggbb') * self._cdata.ncolors + len('>')
        buf = ffi.buffer(self._cdata.cmapdatahex, buflen)
        return bytes(buf)


@bind('PIXA', 'pixa')
class PixArray(LeptonicaObject, Sequence):
    """Wrapper around PIXA (array of PIX)"""

    def __len__(self):
        return self._cdata[0].n

    def __getitem__(self, n):
        with _LeptonicaErrorTrap():
            return Pix(lept.pixaGetPix(self._cdata, n, lept.L_CLONE))

    def get_box(self, n):
        with _LeptonicaErrorTrap():
            return Box(lept.pixaGetBox(self._cdata, n, lept.L_CLONE))


@bind('BOX', 'box')
class Box(LeptonicaObject):
    """Wrapper around Leptonica's BOX objects (a pixel rectangle)

    Uses x, y, w, h coordinates.
    """

    def __repr__(self):
        if self._cdata:
            return '<leptonica.Box x={0} y={1} w={2} h={3}>'.format(
                self.x, self.y, self.w, self.h
            )
        return '<leptonica.Box NULL>'

    @property
    def x(self):
        return self._cdata.x

    @property
    def y(self):
        return self._cdata.y

    @property
    def w(self):
        return self._cdata.w

    @property
    def h(self):
        return self._cdata.h


@bind('BOXA', 'boxa')
class BoxArray(LeptonicaObject, Sequence):
    """Wrapper around Leptonica's BOXA (Array of BOX) objects."""

    def __repr__(self):
        if not self._cdata:
            return '<BoxArray>'
        boxes = (repr(box) for box in self)
        return '<BoxArray [' + ', '.join(boxes) + ']>'

    def __len__(self):
        return self._cdata.n

    def __getitem__(self, n):
        if not isinstance(n, int):
            raise TypeError('list indices must be integers')
        if 0 <= n < len(self):
            return Box(lept.boxaGetBox(self._cdata, n, lept.L_CLONE))
        raise IndexError(n)


@bind('SARRAY', 'sarray')
class StringArray(LeptonicaObject, Sequence):
    """Leptonica SARRAY/string array"""

    def __len__(self):
        return self._cdata.n

    def __getitem__(self, n):
        if 0 <= n < len(self):
            return ffi.string(self._cdata.array[n])
        raise IndexError(n)


@bind('SEL', 'sel')
class Sel(LeptonicaObject):
    """Leptonica 'sel'/selection element for hit-miss transform"""

    @classmethod
    def from_selstr(cls, selstr, name):
        # TODO this will strip a horizontal line of don't care's
        lines = [line.strip() for line in selstr.split('\n') if line.strip()]
        h = len(lines)
        w = len(lines[0])
        lengths = set(len(line) for line in lines)
        if len(lengths) != 1:
            raise ValueError("All lines in selstr must be same length")

        repacked = ''.join(line.strip() for line in lines)
        buf_selstr = ffi.from_buffer(repacked.encode('ascii'))
        buf_name = ffi.from_buffer(name.encode('ascii'))
        sel = lept.selCreateFromString(buf_selstr, h, w, buf_name)
        return cls(sel)

    @classmethod
    def create_brick(cls, h, w, cy, cx, type_):
        sel = lept.selCreateBrick(h, w, cy, cx, type_)
        return cls(sel)

    def __repr__(self):
        selstr = ffi.gc(lept.selPrintToString(self._cdata), lept.lept_free)
        return '<Sel \n' + ffi.string(selstr).decode('ascii') + '\n>'


@bind('PIXC', 'pixcomp')
class PixComp(LeptonicaObject):
    """Compressed image in memory"""

    @property
    def width(self):
        return self._cdata.w

    @property
    def height(self):
        return self._cdata.h

    @property
    def size(self):
        return (self.width, self.height)

    @property
    def info(self):
        return {'dpi': {'xres': self._cdata.xres, 'yres': self._cdata.yres}}

    def topix(self):
        return Pix(self.create_from_pixcomp(self._cdata))


@bind('PIXAC', 'pixacomp')
class PixCompArray(LeptonicaObject, Sequence):
    def __init__(self, param):
        if isinstance(param, int):
            cdata = lept.pixacompCreate(param)
        else:
            cdata = param
        super().__init__(cdata)

    def __repr__(self):
        return f'<PixCompArray n={len(self)}>'

    def __len__(self):
        return self._cdata.n

    def __getitem__(self, n):
        if not isinstance(n, int):
            raise TypeError('list indices must be integers')
        if n < 0:
            n += len(self)
        if 0 <= n < len(self):
            box = Box(lept.pixacompGetBox(self._cdata, n, lept.L_CLONE))
            pixc = PixComp(lept.pixacompGetPix(self._cdata, n, lept.L_CLONE))
            return (box, pixc)
        raise IndexError(n)


def get_leptonica_version():
    """Get Leptonica version string."""
    cresult = lept.getLeptonicaVersion()
    try:
        return ffi.string(cresult).decode()
    finally:
        lept.lept_free(cresult)
