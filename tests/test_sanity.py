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

from os import fspath
from pickle import dumps, loads

import pytest
from PIL import Image, ImageChops

import leptonica as lept


def test_colormap_backgroundnorm(resources):
    # Issue #262 - unclear how to reproduce exactly, so just ensure leptonica
    # can handle that case
    pix = lept.Pix.open(resources / 'baiona_colormapped.png')
    pix.background_norm()


@pytest.fixture
def crom_pix(resources):
    pix = lept.Pix.open(resources / 'crom.png')
    im = Image.open(resources / 'crom.png')
    return pix, im


def test_pix_basic(crom_pix):
    pix, im = crom_pix

    assert pix.width == im.width
    assert pix.height == im.height
    assert pix.mode == im.mode


def test_pil_conversion(crom_pix):
    pix, im = crom_pix

    # Check for pixel perfect
    assert ImageChops.difference(pix.topil(), im).getbbox() is None


def test_pix_otsu(crom_pix):
    pix, _ = crom_pix
    im1bpp = pix.otsu_adaptive_threshold()
    assert im1bpp.mode == '1'


def test_crop(resources):
    pix = lept.Pix.open(resources / 'linn.png')
    foreground = pix.crop_to_foreground()
    assert foreground.width < pix.width


def test_clean_bg(resources):
    pix = lept.Pix.open(resources / 'congress.jpg')
    imbg = pix.clean_background_to_white()


def test_pickle(crom_pix):
    pix, _ = crom_pix
    pickled = dumps(pix)
    pix2 = loads(pickled)
    assert pix.mode == pix2.mode
