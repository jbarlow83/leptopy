#!/usr/bin/env python3
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

from cffi import FFI

ffibuilder = FFI()

ffibuilder.cdef(
    """

/* 146 "./environ.h" */
typedef int                     l_ok;    /*!< return type 0 if OK, 1 on error */
typedef signed char             l_int8;
typedef unsigned char           l_uint8;
typedef short                   l_int16;
typedef unsigned short          l_uint16;
typedef int                     l_int32;
typedef unsigned int            l_uint32;
typedef float                   l_float32;
typedef double                  l_float64;

typedef long long               l_int64;
typedef unsigned long long      l_uint64;

extern l_int32  LeptDebugOK;

enum {
    L_NOT_FOUND = 0,
    L_FOUND = 1
};

enum {
    UNIX_PATH_SEPCHAR = 0,
    WIN_PATH_SEPCHAR = 1
};
typedef void *L_TIMER;

struct L_WallTimer {
    l_int32  start_sec;
    l_int32  start_usec;
    l_int32  stop_sec;
    l_int32  stop_usec;
};
typedef struct L_WallTimer  L_WALLTIMER;

/* 347 "./environ.h" */
enum {
    L_SEVERITY_EXTERNAL = 0,
    L_SEVERITY_ALL      = 1,
    L_SEVERITY_DEBUG    = 2,
    L_SEVERITY_INFO     = 3,
    L_SEVERITY_WARNING  = 4,
    L_SEVERITY_ERROR    = 5,
    L_SEVERITY_NONE     = 6
};

/* 391 "./environ.h" */


#define DEFAULT_SEVERITY    3


extern l_int32  LeptMsgSeverity;

/* 464 "./environ.h" */
/* 477 "./environ.h" */

/* 48 "./array.h" */


struct Numa
{
    l_int32          nalloc;
    l_int32          n;
    l_int32          refcount;
    l_float32        startx;
    l_float32        delx;
    l_float32       *array;
};
typedef struct Numa  NUMA;

struct Numaa
{
    l_int32          nalloc;
    l_int32          n;
    struct Numa    **numa;
};
typedef struct Numaa  NUMAA;


struct L_Dna
{
    l_int32          nalloc;
    l_int32          n;
    l_int32          refcount;
    l_float64        startx;
    l_float64        delx;
    l_float64       *array;
};
typedef struct L_Dna  L_DNA;

struct L_Dnaa
{
    l_int32          nalloc;
    l_int32          n;
    struct L_Dna   **dna;
};
typedef struct L_Dnaa  L_DNAA;

struct L_DnaHash
{
    l_int32          nbuckets;
    l_int32          initsize;
    struct L_Dna   **dna;
};
typedef struct L_DnaHash L_DNAHASH;


struct Sarray
{
    l_int32          nalloc;
    l_int32          n;
    l_int32          refcount;
    char           **array;
};
typedef struct Sarray SARRAY;

struct L_Bytea
{
    size_t           nalloc;
    size_t           size;
    l_int32          refcount;
    l_uint8         *data;
};
typedef struct L_Bytea L_BYTEA;

enum {
    L_LINEAR_INTERP = 1,
    L_QUADRATIC_INTERP = 2
};

enum {
    L_CONTINUED_BORDER = 1,
    L_SLOPE_BORDER = 2,
    L_MIRRORED_BORDER = 3
};

enum {
    L_INTEGER_VALUE = 1,
    L_FLOAT_VALUE = 2
};
/* 41 "alltypes.h" 2 */
/* 1 "./bbuffer.h" 1 */
/* 25 "./bbuffer.h" */

/* 47 "./bbuffer.h" */
struct L_ByteBuffer
{
    l_int32      nalloc;
    l_int32      n;
    l_int32      nwritten;
    l_uint8     *array;
};
typedef struct L_ByteBuffer L_BBUFFER;
/* 42 "alltypes.h" 2 */
/* 1 "./heap.h" 1 */
/* 25 "./heap.h" */

/* 74 "./heap.h" */
struct L_Heap
{
    l_int32      nalloc;
    l_int32      n;
    void       **array;
    l_int32      direction;
};
typedef struct L_Heap  L_HEAP;
/* 43 "alltypes.h" 2 */
/* 1 "./list.h" 1 */
/* 25 "./list.h" */
/* 59 "./list.h" */

struct DoubleLinkedList
{
    struct DoubleLinkedList    *prev;
    struct DoubleLinkedList    *next;
    void                       *data;
};
typedef struct DoubleLinkedList    DLLIST;


/* 44 "alltypes.h" 2 */
/* 1 "./ptra.h" 1 */
/* 25 "./ptra.h" */

/* 43 "./ptra.h" */

struct L_Ptra
{
    l_int32          nalloc;
    l_int32          imax;
    l_int32          nactual;
    void           **array;
};
typedef struct L_Ptra  L_PTRA;


struct L_Ptraa
{
    l_int32          nalloc;
    struct L_Ptra  **ptra;
};
typedef struct L_Ptraa  L_PTRAA;

enum {
    L_NO_COMPACTION = 1,
    L_COMPACTION = 2
};

enum {
    L_AUTO_DOWNSHIFT = 0,
    L_MIN_DOWNSHIFT = 1,
    L_FULL_DOWNSHIFT = 2
};

enum {
    L_HANDLE_ONLY = 0,
    L_REMOVE = 1
};
/* 45 "alltypes.h" 2 */
/* 1 "./queue.h" 1 */
/* 25 "./queue.h" */

/* 61 "./queue.h" */
struct L_Queue
{
    l_int32          nalloc;
    l_int32          nhead;

    l_int32          nelem;
    void           **array;
    struct L_Stack  *stack;
    };
typedef struct L_Queue L_QUEUE;
/* 46 "alltypes.h" 2 */
/* 1 "./rbtree.h" 1 */
/* 25 "./rbtree.h" */
/* 41 "./rbtree.h" */

enum {
    L_INT_TYPE = 1,
    L_UINT_TYPE = 2,
    L_FLOAT_TYPE = 3
};

union Rb_Type {
    l_int64    itype;
    l_uint64   utype;
    l_float64  ftype;
    void      *ptype;
};
typedef union Rb_Type RB_TYPE;
struct L_Rbtree {
    struct L_Rbtree_Node  *root;
    l_int32                keytype;
};
typedef struct L_Rbtree L_RBTREE;
typedef struct L_Rbtree L_AMAP;
typedef struct L_Rbtree L_ASET;
struct L_Rbtree_Node {
    union Rb_Type          key;
    union Rb_Type          value;
    struct L_Rbtree_Node  *left;
    struct L_Rbtree_Node  *right;
    struct L_Rbtree_Node  *parent;
    l_int32                color;
};
typedef struct L_Rbtree_Node L_RBTREE_NODE;
typedef struct L_Rbtree_Node L_AMAP_NODE;
typedef struct L_Rbtree_Node L_ASET_NODE;
/* 47 "alltypes.h" 2 */
/* 1 "./stack.h" 1 */
/* 25 "./stack.h" */

/* 53 "./stack.h" */


struct L_Stack
{
    l_int32          nalloc;
    l_int32          n;
    void           **array;
    struct L_Stack  *auxstack;
};
typedef struct L_Stack  L_STACK;
/* 48 "alltypes.h" 2 */

/* 1 "./arrayaccess.h" 1 */
/* 25 "./arrayaccess.h" */

/* 103 "./arrayaccess.h" */


/* 262 "./arrayaccess.h" */
/* 51 "alltypes.h" 2 */
/* 1 "./bmf.h" 1 */
/* 25 "./bmf.h" */

enum {
    SPLIT_ON_LEADING_WHITE = 1,
    SPLIT_ON_BLANK_LINE    = 2,
    SPLIT_ON_BOTH          = 3
};
struct L_Bmf
{
    struct Pixa  *pixa;
    l_int32       size;
    char         *directory;
    l_int32       baseline1;
    l_int32       baseline2;
    l_int32       baseline3;
    l_int32       lineheight;
    l_int32       kernwidth;
    l_int32       spacewidth;
    l_int32       vertlinesep;
    l_int32      *fonttab;
    l_int32      *baselinetab;
    l_int32      *widthtab;
};
typedef struct L_Bmf L_BMF;

/* 52 "alltypes.h" 2 */
/* 1 "./ccbord.h" 1 */
/* 25 "./ccbord.h" */


enum {
      CCB_LOCAL_COORDS = 1,
      CCB_GLOBAL_COORDS = 2
};

enum {
      CCB_SAVE_ALL_PTS = 1,
      CCB_SAVE_TURNING_PTS = 2
};


/* 90 "./ccbord.h" */
struct CCBord
{
    struct Pix          *pix;
    struct Boxa         *boxa;
    struct Pta          *start;
    l_int32              refcount;
    struct Ptaa         *local;
    struct Ptaa         *global;
    struct Numaa        *step;
    struct Pta          *splocal;
    struct Pta          *spglobal;
};
typedef struct CCBord CCBORD;

struct CCBorda
{
    struct Pix          *pix;
    l_int32              w;
    l_int32              h;
    l_int32              n;
    l_int32              nalloc;
    struct CCBord      **ccb;
};
typedef struct CCBorda CCBORDA;
/* 53 "alltypes.h" 2 */
/* 1 "./dewarp.h" 1 */
/* 25 "./dewarp.h" */

/* 99 "./dewarp.h" */


    struct L_Dewarpa
{
    l_int32            nalloc;
    l_int32            maxpage;
    struct L_Dewarp  **dewarp;
    struct L_Dewarp  **dewarpcache;
    struct Numa       *namodels;

    struct Numa       *napages;

    l_int32            redfactor;
    l_int32            sampling;
    l_int32            minlines;
    l_int32            maxdist;
    l_int32            max_linecurv;

    l_int32            min_diff_linecurv;

    l_int32            max_diff_linecurv;

    l_int32            max_edgeslope;

    l_int32            max_edgecurv;

    l_int32            max_diff_edgecurv;

    l_int32            useboth;

    l_int32            check_columns;


    l_int32            modelsready;

};
typedef struct L_Dewarpa L_DEWARPA;
struct L_Dewarp
{
    struct L_Dewarpa  *dewa;
    struct Pix        *pixs;
    struct FPix       *sampvdispar;
    struct FPix       *samphdispar;
    struct FPix       *sampydispar;
    struct FPix       *fullvdispar;
    struct FPix       *fullhdispar;
    struct FPix       *fullydispar;
    struct Numa       *namidys;
    struct Numa       *nacurves;
    l_int32            w;
    l_int32            h;
    l_int32            pageno;
    l_int32            sampling;
    l_int32            redfactor;
    l_int32            minlines;
    l_int32            nlines;
    l_int32            mincurv;
    l_int32            maxcurv;
    l_int32            leftslope;
    l_int32            rightslope;
    l_int32            leftcurv;
    l_int32            rightcurv;
    l_int32            nx;
    l_int32            ny;
    l_int32            hasref;
    l_int32            refpage;
    l_int32            vsuccess;
    l_int32            hsuccess;
    l_int32            ysuccess;
    l_int32            vvalid;
    l_int32            hvalid;
    l_int32            skip_horiz;

    l_int32            debug;
};
typedef struct L_Dewarp L_DEWARP;

/* 54 "alltypes.h" 2 */
/* 1 "./gplot.h" 1 */
/* 25 "./gplot.h" */

/* 42 "./gplot.h" */
enum GPLOT_STYLE {
    GPLOT_LINES       = 0,
    GPLOT_POINTS      = 1,
    GPLOT_IMPULSES    = 2,
    GPLOT_LINESPOINTS = 3,
    GPLOT_DOTS        = 4
};

enum GPLOT_OUTPUT {
    GPLOT_NONE  = 0,
    GPLOT_PNG   = 1,
    GPLOT_PS    = 2,
    GPLOT_EPS   = 3,
    GPLOT_LATEX = 4
};
enum GPLOT_SCALING {
    GPLOT_LINEAR_SCALE  = 0,
    GPLOT_LOG_SCALE_X   = 1,
    GPLOT_LOG_SCALE_Y   = 2,
    GPLOT_LOG_SCALE_X_Y = 3
};
extern const char  *gplotstylenames[];
extern const char  *gplotfileoutputs[];

struct GPlot
{
    char          *rootname;
    char          *cmdname;
    struct Sarray *cmddata;
    struct Sarray *datanames;
    struct Sarray *plotdata;
    struct Sarray *plottitles;
    struct Numa   *plotstyles;
    l_int32        nplots;
    char          *outname;
    l_int32        outformat;
    l_int32        scaling;
    char          *title;
    char          *xlabel;
    char          *ylabel;
};
typedef struct GPlot  GPLOT;
/* 55 "alltypes.h" 2 */
/* 1 "./imageio.h" 1 */
/* 25 "./imageio.h" */
/* 68 "./imageio.h" */
/* 88 "./imageio.h" */
enum {
    IFF_UNKNOWN        = 0,
    IFF_BMP            = 1,
    IFF_JFIF_JPEG      = 2,
    IFF_PNG            = 3,
    IFF_TIFF           = 4,
    IFF_TIFF_PACKBITS  = 5,
    IFF_TIFF_RLE       = 6,
    IFF_TIFF_G3        = 7,
    IFF_TIFF_G4        = 8,
    IFF_TIFF_LZW       = 9,
    IFF_TIFF_ZIP       = 10,
    IFF_PNM            = 11,
    IFF_PS             = 12,
    IFF_GIF            = 13,
    IFF_JP2            = 14,
    IFF_WEBP           = 15,
    IFF_LPDF           = 16,
    IFF_DEFAULT        = 17,
    IFF_SPIX           = 18
};
enum {
    BMP_ID             = 0x4d42,
    TIFF_BIGEND_ID     = 0x4d4d,
    TIFF_LITTLEEND_ID  = 0x4949
};
enum {
    L_JPEG_READ_LUMINANCE = 1,
    L_JPEG_FAIL_ON_BAD_DATA = 2
};
enum {
    L_DEFAULT_ENCODE  = 0,
    L_JPEG_ENCODE     = 1,
    L_G4_ENCODE       = 2,
    L_FLATE_ENCODE    = 3,
    L_JP2K_ENCODE     = 4
};

/* 163 "./imageio.h" */
struct L_Compressed_Data
{
    l_int32            type;
    l_uint8           *datacomp;
    size_t             nbytescomp;
    char              *data85;
    size_t             nbytes85;
    char              *cmapdata85;
    char              *cmapdatahex;
    l_int32            ncolors;
    l_int32            w;
    l_int32            h;
    l_int32            bps;
    l_int32            spp;
    l_int32            minisblack;
    l_int32            predictor;
    size_t             nbytes;
    l_int32            res;
};
typedef struct L_Compressed_Data  L_COMP_DATA;
enum {
    L_FIRST_IMAGE   = 1,
    L_NEXT_IMAGE    = 2,
    L_LAST_IMAGE    = 3
};
struct L_Pdf_Data
{
    char              *title;
    l_int32            n;
    l_int32            ncmap;
    struct L_Ptra     *cida;
    char              *id;
    char              *obj1;
    char              *obj2;
    char              *obj3;
    char              *obj4;
    char              *obj5;
    char              *poststream;
    char              *trailer;
    struct Pta        *xy;
    struct Pta        *wh;
    struct Box        *mediabox;
    struct Sarray     *saprex;
    struct Sarray     *sacmap;
    struct L_Dna      *objsize;
    struct L_Dna      *objloc;
    l_int32            xrefloc;
};
typedef struct L_Pdf_Data  L_PDF_DATA;
/* 56 "alltypes.h" 2 */
/* 1 "./jbclass.h" 1 */
/* 25 "./jbclass.h" */


struct JbClasser
{
    struct Sarray   *safiles;
    l_int32          method;
    l_int32          components;

    l_int32          maxwidth;
    l_int32          maxheight;
    l_int32          npages;
    l_int32          baseindex;

    struct Numa     *nacomps;
    l_int32          sizehaus;
    l_float32        rankhaus;
    l_float32        thresh;
    l_float32        weightfactor;

    struct Numa     *naarea;

    l_int32          w;
    l_int32          h;
    l_int32          nclass;
    l_int32          keep_pixaa;
    struct Pixaa    *pixaa;
    struct Pixa     *pixat;

    struct Pixa     *pixatd;

    struct L_DnaHash *dahash;
    struct Numa     *nafgt;

    struct Pta      *ptac;
    struct Pta      *ptact;
    struct Numa     *naclass;
    struct Numa     *napage;
    struct Pta      *ptaul;


    struct Pta      *ptall;
};
typedef struct JbClasser  JBCLASSER;


/* 103 "./jbclass.h" */
struct JbData
{
    struct Pix      *pix;
    l_int32          npages;
    l_int32          w;
    l_int32          h;
    l_int32          nclass;
    l_int32          latticew;
    l_int32          latticeh;
    struct Numa     *naclass;
    struct Numa     *napage;
    struct Pta      *ptaul;


};
typedef struct JbData  JBDATA;


enum {
   JB_RANKHAUS = 0,
   JB_CORRELATION = 1
};

enum {
   JB_CONN_COMPS = 0,
   JB_CHARACTERS = 1,
   JB_WORDS = 2
};


/* 57 "alltypes.h" 2 */
/* 1 "./morph.h" 1 */
/* 25 "./morph.h" */

/* 54 "./morph.h" */

struct Sel
{
    l_int32       sy;
    l_int32       sx;
    l_int32       cy;
    l_int32       cx;
    l_int32     **data;
    char         *name;
};
typedef struct Sel SEL;

struct Sela
{
    l_int32          n;
    l_int32          nalloc;
    struct Sel     **sel;
};
typedef struct Sela SELA;

struct L_Kernel
{
    l_int32       sy;
    l_int32       sx;
    l_int32       cy;
    l_int32       cx;
    l_float32   **data;
};
typedef struct L_Kernel  L_KERNEL;
enum {
    SYMMETRIC_MORPH_BC = 0,
    ASYMMETRIC_MORPH_BC = 1
};

enum {
    SEL_DONT_CARE  = 0,
    SEL_HIT        = 1,
    SEL_MISS       = 2
};

enum {
    L_RUN_OFF = 0,
    L_RUN_ON  = 1
};
enum {
    L_HORIZ            = 1,
    L_VERT             = 2,
    L_BOTH_DIRECTIONS  = 3
};

enum {
    L_MORPH_DILATE    = 1,
    L_MORPH_ERODE     = 2,
    L_MORPH_OPEN      = 3,
    L_MORPH_CLOSE     = 4,
    L_MORPH_HMT       = 5
};

enum {
    L_LINEAR_SCALE  = 1,
    L_LOG_SCALE     = 2
};

enum {
    L_TOPHAT_WHITE = 0,
    L_TOPHAT_BLACK = 1
};
enum {
    L_ARITH_ADD       = 1,
    L_ARITH_SUBTRACT  = 2,
    L_ARITH_MULTIPLY  = 3,
    L_ARITH_DIVIDE    = 4,
    L_UNION           = 5,
    L_INTERSECTION    = 6,
    L_SUBTRACTION     = 7,
    L_EXCLUSIVE_OR    = 8
};

enum {
    L_CHOOSE_MIN = 1,
    L_CHOOSE_MAX = 2,
    L_CHOOSE_MAXDIFF = 3,
    L_CHOOSE_MIN_BOOST = 4,
    L_CHOOSE_MAX_BOOST = 5
};

enum {
    L_BOUNDARY_BG = 1,
    L_BOUNDARY_FG = 2
};

enum {
    L_COMPARE_XOR = 1,
    L_COMPARE_SUBTRACT = 2,
    L_COMPARE_ABS_DIFF = 3
};

enum {
    L_MAX_DIFF_FROM_AVERAGE_2 = 1,
    L_MAX_MIN_DIFF_FROM_2 = 2,
    L_MAX_DIFF = 3
};

static const l_int32  ADDED_BORDER = 32;
/* 58 "alltypes.h" 2 */
/* 1 "./pix.h" 1 */
/* 25 "./pix.h" */

/* 124 "./pix.h" */


    struct Pix
{
    l_uint32             w;
    l_uint32             h;
    l_uint32             d;
    l_uint32             spp;
    l_uint32             wpl;
    l_uint32             refcount;
    l_int32              xres;

    l_int32              yres;

    l_int32              informat;
    l_int32              special;
    char                *text;
    struct PixColormap  *colormap;
    l_uint32            *data;
};
typedef struct Pix PIX;

struct PixColormap
{
    void            *array;
    l_int32          depth;
    l_int32          nalloc;
    l_int32          n;
};
typedef struct PixColormap  PIXCMAP;


    struct RGBA_Quad
{
    l_uint8     blue;
    l_uint8     green;
    l_uint8     red;
    l_uint8     alpha;
};
typedef struct RGBA_Quad  RGBA_QUAD;
/* 197 "./pix.h" */
enum {
    COLOR_RED = 0,
    COLOR_GREEN = 1,
    COLOR_BLUE = 2,
    L_ALPHA_CHANNEL = 3
};
static const l_int32  L_RED_SHIFT =
       8 * (sizeof(l_uint32) - 1 - COLOR_RED);
static const l_int32  L_GREEN_SHIFT =
       8 * (sizeof(l_uint32) - 1 - COLOR_GREEN);
static const l_int32  L_BLUE_SHIFT =
       8 * (sizeof(l_uint32) - 1 - COLOR_BLUE);
static const l_int32  L_ALPHA_SHIFT =
       8 * (sizeof(l_uint32) - 1 - L_ALPHA_CHANNEL);

enum {
    L_DRAW_RED = 0,
    L_DRAW_GREEN = 1,
    L_DRAW_BLUE = 2,
    L_DRAW_SPECIFIED = 3,
    L_DRAW_RGB = 4,
    L_DRAW_RANDOM = 5
};

static const l_float32 L_RED_WEIGHT =   0.3f;
static const l_float32 L_GREEN_WEIGHT = 0.5f;
static const l_float32 L_BLUE_WEIGHT =  0.2f;

enum {
    REMOVE_CMAP_TO_BINARY = 0,
    REMOVE_CMAP_TO_GRAYSCALE = 1,
    REMOVE_CMAP_TO_FULL_COLOR = 2,
    REMOVE_CMAP_WITH_ALPHA = 3,
    REMOVE_CMAP_BASED_ON_SRC = 4
};
/* 325 "./pix.h" */


/* 439 "./pix.h" */



struct Pixa
{
    l_int32             n;
    l_int32             nalloc;
    l_uint32            refcount;
    struct Pix        **pix;
    struct Boxa        *boxa;
};
typedef struct Pixa PIXA;

struct Pixaa
{
    l_int32             n;
    l_int32             nalloc;
    struct Pixa       **pixa;
    struct Boxa        *boxa;
};
typedef struct Pixaa PIXAA;
struct Box
{
    l_int32            x;
    l_int32            y;
    l_int32            w;
    l_int32            h;
    l_uint32           refcount;
    };
typedef struct Box    BOX;

struct Boxa
{
    l_int32            n;
    l_int32            nalloc;
    l_uint32           refcount;
    struct Box       **box;
};
typedef struct Boxa  BOXA;

struct Boxaa
{
    l_int32            n;
    l_int32            nalloc;
    struct Boxa      **boxa;
};
typedef struct Boxaa  BOXAA;

struct Pta
{
    l_int32            n;
    l_int32            nalloc;
    l_uint32           refcount;
    l_float32         *x, *y;
};
typedef struct Pta PTA;
struct Ptaa
{
    l_int32              n;
    l_int32              nalloc;
    struct Pta         **pta;
};
typedef struct Ptaa PTAA;
struct Pixacc
{
    l_int32             w;
    l_int32             h;
    l_int32             offset;

    struct Pix         *pix;
};
typedef struct Pixacc PIXACC;
struct PixTiling
{
    struct Pix          *pix;
    l_int32              nx;
    l_int32              ny;
    l_int32              w;
    l_int32              h;
    l_int32              xoverlap;
    l_int32              yoverlap;
    l_int32              strip;
};
typedef struct PixTiling PIXTILING;

struct FPix
{
    l_int32              w;
    l_int32              h;
    l_int32              wpl;
    l_uint32             refcount;
    l_int32              xres;

    l_int32              yres;

    l_float32           *data;
};
typedef struct FPix FPIX;

struct FPixa
{
    l_int32             n;
    l_int32             nalloc;
    l_uint32            refcount;
    struct FPix       **fpix;
};
typedef struct FPixa FPIXA;

struct DPix
{
    l_int32              w;
    l_int32              h;
    l_int32              wpl;
    l_uint32             refcount;
    l_int32              xres;

    l_int32              yres;

    l_float64           *data;
};
typedef struct DPix DPIX;
struct PixComp
{
    l_int32              w;
    l_int32              h;
    l_int32              d;
    l_int32              xres;

    l_int32              yres;

    l_int32              comptype;

    char                *text;
    l_int32              cmapflag;
    l_uint8             *data;
    size_t               size;
};
typedef struct PixComp PIXC;

struct PixaComp
{
    l_int32              n;
    l_int32              nalloc;
    l_int32              offset;
    struct PixComp     **pixc;
    struct Boxa         *boxa;
};
typedef struct PixaComp PIXAC;

/* 712 "./pix.h" */
enum {
    L_NOCOPY = 0,
    L_INSERT = L_NOCOPY,
    L_COPY = 1,
    L_CLONE = 2,
    L_COPY_CLONE = 3

};
enum {
    L_SHELL_SORT = 1,
    L_BIN_SORT = 2
};

enum {
    L_SORT_INCREASING = 1,
    L_SORT_DECREASING = 2
};

enum {
    L_SORT_BY_X = 1,
    L_SORT_BY_Y = 2,
    L_SORT_BY_RIGHT = 3,
    L_SORT_BY_BOT = 4,
    L_SORT_BY_WIDTH = 5,
    L_SORT_BY_HEIGHT = 6,
    L_SORT_BY_MIN_DIMENSION = 7,
    L_SORT_BY_MAX_DIMENSION = 8,
    L_SORT_BY_PERIMETER = 9,
    L_SORT_BY_AREA = 10,
    L_SORT_BY_ASPECT_RATIO = 11
};
enum {
    L_BLEND_WITH_INVERSE = 1,
    L_BLEND_TO_WHITE = 2,
    L_BLEND_TO_BLACK = 3,
    L_BLEND_GRAY = 4,
    L_BLEND_GRAY_WITH_INVERSE = 5

};
enum {
    L_PAINT_LIGHT = 1,
    L_PAINT_DARK = 2
};
enum {
    L_SET_PIXELS = 1,
    L_CLEAR_PIXELS = 2,
    L_FLIP_PIXELS = 3
};
enum {
    L_SELECT_WIDTH = 1,
    L_SELECT_HEIGHT = 2,
    L_SELECT_XVAL = 3,
    L_SELECT_YVAL = 4,
    L_SELECT_IF_EITHER = 5,

    L_SELECT_IF_BOTH = 6

};

enum {
    L_SELECT_IF_LT = 1,
    L_SELECT_IF_GT = 2,
    L_SELECT_IF_LTE = 3,
    L_SELECT_IF_GTE = 4
};
enum {
    L_SELECT_RED = 1,
    L_SELECT_GREEN = 2,
    L_SELECT_BLUE = 3,
    L_SELECT_MIN = 4,
    L_SELECT_MAX = 5,
    L_SELECT_AVERAGE = 6,
    L_SELECT_HUE = 7,
    L_SELECT_SATURATION = 8
};
enum {
    L_LS_BYTE = 1,
    L_MS_BYTE = 2,
    L_AUTO_BYTE = 3,
    L_CLIP_TO_FF = 4,
    L_LS_TWO_BYTES = 5,
    L_MS_TWO_BYTES = 6,
    L_CLIP_TO_FFFF = 7
};
enum {
    L_ROTATE_AREA_MAP = 1,
    L_ROTATE_SHEAR = 2,
    L_ROTATE_SAMPLING = 3
};

enum {
    L_BRING_IN_WHITE = 1,
    L_BRING_IN_BLACK = 2
};

enum {
    L_SHEAR_ABOUT_CORNER = 1,
    L_SHEAR_ABOUT_CENTER = 2
};
enum {
    L_TR_SC_RO = 1,
    L_SC_RO_TR = 2,
    L_RO_TR_SC = 3,
    L_TR_RO_SC = 4,
    L_RO_SC_TR = 5,
    L_SC_TR_RO = 6
};
enum {
    L_FILL_WHITE = 1,
    L_FILL_BLACK = 2
};
enum {
    L_SET_WHITE = 1,
    L_SET_BLACK = 2
};
enum {
    L_GET_WHITE_VAL = 1,
    L_GET_BLACK_VAL = 2
};
enum {
    L_WHITE_IS_MAX = 1,
    L_BLACK_IS_MAX = 2
};
enum {
    DEFAULT_CLIP_LOWER_1 = 10,
    DEFAULT_CLIP_UPPER_1 = 10,
    DEFAULT_CLIP_LOWER_2 = 5,
    DEFAULT_CLIP_UPPER_2 = 5
};
enum {
    L_MANHATTAN_DISTANCE = 1,
    L_EUCLIDEAN_DISTANCE = 2
};
enum {
    L_NEGATIVE = 1,
    L_NON_NEGATIVE = 2,
    L_POSITIVE = 3,
    L_NON_POSITIVE = 4,
    L_ZERO = 5,
    L_ALL = 6
};
enum {
    L_MEAN_ABSVAL = 1,
    L_MEDIAN_VAL = 2,
    L_MODE_VAL = 3,
    L_MODE_COUNT = 4,
    L_ROOT_MEAN_SQUARE = 5,
    L_STANDARD_DEVIATION = 6,
    L_VARIANCE = 7
};
enum {
    L_CHOOSE_CONSECUTIVE = 1,
    L_CHOOSE_SKIP_BY = 2
};
enum {
    L_TEXT_ORIENT_UNKNOWN = 0,
    L_TEXT_ORIENT_UP = 1,
    L_TEXT_ORIENT_LEFT = 2,
    L_TEXT_ORIENT_DOWN = 3,
    L_TEXT_ORIENT_RIGHT = 4
};
enum {
    L_HORIZONTAL_EDGES = 0,
    L_VERTICAL_EDGES = 1,
    L_ALL_EDGES = 2
};
enum {
    L_HORIZONTAL_LINE = 0,
    L_POS_SLOPE_LINE = 1,
    L_VERTICAL_LINE = 2,
    L_NEG_SLOPE_LINE = 3,
    L_OBLIQUE_LINE = 4
};
enum {
    L_PORTRAIT_MODE = 0,
    L_LANDSCAPE_MODE = 1
};
enum {
    L_FROM_LEFT = 0,
    L_FROM_RIGHT = 1,
    L_FROM_TOP = 2,
    L_FROM_BOT = 3,
    L_SCAN_NEGATIVE = 4,
    L_SCAN_POSITIVE = 5,
    L_SCAN_BOTH = 6,
    L_SCAN_HORIZONTAL = 7,
    L_SCAN_VERTICAL = 8
};
enum {
    L_ADJUST_SKIP = 0,
    L_ADJUST_LEFT = 1,
    L_ADJUST_RIGHT = 2,
    L_ADJUST_LEFT_AND_RIGHT = 3,
    L_ADJUST_TOP = 4,
    L_ADJUST_BOT = 5,
    L_ADJUST_TOP_AND_BOT = 6,
    L_ADJUST_CHOOSE_MIN = 7,
    L_ADJUST_CHOOSE_MAX = 8,
    L_SET_LEFT = 9,
    L_SET_RIGHT = 10,
    L_SET_TOP = 11,
    L_SET_BOT = 12,
    L_GET_LEFT = 13,
    L_GET_RIGHT = 14,
    L_GET_TOP = 15,
    L_GET_BOT = 16
};
enum {
    L_USE_MINSIZE = 1,
    L_USE_MAXSIZE = 2,
    L_SUB_ON_LOC_DIFF = 3,
    L_SUB_ON_SIZE_DIFF = 4,
    L_USE_CAPPED_MIN = 5,
    L_USE_CAPPED_MAX = 6
};

enum {
    L_COMBINE = 1,
    L_REMOVE_SMALL = 2
};

enum {
    L_USE_ALL_BOXES = 1,
    L_USE_SAME_PARITY_BOXES = 2
};

enum {
    L_WARP_TO_LEFT = 1,
    L_WARP_TO_RIGHT = 2
};

enum {
    L_LINEAR_WARP = 1,
    L_QUADRATIC_WARP = 2
};
enum {
    L_INTERPOLATED = 1,
    L_SAMPLED = 2
};
enum {
    L_THIN_FG = 1,
    L_THIN_BG = 2
};
enum {
    L_HORIZONTAL_RUNS = 0,
    L_VERTICAL_RUNS = 1
};
enum {
    L_SOBEL_EDGE = 1,
    L_TWO_SIDED_EDGE = 2
};
enum {
    L_SUBPIXEL_ORDER_RGB = 1,
    L_SUBPIXEL_ORDER_BGR = 2,
    L_SUBPIXEL_ORDER_VRGB = 3,
    L_SUBPIXEL_ORDER_VBGR = 4
};
enum {
    L_HS_HISTO = 1,
    L_HV_HISTO = 2,
    L_SV_HISTO = 3
};
enum {
    L_INCLUDE_REGION = 1,
    L_EXCLUDE_REGION = 2
};
enum {
    L_ADD_ABOVE = 1,
    L_ADD_BELOW = 2,
    L_ADD_LEFT = 3,
    L_ADD_RIGHT = 4,
    L_ADD_AT_TOP = 5,
    L_ADD_AT_BOT = 6,
    L_ADD_AT_LEFT = 7,
    L_ADD_AT_RIGHT = 8
};
enum {
    L_PLOT_AT_TOP = 1,
    L_PLOT_AT_MID_HORIZ = 2,
    L_PLOT_AT_BOT = 3,
    L_PLOT_AT_LEFT = 4,
    L_PLOT_AT_MID_VERT = 5,
    L_PLOT_AT_RIGHT = 6
};
enum {
    L_DISPLAY_WITH_XZGV = 1,
    L_DISPLAY_WITH_XLI = 2,
    L_DISPLAY_WITH_XV = 3,
    L_DISPLAY_WITH_IV = 4,
    L_DISPLAY_WITH_OPEN = 5
};
enum {
    L_NO_CHROMA_SAMPLING_JPEG = 1
};
enum {
    L_CLIP_TO_ZERO = 1,
    L_TAKE_ABSVAL = 2
};
enum {
    L_LESS_THAN_ZERO = 1,
    L_EQUAL_TO_ZERO = 2,
    L_GREATER_THAN_ZERO = 3
};
enum {
    L_ADD_TRAIL_SLASH = 1,
    L_REMOVE_TRAIL_SLASH = 2
};

typedef void *(*alloc_fn)(size_t);

typedef void (*dealloc_fn)(void *);
/* 59 "alltypes.h" 2 */
/* 1 "./recog.h" 1 */
/* 25 "./recog.h" */

/* 112 "./recog.h" */

struct L_Recog {
    l_int32        scalew;

    l_int32        scaleh;

    l_int32        linew;

    l_int32        templ_use;


    l_int32        maxarraysize;
    l_int32        setsize;
    l_int32        threshold;
    l_int32        maxyshift;

    l_int32        charset_type;
    l_int32        charset_size;
    l_int32        min_nopad;
    l_int32        num_samples;
    l_int32        minwidth_u;
    l_int32        maxwidth_u;
    l_int32        minheight_u;
    l_int32        maxheight_u;
    l_int32        minwidth;
    l_int32        maxwidth;
    l_int32        ave_done;
    l_int32        train_done;

    l_float32      max_wh_ratio;
    l_float32      max_ht_ratio;
    l_int32        min_splitw;
    l_int32        max_splith;
    struct Sarray *sa_text;
    struct L_Dna  *dna_tochar;
    l_int32       *centtab;
    l_int32       *sumtab;
    struct Pixaa  *pixaa_u;
    struct Ptaa   *ptaa_u;
    struct Numaa  *naasum_u;
    struct Pixaa  *pixaa;
    struct Ptaa   *ptaa;
    struct Numaa  *naasum;
    struct Pixa   *pixa_u;
    struct Pta    *pta_u;
    struct Numa   *nasum_u;
    struct Pixa   *pixa;
    struct Pta    *pta;
    struct Numa   *nasum;
    struct Pixa   *pixa_tr;
    struct Pixa   *pixadb_ave;
    struct Pixa   *pixa_id;
    struct Pix    *pixdb_ave;
    struct Pix    *pixdb_range;
    struct Pixa   *pixadb_boot;
    struct Pixa   *pixadb_split;
    struct L_Bmf  *bmf;
    l_int32        bmf_size;
    struct L_Rdid *did;
    struct L_Rch  *rch;
    struct L_Rcha *rcha;
};
typedef struct L_Recog L_RECOG;

struct L_Rch {
    l_int32        index;
    l_float32      score;
    char          *text;
    l_int32        sample;

    l_int32        xloc;
    l_int32        yloc;
    l_int32        width;
};
typedef struct L_Rch L_RCH;

struct L_Rcha {
    struct Numa   *naindex;
    struct Numa   *nascore;
    struct Sarray *satext;
    struct Numa   *nasample;
    struct Numa   *naxloc;
    struct Numa   *nayloc;
    struct Numa   *nawidth;
};
typedef struct L_Rcha L_RCHA;

struct L_Rdid {
    struct Pix    *pixs;
    l_int32      **counta;
    l_int32      **delya;
    l_int32        narray;
    l_int32        size;
    l_int32       *setwidth;
    struct Numa   *nasum;
    struct Numa   *namoment;
    l_int32        fullarrays;
    l_float32     *beta;
    l_float32     *gamma;
    l_float32     *trellisscore;
    l_int32       *trellistempl;
    struct Numa   *natempl;
    struct Numa   *naxloc;
    struct Numa   *nadely;
    struct Numa   *nawidth;
    struct Boxa   *boxa;
    struct Numa   *nascore;
    struct Numa   *natempl_r;
    struct Numa   *nasample_r;
    struct Numa   *naxloc_r;
    struct Numa   *nadely_r;
    struct Numa   *nawidth_r;
    struct Numa   *nascore_r;
};
typedef struct L_Rdid L_RDID;

enum {
    L_UNKNOWN = 0,
    L_ARABIC_NUMERALS = 1,
    L_LC_ROMAN_NUMERALS = 2,
    L_UC_ROMAN_NUMERALS = 3,
    L_LC_ALPHA = 4,
    L_UC_ALPHA = 5
};
enum {
    L_USE_ALL_TEMPLATES = 0,
    L_USE_AVERAGE_TEMPLATES = 1
};

/* 60 "alltypes.h" 2 */
/* 1 "./regutils.h" 1 */
/* 25 "./regutils.h" */

/* 110 "./regutils.h" */
struct L_RegParams
{
    FILE    *fp;
    char    *testname;
    char    *tempfile;
    l_int32  mode;
    l_int32  index;
    l_int32  success;
    l_int32  display;
    L_TIMER  tstart;
};
typedef struct L_RegParams  L_REGPARAMS;


enum {
    L_REG_GENERATE = 0,
    L_REG_COMPARE = 1,
    L_REG_DISPLAY = 2
};
/* 61 "alltypes.h" 2 */
/* 1 "./stringcode.h" 1 */
/* 25 "./stringcode.h" */
struct L_StrCode
{
    l_int32       fileno;
    l_int32       ifunc;
    SARRAY       *function;
    SARRAY       *data;
    SARRAY       *descr;
    l_int32       n;
};
typedef struct L_StrCode  L_STRCODE;
enum {
    L_STR_TYPE = 0,
    L_STR_NAME = 1,
    L_STR_READER = 2,
    L_STR_MEMREADER = 3
};

/* 62 "alltypes.h" 2 */
/* 1 "./sudoku.h" 1 */
/* 25 "./sudoku.h" */

/* 50 "./sudoku.h" */

struct L_Sudoku
{
    l_int32        num;
    l_int32       *locs;
    l_int32        current;
    l_int32       *init;

    l_int32       *state;

    l_int32        nguess;
    l_int32        finished;
    l_int32        failure;
};
typedef struct L_Sudoku  L_SUDOKU;


enum {
    L_SUDOKU_INIT = 0,
    L_SUDOKU_STATE = 1
};
/* 63 "alltypes.h" 2 */
/* 1 "./watershed.h" 1 */
/* 25 "./watershed.h" */
struct L_WShed
{
    struct Pix    *pixs;
    struct Pix    *pixm;
    l_int32        mindepth;
    struct Pix    *pixlab;
    struct Pix    *pixt;
    void         **lines8;
    void         **linem1;
    void         **linelab32;
    void         **linet1;
    struct Pixa   *pixad;
    struct Pta    *ptas;
    struct Numa   *nasi;
    struct Numa   *nash;
    struct Numa   *namh;
    struct Numa   *nalevels;
    l_int32        nseeds;
    l_int32        nother;
    l_int32       *lut;
    struct Numa  **links;
    l_int32        arraysize;
    l_int32        debug;
};
typedef struct L_WShed L_WSHED;

/* 64 "alltypes.h" 2 */

"""
)

ffibuilder.cdef(
    """
/*====================================================================*
 -  Copyright (C) 2001 Leptonica.  All rights reserved.
 -
 -  Redistribution and use in source and binary forms, with or without
 -  modification, are permitted provided that the following conditions
 -  are met:
 -  1. Redistributions of source code must retain the above copyright
 -     notice, this list of conditions and the following disclaimer.
 -  2. Redistributions in binary form must reproduce the above
 -     copyright notice, this list of conditions and the following
 -     disclaimer in the documentation and/or other materials
 -     provided with the distribution.
 -
 -  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
 -  ``AS IS'' AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
 -  LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
 -  A PARTICULAR PURPOSE ARE DISCLAIMED.  IN NO EVENT SHALL ANY
 -  CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
 -  EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
 -  PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
 -  PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY
 -  OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
 -  NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
 -  SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 *====================================================================*/


//#define LIBLEPT_MAJOR_VERSION   1
//#define LIBLEPT_MINOR_VERSION   76
//#define LIBLEPT_PATCH_VERSION   0


PIX * pixCleanBackgroundToWhite ( PIX *pixs, PIX *pixim, PIX *pixg, l_float32 gamma, l_int32 blackval, l_int32 whiteval );
PIX * pixBackgroundNormSimple ( PIX *pixs, PIX *pixim, PIX *pixg );
PIX * pixBackgroundNorm ( PIX *pixs, PIX *pixim, PIX *pixg, l_int32 sx, l_int32 sy, l_int32 thresh, l_int32 mincount, l_int32 bgval, l_int32 smoothx, l_int32 smoothy );
PIX * pixBackgroundNormMorph ( PIX *pixs, PIX *pixim, l_int32 reduction, l_int32 size, l_int32 bgval );
l_ok pixBackgroundNormGrayArray ( PIX *pixs, PIX *pixim, l_int32 sx, l_int32 sy, l_int32 thresh, l_int32 mincount, l_int32 bgval, l_int32 smoothx, l_int32 smoothy, PIX **ppixd );
l_ok pixBackgroundNormRGBArrays ( PIX *pixs, PIX *pixim, PIX *pixg, l_int32 sx, l_int32 sy, l_int32 thresh, l_int32 mincount, l_int32 bgval, l_int32 smoothx, l_int32 smoothy, PIX **ppixr, PIX **ppixg, PIX **ppixb );
l_ok pixBackgroundNormGrayArrayMorph ( PIX *pixs, PIX *pixim, l_int32 reduction, l_int32 size, l_int32 bgval, PIX **ppixd );
l_ok pixBackgroundNormRGBArraysMorph ( PIX *pixs, PIX *pixim, l_int32 reduction, l_int32 size, l_int32 bgval, PIX **ppixr, PIX **ppixg, PIX **ppixb );
l_ok pixGetBackgroundGrayMap ( PIX *pixs, PIX *pixim, l_int32 sx, l_int32 sy, l_int32 thresh, l_int32 mincount, PIX **ppixd );
l_ok pixGetBackgroundRGBMap ( PIX *pixs, PIX *pixim, PIX *pixg, l_int32 sx, l_int32 sy, l_int32 thresh, l_int32 mincount, PIX **ppixmr, PIX **ppixmg, PIX **ppixmb );
l_ok pixGetBackgroundGrayMapMorph ( PIX *pixs, PIX *pixim, l_int32 reduction, l_int32 size, PIX **ppixm );
l_ok pixGetBackgroundRGBMapMorph ( PIX *pixs, PIX *pixim, l_int32 reduction, l_int32 size, PIX **ppixmr, PIX **ppixmg, PIX **ppixmb );
l_ok pixFillMapHoles ( PIX *pix, l_int32 nx, l_int32 ny, l_int32 filltype );
PIX * pixExtendByReplication ( PIX *pixs, l_int32 addw, l_int32 addh );
l_ok pixSmoothConnectedRegions ( PIX *pixs, PIX *pixm, l_int32 factor );
PIX * pixGetInvBackgroundMap ( PIX *pixs, l_int32 bgval, l_int32 smoothx, l_int32 smoothy );
PIX * pixApplyInvBackgroundGrayMap ( PIX *pixs, PIX *pixm, l_int32 sx, l_int32 sy );
PIX * pixApplyInvBackgroundRGBMap ( PIX *pixs, PIX *pixmr, PIX *pixmg, PIX *pixmb, l_int32 sx, l_int32 sy );
PIX * pixApplyVariableGrayMap ( PIX *pixs, PIX *pixg, l_int32 target );
PIX * pixGlobalNormRGB ( PIX *pixd, PIX *pixs, l_int32 rval, l_int32 gval, l_int32 bval, l_int32 mapval );
PIX * pixGlobalNormNoSatRGB ( PIX *pixd, PIX *pixs, l_int32 rval, l_int32 gval, l_int32 bval, l_int32 factor, l_float32 rank );
l_ok pixThresholdSpreadNorm ( PIX *pixs, l_int32 filtertype, l_int32 edgethresh, l_int32 smoothx, l_int32 smoothy, l_float32 gamma, l_int32 minval, l_int32 maxval, l_int32 targetthresh, PIX **ppixth, PIX **ppixb, PIX **ppixd );
PIX * pixBackgroundNormFlex ( PIX *pixs, l_int32 sx, l_int32 sy, l_int32 smoothx, l_int32 smoothy, l_int32 delta );
PIX * pixContrastNorm ( PIX *pixd, PIX *pixs, l_int32 sx, l_int32 sy, l_int32 mindiff, l_int32 smoothx, l_int32 smoothy );
l_ok pixMinMaxTiles ( PIX *pixs, l_int32 sx, l_int32 sy, l_int32 mindiff, l_int32 smoothx, l_int32 smoothy, PIX **ppixmin, PIX **ppixmax );
l_ok pixSetLowContrast ( PIX *pixs1, PIX *pixs2, l_int32 mindiff );
PIX * pixLinearTRCTiled ( PIX *pixd, PIX *pixs, l_int32 sx, l_int32 sy, PIX *pixmin, PIX *pixmax );
PIX * pixAffineSampledPta ( PIX *pixs, PTA *ptad, PTA *ptas, l_int32 incolor );
PIX * pixAffineSampled ( PIX *pixs, l_float32 *vc, l_int32 incolor );
PIX * pixAffinePta ( PIX *pixs, PTA *ptad, PTA *ptas, l_int32 incolor );
PIX * pixAffine ( PIX *pixs, l_float32 *vc, l_int32 incolor );
PIX * pixAffinePtaColor ( PIX *pixs, PTA *ptad, PTA *ptas, l_uint32 colorval );
PIX * pixAffineColor ( PIX *pixs, l_float32 *vc, l_uint32 colorval );
PIX * pixAffinePtaGray ( PIX *pixs, PTA *ptad, PTA *ptas, l_uint8 grayval );
PIX * pixAffineGray ( PIX *pixs, l_float32 *vc, l_uint8 grayval );
PIX * pixAffinePtaWithAlpha ( PIX *pixs, PTA *ptad, PTA *ptas, PIX *pixg, l_float32 fract, l_int32 border );
l_ok getAffineXformCoeffs ( PTA *ptas, PTA *ptad, l_float32 **pvc );
l_ok affineInvertXform ( l_float32 *vc, l_float32 **pvci );
l_ok affineXformSampledPt ( l_float32 *vc, l_int32 x, l_int32 y, l_int32 *pxp, l_int32 *pyp );
l_ok affineXformPt ( l_float32 *vc, l_int32 x, l_int32 y, l_float32 *pxp, l_float32 *pyp );
l_ok linearInterpolatePixelColor ( l_uint32 *datas, l_int32 wpls, l_int32 w, l_int32 h, l_float32 x, l_float32 y, l_uint32 colorval, l_uint32 *pval );
l_ok linearInterpolatePixelGray ( l_uint32 *datas, l_int32 wpls, l_int32 w, l_int32 h, l_float32 x, l_float32 y, l_int32 grayval, l_int32 *pval );
l_int32 gaussjordan ( l_float32 **a, l_float32 *b, l_int32 n );
PIX * pixAffineSequential ( PIX *pixs, PTA *ptad, PTA *ptas, l_int32 bw, l_int32 bh );
l_float32 * createMatrix2dTranslate ( l_float32 transx, l_float32 transy );
l_float32 * createMatrix2dScale ( l_float32 scalex, l_float32 scaley );
l_float32 * createMatrix2dRotate ( l_float32 xc, l_float32 yc, l_float32 angle );
PTA * ptaTranslate ( PTA *ptas, l_float32 transx, l_float32 transy );
PTA * ptaScale ( PTA *ptas, l_float32 scalex, l_float32 scaley );
PTA * ptaRotate ( PTA *ptas, l_float32 xc, l_float32 yc, l_float32 angle );
BOXA * boxaTranslate ( BOXA *boxas, l_float32 transx, l_float32 transy );
BOXA * boxaScale ( BOXA *boxas, l_float32 scalex, l_float32 scaley );
BOXA * boxaRotate ( BOXA *boxas, l_float32 xc, l_float32 yc, l_float32 angle );
PTA * ptaAffineTransform ( PTA *ptas, l_float32 *mat );
BOXA * boxaAffineTransform ( BOXA *boxas, l_float32 *mat );
l_ok l_productMatVec ( l_float32 *mat, l_float32 *vecs, l_float32 *vecd, l_int32 size );
l_ok l_productMat2 ( l_float32 *mat1, l_float32 *mat2, l_float32 *matd, l_int32 size );
l_ok l_productMat3 ( l_float32 *mat1, l_float32 *mat2, l_float32 *mat3, l_float32 *matd, l_int32 size );
l_ok l_productMat4 ( l_float32 *mat1, l_float32 *mat2, l_float32 *mat3, l_float32 *mat4, l_float32 *matd, l_int32 size );
l_int32 l_getDataBit ( void *line, l_int32 n );
void l_setDataBit ( void *line, l_int32 n );
void l_clearDataBit ( void *line, l_int32 n );
void l_setDataBitVal ( void *line, l_int32 n, l_int32 val );
l_int32 l_getDataDibit ( void *line, l_int32 n );
void l_setDataDibit ( void *line, l_int32 n, l_int32 val );
void l_clearDataDibit ( void *line, l_int32 n );
l_int32 l_getDataQbit ( void *line, l_int32 n );
void l_setDataQbit ( void *line, l_int32 n, l_int32 val );
void l_clearDataQbit ( void *line, l_int32 n );
l_int32 l_getDataByte ( void *line, l_int32 n );
void l_setDataByte ( void *line, l_int32 n, l_int32 val );
l_int32 l_getDataTwoBytes ( void *line, l_int32 n );
void l_setDataTwoBytes ( void *line, l_int32 n, l_int32 val );
l_int32 l_getDataFourBytes ( void *line, l_int32 n );
void l_setDataFourBytes ( void *line, l_int32 n, l_int32 val );
char * barcodeDispatchDecoder ( char *barstr, l_int32 format, l_int32 debugflag );
l_int32 barcodeFormatIsSupported ( l_int32 format );
NUMA * pixFindBaselines ( PIX *pixs, PTA **ppta, PIXA *pixadb );
PIX * pixDeskewLocal ( PIX *pixs, l_int32 nslices, l_int32 redsweep, l_int32 redsearch, l_float32 sweeprange, l_float32 sweepdelta, l_float32 minbsdelta );
l_ok pixGetLocalSkewTransform ( PIX *pixs, l_int32 nslices, l_int32 redsweep, l_int32 redsearch, l_float32 sweeprange, l_float32 sweepdelta, l_float32 minbsdelta, PTA **pptas, PTA **pptad );
NUMA * pixGetLocalSkewAngles ( PIX *pixs, l_int32 nslices, l_int32 redsweep, l_int32 redsearch, l_float32 sweeprange, l_float32 sweepdelta, l_float32 minbsdelta, l_float32 *pa, l_float32 *pb, l_int32 debug );
L_BBUFFER * bbufferCreate ( const l_uint8 *indata, l_int32 nalloc );
void bbufferDestroy ( L_BBUFFER **pbb );
l_uint8 * bbufferDestroyAndSaveData ( L_BBUFFER **pbb, size_t *pnbytes );
l_ok bbufferRead ( L_BBUFFER *bb, l_uint8 *src, l_int32 nbytes );
l_ok bbufferReadStream ( L_BBUFFER *bb, FILE *fp, l_int32 nbytes );
l_ok bbufferExtendArray ( L_BBUFFER *bb, l_int32 nbytes );
l_ok bbufferWrite ( L_BBUFFER *bb, l_uint8 *dest, size_t nbytes, size_t *pnout );
l_ok bbufferWriteStream ( L_BBUFFER *bb, FILE *fp, size_t nbytes, size_t *pnout );
PIX * pixBilateral ( PIX *pixs, l_float32 spatial_stdev, l_float32 range_stdev, l_int32 ncomps, l_int32 reduction );
PIX * pixBilateralGray ( PIX *pixs, l_float32 spatial_stdev, l_float32 range_stdev, l_int32 ncomps, l_int32 reduction );
PIX * pixBilateralExact ( PIX *pixs, L_KERNEL *spatial_kel, L_KERNEL *range_kel );
PIX * pixBilateralGrayExact ( PIX *pixs, L_KERNEL *spatial_kel, L_KERNEL *range_kel );
PIX* pixBlockBilateralExact ( PIX *pixs, l_float32 spatial_stdev, l_float32 range_stdev );
L_KERNEL * makeRangeKernel ( l_float32 range_stdev );
PIX * pixBilinearSampledPta ( PIX *pixs, PTA *ptad, PTA *ptas, l_int32 incolor );
PIX * pixBilinearSampled ( PIX *pixs, l_float32 *vc, l_int32 incolor );
PIX * pixBilinearPta ( PIX *pixs, PTA *ptad, PTA *ptas, l_int32 incolor );
PIX * pixBilinear ( PIX *pixs, l_float32 *vc, l_int32 incolor );
PIX * pixBilinearPtaColor ( PIX *pixs, PTA *ptad, PTA *ptas, l_uint32 colorval );
PIX * pixBilinearColor ( PIX *pixs, l_float32 *vc, l_uint32 colorval );
PIX * pixBilinearPtaGray ( PIX *pixs, PTA *ptad, PTA *ptas, l_uint8 grayval );
PIX * pixBilinearGray ( PIX *pixs, l_float32 *vc, l_uint8 grayval );
PIX * pixBilinearPtaWithAlpha ( PIX *pixs, PTA *ptad, PTA *ptas, PIX *pixg, l_float32 fract, l_int32 border );
l_ok getBilinearXformCoeffs ( PTA *ptas, PTA *ptad, l_float32 **pvc );
l_ok bilinearXformSampledPt ( l_float32 *vc, l_int32 x, l_int32 y, l_int32 *pxp, l_int32 *pyp );
l_ok bilinearXformPt ( l_float32 *vc, l_int32 x, l_int32 y, l_float32 *pxp, l_float32 *pyp );
l_ok pixOtsuAdaptiveThreshold ( PIX *pixs, l_int32 sx, l_int32 sy, l_int32 smoothx, l_int32 smoothy, l_float32 scorefract, PIX **ppixth, PIX **ppixd );
PIX * pixOtsuThreshOnBackgroundNorm ( PIX *pixs, PIX *pixim, l_int32 sx, l_int32 sy, l_int32 thresh, l_int32 mincount, l_int32 bgval, l_int32 smoothx, l_int32 smoothy, l_float32 scorefract, l_int32 *pthresh );
PIX * pixMaskedThreshOnBackgroundNorm ( PIX *pixs, PIX *pixim, l_int32 sx, l_int32 sy, l_int32 thresh, l_int32 mincount, l_int32 smoothx, l_int32 smoothy, l_float32 scorefract, l_int32 *pthresh );
l_ok pixSauvolaBinarizeTiled ( PIX *pixs, l_int32 whsize, l_float32 factor, l_int32 nx, l_int32 ny, PIX **ppixth, PIX **ppixd );
l_ok pixSauvolaBinarize ( PIX *pixs, l_int32 whsize, l_float32 factor, l_int32 addborder, PIX **ppixm, PIX **ppixsd, PIX **ppixth, PIX **ppixd );
PIX * pixSauvolaGetThreshold ( PIX *pixm, PIX *pixms, l_float32 factor, PIX **ppixsd );
PIX * pixApplyLocalThreshold ( PIX *pixs, PIX *pixth, l_int32 redfactor );
l_ok pixThresholdByConnComp ( PIX *pixs, PIX *pixm, l_int32 start, l_int32 end, l_int32 incr, l_float32 thresh48, l_float32 threshdiff, l_int32 *pglobthresh, PIX **ppixd, l_int32 debugflag );
PIX * pixExpandBinaryReplicate ( PIX *pixs, l_int32 xfact, l_int32 yfact );
PIX * pixExpandBinaryPower2 ( PIX *pixs, l_int32 factor );
PIX * pixReduceBinary2 ( PIX *pixs, l_uint8 *intab );
PIX * pixReduceRankBinaryCascade ( PIX *pixs, l_int32 level1, l_int32 level2, l_int32 level3, l_int32 level4 );
PIX * pixReduceRankBinary2 ( PIX *pixs, l_int32 level, l_uint8 *intab );
l_uint8 * makeSubsampleTab2x ( void );
PIX * pixBlend ( PIX *pixs1, PIX *pixs2, l_int32 x, l_int32 y, l_float32 fract );
PIX * pixBlendMask ( PIX *pixd, PIX *pixs1, PIX *pixs2, l_int32 x, l_int32 y, l_float32 fract, l_int32 type );
PIX * pixBlendGray ( PIX *pixd, PIX *pixs1, PIX *pixs2, l_int32 x, l_int32 y, l_float32 fract, l_int32 type, l_int32 transparent, l_uint32 transpix );
PIX * pixBlendGrayInverse ( PIX *pixd, PIX *pixs1, PIX *pixs2, l_int32 x, l_int32 y, l_float32 fract );
PIX * pixBlendColor ( PIX *pixd, PIX *pixs1, PIX *pixs2, l_int32 x, l_int32 y, l_float32 fract, l_int32 transparent, l_uint32 transpix );
PIX * pixBlendColorByChannel ( PIX *pixd, PIX *pixs1, PIX *pixs2, l_int32 x, l_int32 y, l_float32 rfract, l_float32 gfract, l_float32 bfract, l_int32 transparent, l_uint32 transpix );
PIX * pixBlendGrayAdapt ( PIX *pixd, PIX *pixs1, PIX *pixs2, l_int32 x, l_int32 y, l_float32 fract, l_int32 shift );
PIX * pixFadeWithGray ( PIX *pixs, PIX *pixb, l_float32 factor, l_int32 type );
PIX * pixBlendHardLight ( PIX *pixd, PIX *pixs1, PIX *pixs2, l_int32 x, l_int32 y, l_float32 fract );
l_ok pixBlendCmap ( PIX *pixs, PIX *pixb, l_int32 x, l_int32 y, l_int32 sindex );
PIX * pixBlendWithGrayMask ( PIX *pixs1, PIX *pixs2, PIX *pixg, l_int32 x, l_int32 y );
PIX * pixBlendBackgroundToColor ( PIX *pixd, PIX *pixs, BOX *box, l_uint32 color, l_float32 gamma, l_int32 minval, l_int32 maxval );
PIX * pixMultiplyByColor ( PIX *pixd, PIX *pixs, BOX *box, l_uint32 color );
PIX * pixAlphaBlendUniform ( PIX *pixs, l_uint32 color );
PIX * pixAddAlphaToBlend ( PIX *pixs, l_float32 fract, l_int32 invert );
PIX * pixSetAlphaOverWhite ( PIX *pixs );
l_ok pixLinearEdgeFade ( PIX *pixs, l_int32 dir, l_int32 fadeto, l_float32 distfract, l_float32 maxfade );
L_BMF * bmfCreate ( const char *dir, l_int32 fontsize );
void bmfDestroy ( L_BMF **pbmf );
PIX * bmfGetPix ( L_BMF *bmf, char chr );
l_ok bmfGetWidth ( L_BMF *bmf, char chr, l_int32 *pw );
l_ok bmfGetBaseline ( L_BMF *bmf, char chr, l_int32 *pbaseline );
PIXA * pixaGetFont ( const char *dir, l_int32 fontsize, l_int32 *pbl0, l_int32 *pbl1, l_int32 *pbl2 );
l_ok pixaSaveFont ( const char *indir, const char *outdir, l_int32 fontsize );
PIX * pixReadStreamBmp ( FILE *fp );
PIX * pixReadMemBmp ( const l_uint8 *cdata, size_t size );
l_ok pixWriteStreamBmp ( FILE *fp, PIX *pix );
l_ok pixWriteMemBmp ( l_uint8 **pfdata, size_t *pfsize, PIX *pixs );
PIXA * l_bootnum_gen1 ( void );
PIXA * l_bootnum_gen2 ( void );
PIXA * l_bootnum_gen3 ( void );
PIXA * l_bootnum_gen4 ( l_int32 nsamp );
BOX * boxCreate ( l_int32 x, l_int32 y, l_int32 w, l_int32 h );
BOX * boxCreateValid ( l_int32 x, l_int32 y, l_int32 w, l_int32 h );
BOX * boxCopy ( BOX *box );
BOX * boxClone ( BOX *box );
void boxDestroy ( BOX **pbox );
l_ok boxGetGeometry ( BOX *box, l_int32 *px, l_int32 *py, l_int32 *pw, l_int32 *ph );
l_ok boxSetGeometry ( BOX *box, l_int32 x, l_int32 y, l_int32 w, l_int32 h );
l_ok boxGetSideLocations ( BOX *box, l_int32 *pl, l_int32 *pr, l_int32 *pt, l_int32 *pb );
l_ok boxSetSideLocations ( BOX *box, l_int32 l, l_int32 r, l_int32 t, l_int32 b );
l_int32 boxGetRefcount ( BOX *box );
l_ok boxChangeRefcount ( BOX *box, l_int32 delta );
l_ok boxIsValid ( BOX *box, l_int32 *pvalid );
BOXA * boxaCreate ( l_int32 n );
BOXA * boxaCopy ( BOXA *boxa, l_int32 copyflag );
void boxaDestroy ( BOXA **pboxa );
l_ok boxaAddBox ( BOXA *boxa, BOX *box, l_int32 copyflag );
l_ok boxaExtendArray ( BOXA *boxa );
l_ok boxaExtendArrayToSize ( BOXA *boxa, l_int32 size );
l_int32 boxaGetCount ( BOXA *boxa );
l_int32 boxaGetValidCount ( BOXA *boxa );
BOX * boxaGetBox ( BOXA *boxa, l_int32 index, l_int32 accessflag );
BOX * boxaGetValidBox ( BOXA *boxa, l_int32 index, l_int32 accessflag );
NUMA * boxaFindInvalidBoxes ( BOXA *boxa );
l_ok boxaGetBoxGeometry ( BOXA *boxa, l_int32 index, l_int32 *px, l_int32 *py, l_int32 *pw, l_int32 *ph );
l_ok boxaIsFull ( BOXA *boxa, l_int32 *pfull );
l_ok boxaReplaceBox ( BOXA *boxa, l_int32 index, BOX *box );
l_ok boxaInsertBox ( BOXA *boxa, l_int32 index, BOX *box );
l_ok boxaRemoveBox ( BOXA *boxa, l_int32 index );
l_ok boxaRemoveBoxAndSave ( BOXA *boxa, l_int32 index, BOX **pbox );
BOXA * boxaSaveValid ( BOXA *boxas, l_int32 copyflag );
l_ok boxaInitFull ( BOXA *boxa, BOX *box );
l_ok boxaClear ( BOXA *boxa );
BOXAA * boxaaCreate ( l_int32 n );
BOXAA * boxaaCopy ( BOXAA *baas, l_int32 copyflag );
void boxaaDestroy ( BOXAA **pbaa );
l_ok boxaaAddBoxa ( BOXAA *baa, BOXA *ba, l_int32 copyflag );
l_ok boxaaExtendArray ( BOXAA *baa );
l_ok boxaaExtendArrayToSize ( BOXAA *baa, l_int32 size );
l_int32 boxaaGetCount ( BOXAA *baa );
l_int32 boxaaGetBoxCount ( BOXAA *baa );
BOXA * boxaaGetBoxa ( BOXAA *baa, l_int32 index, l_int32 accessflag );
BOX * boxaaGetBox ( BOXAA *baa, l_int32 iboxa, l_int32 ibox, l_int32 accessflag );
l_ok boxaaInitFull ( BOXAA *baa, BOXA *boxa );
l_ok boxaaExtendWithInit ( BOXAA *baa, l_int32 maxindex, BOXA *boxa );
l_ok boxaaReplaceBoxa ( BOXAA *baa, l_int32 index, BOXA *boxa );
l_ok boxaaInsertBoxa ( BOXAA *baa, l_int32 index, BOXA *boxa );
l_ok boxaaRemoveBoxa ( BOXAA *baa, l_int32 index );
l_ok boxaaAddBox ( BOXAA *baa, l_int32 index, BOX *box, l_int32 accessflag );
BOXAA * boxaaReadFromFiles ( const char *dirname, const char *substr, l_int32 first, l_int32 nfiles );
BOXAA * boxaaRead ( const char *filename );
BOXAA * boxaaReadStream ( FILE *fp );
BOXAA * boxaaReadMem ( const l_uint8 *data, size_t size );
l_ok boxaaWrite ( const char *filename, BOXAA *baa );
l_ok boxaaWriteStream ( FILE *fp, BOXAA *baa );
l_ok boxaaWriteMem ( l_uint8 **pdata, size_t *psize, BOXAA *baa );
BOXA * boxaRead ( const char *filename );
BOXA * boxaReadStream ( FILE *fp );
BOXA * boxaReadMem ( const l_uint8 *data, size_t size );
l_ok boxaWriteDebug ( const char *filename, BOXA *boxa );
l_ok boxaWrite ( const char *filename, BOXA *boxa );
l_ok boxaWriteStream ( FILE *fp, BOXA *boxa );
l_ok boxaWriteMem ( l_uint8 **pdata, size_t *psize, BOXA *boxa );
l_ok boxPrintStreamInfo ( FILE *fp, BOX *box );
l_ok boxContains ( BOX *box1, BOX *box2, l_int32 *presult );
l_ok boxIntersects ( BOX *box1, BOX *box2, l_int32 *presult );
BOXA * boxaContainedInBox ( BOXA *boxas, BOX *box );
l_ok boxaContainedInBoxCount ( BOXA *boxa, BOX *box, l_int32 *pcount );
l_ok boxaContainedInBoxa ( BOXA *boxa1, BOXA *boxa2, l_int32 *pcontained );
BOXA * boxaIntersectsBox ( BOXA *boxas, BOX *box );
l_ok boxaIntersectsBoxCount ( BOXA *boxa, BOX *box, l_int32 *pcount );
BOXA * boxaClipToBox ( BOXA *boxas, BOX *box );
BOXA * boxaCombineOverlaps ( BOXA *boxas, PIXA *pixadb );
l_ok boxaCombineOverlapsInPair ( BOXA *boxas1, BOXA *boxas2, BOXA **pboxad1, BOXA **pboxad2, PIXA *pixadb );
BOX * boxOverlapRegion ( BOX *box1, BOX *box2 );
BOX * boxBoundingRegion ( BOX *box1, BOX *box2 );
l_ok boxOverlapFraction ( BOX *box1, BOX *box2, l_float32 *pfract );
l_ok boxOverlapArea ( BOX *box1, BOX *box2, l_int32 *parea );
BOXA * boxaHandleOverlaps ( BOXA *boxas, l_int32 op, l_int32 range, l_float32 min_overlap, l_float32 max_ratio, NUMA **pnamap );
l_ok boxSeparationDistance ( BOX *box1, BOX *box2, l_int32 *ph_sep, l_int32 *pv_sep );
l_ok boxCompareSize ( BOX *box1, BOX *box2, l_int32 type, l_int32 *prel );
l_ok boxContainsPt ( BOX *box, l_float32 x, l_float32 y, l_int32 *pcontains );
BOX * boxaGetNearestToPt ( BOXA *boxa, l_int32 x, l_int32 y );
BOX * boxaGetNearestToLine ( BOXA *boxa, l_int32 x, l_int32 y );
l_ok boxaFindNearestBoxes ( BOXA *boxa, l_int32 dist_select, l_int32 range, NUMAA **pnaaindex, NUMAA **pnaadist );
l_ok boxaGetNearestByDirection ( BOXA *boxa, l_int32 i, l_int32 dir, l_int32 dist_select, l_int32 range, l_int32 *pindex, l_int32 *pdist );
l_ok boxGetCenter ( BOX *box, l_float32 *pcx, l_float32 *pcy );
l_ok boxIntersectByLine ( BOX *box, l_int32 x, l_int32 y, l_float32 slope, l_int32 *px1, l_int32 *py1, l_int32 *px2, l_int32 *py2, l_int32 *pn );
BOX * boxClipToRectangle ( BOX *box, l_int32 wi, l_int32 hi );
l_ok boxClipToRectangleParams ( BOX *box, l_int32 w, l_int32 h, l_int32 *pxstart, l_int32 *pystart, l_int32 *pxend, l_int32 *pyend, l_int32 *pbw, l_int32 *pbh );
BOX * boxRelocateOneSide ( BOX *boxd, BOX *boxs, l_int32 loc, l_int32 sideflag );
BOXA * boxaAdjustSides ( BOXA *boxas, l_int32 delleft, l_int32 delright, l_int32 deltop, l_int32 delbot );
BOX * boxAdjustSides ( BOX *boxd, BOX *boxs, l_int32 delleft, l_int32 delright, l_int32 deltop, l_int32 delbot );
BOXA * boxaSetSide ( BOXA *boxad, BOXA *boxas, l_int32 side, l_int32 val, l_int32 thresh );
l_ok boxSetSide ( BOX *boxs, l_int32 side, l_int32 val, l_int32 thresh );
BOXA * boxaAdjustWidthToTarget ( BOXA *boxad, BOXA *boxas, l_int32 sides, l_int32 target, l_int32 thresh );
BOXA * boxaAdjustHeightToTarget ( BOXA *boxad, BOXA *boxas, l_int32 sides, l_int32 target, l_int32 thresh );
l_ok boxEqual ( BOX *box1, BOX *box2, l_int32 *psame );
l_ok boxaEqual ( BOXA *boxa1, BOXA *boxa2, l_int32 maxdist, NUMA **pnaindex, l_int32 *psame );
l_ok boxSimilar ( BOX *box1, BOX *box2, l_int32 leftdiff, l_int32 rightdiff, l_int32 topdiff, l_int32 botdiff, l_int32 *psimilar );
l_ok boxaSimilar ( BOXA *boxa1, BOXA *boxa2, l_int32 leftdiff, l_int32 rightdiff, l_int32 topdiff, l_int32 botdiff, l_int32 debug, l_int32 *psimilar, NUMA **pnasim );
l_ok boxaJoin ( BOXA *boxad, BOXA *boxas, l_int32 istart, l_int32 iend );
l_ok boxaaJoin ( BOXAA *baad, BOXAA *baas, l_int32 istart, l_int32 iend );
l_ok boxaSplitEvenOdd ( BOXA *boxa, l_int32 fillflag, BOXA **pboxae, BOXA **pboxao );
BOXA * boxaMergeEvenOdd ( BOXA *boxae, BOXA *boxao, l_int32 fillflag );
BOXA * boxaTransform ( BOXA *boxas, l_int32 shiftx, l_int32 shifty, l_float32 scalex, l_float32 scaley );
BOX * boxTransform ( BOX *box, l_int32 shiftx, l_int32 shifty, l_float32 scalex, l_float32 scaley );
BOXA * boxaTransformOrdered ( BOXA *boxas, l_int32 shiftx, l_int32 shifty, l_float32 scalex, l_float32 scaley, l_int32 xcen, l_int32 ycen, l_float32 angle, l_int32 order );
BOX * boxTransformOrdered ( BOX *boxs, l_int32 shiftx, l_int32 shifty, l_float32 scalex, l_float32 scaley, l_int32 xcen, l_int32 ycen, l_float32 angle, l_int32 order );
BOXA * boxaRotateOrth ( BOXA *boxas, l_int32 w, l_int32 h, l_int32 rotation );
BOX * boxRotateOrth ( BOX *box, l_int32 w, l_int32 h, l_int32 rotation );
BOXA * boxaSort ( BOXA *boxas, l_int32 sorttype, l_int32 sortorder, NUMA **pnaindex );
BOXA * boxaBinSort ( BOXA *boxas, l_int32 sorttype, l_int32 sortorder, NUMA **pnaindex );
BOXA * boxaSortByIndex ( BOXA *boxas, NUMA *naindex );
BOXAA * boxaSort2d ( BOXA *boxas, NUMAA **pnaad, l_int32 delta1, l_int32 delta2, l_int32 minh1 );
BOXAA * boxaSort2dByIndex ( BOXA *boxas, NUMAA *naa );
l_ok boxaExtractAsNuma ( BOXA *boxa, NUMA **pnal, NUMA **pnat, NUMA **pnar, NUMA **pnab, NUMA **pnaw, NUMA **pnah, l_int32 keepinvalid );
l_ok boxaExtractAsPta ( BOXA *boxa, PTA **pptal, PTA **pptat, PTA **pptar, PTA **pptab, PTA **pptaw, PTA **pptah, l_int32 keepinvalid );
l_ok boxaGetRankVals ( BOXA *boxa, l_float32 fract, l_int32 *px, l_int32 *py, l_int32 *pr, l_int32 *pb, l_int32 *pw, l_int32 *ph );
l_ok boxaGetMedianVals ( BOXA *boxa, l_int32 *px, l_int32 *py, l_int32 *pr, l_int32 *pb, l_int32 *pw, l_int32 *ph );
l_ok boxaGetAverageSize ( BOXA *boxa, l_float32 *pw, l_float32 *ph );
l_ok boxaaGetExtent ( BOXAA *baa, l_int32 *pw, l_int32 *ph, BOX **pbox, BOXA **pboxa );
BOXA * boxaaFlattenToBoxa ( BOXAA *baa, NUMA **pnaindex, l_int32 copyflag );
BOXA * boxaaFlattenAligned ( BOXAA *baa, l_int32 num, BOX *fillerbox, l_int32 copyflag );
BOXAA * boxaEncapsulateAligned ( BOXA *boxa, l_int32 num, l_int32 copyflag );
BOXAA * boxaaTranspose ( BOXAA *baas );
l_ok boxaaAlignBox ( BOXAA *baa, BOX *box, l_int32 delta, l_int32 *pindex );
PIX * pixMaskConnComp ( PIX *pixs, l_int32 connectivity, BOXA **pboxa );
PIX * pixMaskBoxa ( PIX *pixd, PIX *pixs, BOXA *boxa, l_int32 op );
PIX * pixPaintBoxa ( PIX *pixs, BOXA *boxa, l_uint32 val );
PIX * pixSetBlackOrWhiteBoxa ( PIX *pixs, BOXA *boxa, l_int32 op );
PIX * pixPaintBoxaRandom ( PIX *pixs, BOXA *boxa );
PIX * pixBlendBoxaRandom ( PIX *pixs, BOXA *boxa, l_float32 fract );
PIX * pixDrawBoxa ( PIX *pixs, BOXA *boxa, l_int32 width, l_uint32 val );
PIX * pixDrawBoxaRandom ( PIX *pixs, BOXA *boxa, l_int32 width );
PIX * boxaaDisplay ( PIX *pixs, BOXAA *baa, l_int32 linewba, l_int32 linewb, l_uint32 colorba, l_uint32 colorb, l_int32 w, l_int32 h );
PIXA * pixaDisplayBoxaa ( PIXA *pixas, BOXAA *baa, l_int32 colorflag, l_int32 width );
BOXA * pixSplitIntoBoxa ( PIX *pixs, l_int32 minsum, l_int32 skipdist, l_int32 delta, l_int32 maxbg, l_int32 maxcomps, l_int32 remainder );
BOXA * pixSplitComponentIntoBoxa ( PIX *pix, BOX *box, l_int32 minsum, l_int32 skipdist, l_int32 delta, l_int32 maxbg, l_int32 maxcomps, l_int32 remainder );
BOXA * makeMosaicStrips ( l_int32 w, l_int32 h, l_int32 direction, l_int32 size );
l_ok boxaCompareRegions ( BOXA *boxa1, BOXA *boxa2, l_int32 areathresh, l_int32 *pnsame, l_float32 *pdiffarea, l_float32 *pdiffxor, PIX **ppixdb );
BOX * pixSelectLargeULComp ( PIX *pixs, l_float32 areaslop, l_int32 yslop, l_int32 connectivity );
BOX * boxaSelectLargeULBox ( BOXA *boxas, l_float32 areaslop, l_int32 yslop );
BOXA * boxaSelectRange ( BOXA *boxas, l_int32 first, l_int32 last, l_int32 copyflag );
BOXAA * boxaaSelectRange ( BOXAA *baas, l_int32 first, l_int32 last, l_int32 copyflag );
BOXA * boxaSelectBySize ( BOXA *boxas, l_int32 width, l_int32 height, l_int32 type, l_int32 relation, l_int32 *pchanged );
NUMA * boxaMakeSizeIndicator ( BOXA *boxa, l_int32 width, l_int32 height, l_int32 type, l_int32 relation );
BOXA * boxaSelectByArea ( BOXA *boxas, l_int32 area, l_int32 relation, l_int32 *pchanged );
NUMA * boxaMakeAreaIndicator ( BOXA *boxa, l_int32 area, l_int32 relation );
BOXA * boxaSelectByWHRatio ( BOXA *boxas, l_float32 ratio, l_int32 relation, l_int32 *pchanged );
NUMA * boxaMakeWHRatioIndicator ( BOXA *boxa, l_float32 ratio, l_int32 relation );
BOXA * boxaSelectWithIndicator ( BOXA *boxas, NUMA *na, l_int32 *pchanged );
BOXA * boxaPermutePseudorandom ( BOXA *boxas );
BOXA * boxaPermuteRandom ( BOXA *boxad, BOXA *boxas );
l_ok boxaSwapBoxes ( BOXA *boxa, l_int32 i, l_int32 j );
PTA * boxaConvertToPta ( BOXA *boxa, l_int32 ncorners );
BOXA * ptaConvertToBoxa ( PTA *pta, l_int32 ncorners );
PTA * boxConvertToPta ( BOX *box, l_int32 ncorners );
BOX * ptaConvertToBox ( PTA *pta );
l_ok boxaGetExtent ( BOXA *boxa, l_int32 *pw, l_int32 *ph, BOX **pbox );
l_ok boxaGetCoverage ( BOXA *boxa, l_int32 wc, l_int32 hc, l_int32 exactflag, l_float32 *pfract );
l_ok boxaaSizeRange ( BOXAA *baa, l_int32 *pminw, l_int32 *pminh, l_int32 *pmaxw, l_int32 *pmaxh );
l_ok boxaSizeRange ( BOXA *boxa, l_int32 *pminw, l_int32 *pminh, l_int32 *pmaxw, l_int32 *pmaxh );
l_ok boxaLocationRange ( BOXA *boxa, l_int32 *pminx, l_int32 *pminy, l_int32 *pmaxx, l_int32 *pmaxy );
l_ok boxaGetSizes ( BOXA *boxa, NUMA **pnaw, NUMA **pnah );
l_ok boxaGetArea ( BOXA *boxa, l_int32 *parea );
PIX * boxaDisplayTiled ( BOXA *boxas, PIXA *pixa, l_int32 first, l_int32 last, l_int32 maxwidth, l_int32 linewidth, l_float32 scalefactor, l_int32 background, l_int32 spacing, l_int32 border );
BOXA * boxaSmoothSequenceLS ( BOXA *boxas, l_float32 factor, l_int32 subflag, l_int32 maxdiff, l_int32 extrapixels, l_int32 debug );
BOXA * boxaSmoothSequenceMedian ( BOXA *boxas, l_int32 halfwin, l_int32 subflag, l_int32 maxdiff, l_int32 extrapixels, l_int32 debug );
BOXA * boxaLinearFit ( BOXA *boxas, l_float32 factor, l_int32 debug );
BOXA * boxaWindowedMedian ( BOXA *boxas, l_int32 halfwin, l_int32 debug );
BOXA * boxaModifyWithBoxa ( BOXA *boxas, BOXA *boxam, l_int32 subflag, l_int32 maxdiff, l_int32 extrapixels );
BOXA * boxaConstrainSize ( BOXA *boxas, l_int32 width, l_int32 widthflag, l_int32 height, l_int32 heightflag );
BOXA * boxaReconcileEvenOddHeight ( BOXA *boxas, l_int32 sides, l_int32 delh, l_int32 op, l_float32 factor, l_int32 start );
BOXA * boxaReconcilePairWidth ( BOXA *boxas, l_int32 delw, l_int32 op, l_float32 factor, NUMA *na );
l_ok boxaSizeConsistency1 ( BOXA *boxas, l_int32 type, l_float32 threshp, l_float32 threshm, l_float32 *pfvarp, l_float32 *pfvarm, l_int32 *psame );
l_ok boxaSizeConsistency2 ( BOXA *boxas, l_float32 *pfdevw, l_float32 *pfdevh, l_int32 debug );
BOXA * boxaReconcileSizeByMedian ( BOXA *boxas, l_int32 type, l_float32 fract, l_float32 factor, NUMA **pnadelw, NUMA **pnadelh, l_float32 *pratiowh );
l_ok boxaPlotSides ( BOXA *boxa, const char *plotname, NUMA **pnal, NUMA **pnat, NUMA **pnar, NUMA **pnab, PIX **ppixd );
l_ok boxaPlotSizes ( BOXA *boxa, const char *plotname, NUMA **pnaw, NUMA **pnah, PIX **ppixd );
BOXA * boxaFillSequence ( BOXA *boxas, l_int32 useflag, l_int32 debug );
l_ok boxaSizeVariation ( BOXA *boxa, l_int32 type, l_float32 *pdel_evenodd, l_float32 *prms_even, l_float32 *prms_odd, l_float32 *prms_all );
l_ok boxaMedianDimensions ( BOXA *boxas, l_int32 *pmedw, l_int32 *pmedh, l_int32 *pmedwe, l_int32 *pmedwo, l_int32 *pmedhe, l_int32 *pmedho, NUMA **pnadelw, NUMA **pnadelh );
L_BYTEA * l_byteaCreate ( size_t nbytes );
L_BYTEA * l_byteaInitFromMem ( const l_uint8 *data, size_t size );
L_BYTEA * l_byteaInitFromFile ( const char *fname );
L_BYTEA * l_byteaInitFromStream ( FILE *fp );
L_BYTEA * l_byteaCopy ( L_BYTEA *bas, l_int32 copyflag );
void l_byteaDestroy ( L_BYTEA **pba );
size_t l_byteaGetSize ( L_BYTEA *ba );
l_uint8 * l_byteaGetData ( L_BYTEA *ba, size_t *psize );
l_uint8 * l_byteaCopyData ( L_BYTEA *ba, size_t *psize );
l_ok l_byteaAppendData ( L_BYTEA *ba, const l_uint8 *newdata, size_t newbytes );
l_ok l_byteaAppendString ( L_BYTEA *ba, const char *str );
l_ok l_byteaJoin ( L_BYTEA *ba1, L_BYTEA **pba2 );
l_ok l_byteaSplit ( L_BYTEA *ba1, size_t splitloc, L_BYTEA **pba2 );
l_ok l_byteaFindEachSequence ( L_BYTEA *ba, const l_uint8 *sequence, size_t seqlen, L_DNA **pda );
l_ok l_byteaWrite ( const char *fname, L_BYTEA *ba, size_t startloc, size_t nbytes );
l_ok l_byteaWriteStream ( FILE *fp, L_BYTEA *ba, size_t startloc, size_t nbytes );
CCBORDA * ccbaCreate ( PIX *pixs, l_int32 n );
void ccbaDestroy ( CCBORDA **pccba );
CCBORD * ccbCreate ( PIX *pixs );
void ccbDestroy ( CCBORD **pccb );
l_ok ccbaAddCcb ( CCBORDA *ccba, CCBORD *ccb );
l_int32 ccbaGetCount ( CCBORDA *ccba );
CCBORD * ccbaGetCcb ( CCBORDA *ccba, l_int32 index );
CCBORDA * pixGetAllCCBorders ( PIX *pixs );
CCBORD * pixGetCCBorders ( PIX *pixs, BOX *box );
PTAA * pixGetOuterBordersPtaa ( PIX *pixs );
PTA * pixGetOuterBorderPta ( PIX *pixs, BOX *box );
l_ok pixGetOuterBorder ( CCBORD *ccb, PIX *pixs, BOX *box );
l_ok pixGetHoleBorder ( CCBORD *ccb, PIX *pixs, BOX *box, l_int32 xs, l_int32 ys );
l_int32 findNextBorderPixel ( l_int32 w, l_int32 h, l_uint32 *data, l_int32 wpl, l_int32 px, l_int32 py, l_int32 *pqpos, l_int32 *pnpx, l_int32 *pnpy );
void locateOutsideSeedPixel ( l_int32 fpx, l_int32 fpy, l_int32 spx, l_int32 spy, l_int32 *pxs, l_int32 *pys );
l_ok ccbaGenerateGlobalLocs ( CCBORDA *ccba );
l_ok ccbaGenerateStepChains ( CCBORDA *ccba );
l_ok ccbaStepChainsToPixCoords ( CCBORDA *ccba, l_int32 coordtype );
l_ok ccbaGenerateSPGlobalLocs ( CCBORDA *ccba, l_int32 ptsflag );
l_ok ccbaGenerateSinglePath ( CCBORDA *ccba );
PTA * getCutPathForHole ( PIX *pix, PTA *pta, BOX *boxinner, l_int32 *pdir, l_int32 *plen );
PIX * ccbaDisplayBorder ( CCBORDA *ccba );
PIX * ccbaDisplaySPBorder ( CCBORDA *ccba );
PIX * ccbaDisplayImage1 ( CCBORDA *ccba );
PIX * ccbaDisplayImage2 ( CCBORDA *ccba );
l_ok ccbaWrite ( const char *filename, CCBORDA *ccba );
l_ok ccbaWriteStream ( FILE *fp, CCBORDA *ccba );
CCBORDA * ccbaRead ( const char *filename );
CCBORDA * ccbaReadStream ( FILE *fp );
l_ok ccbaWriteSVG ( const char *filename, CCBORDA *ccba );
char * ccbaWriteSVGString ( const char *filename, CCBORDA *ccba );
PIXA * pixaThinConnected ( PIXA *pixas, l_int32 type, l_int32 connectivity, l_int32 maxiters );
PIX * pixThinConnected ( PIX *pixs, l_int32 type, l_int32 connectivity, l_int32 maxiters );
PIX * pixThinConnectedBySet ( PIX *pixs, l_int32 type, SELA *sela, l_int32 maxiters );
SELA * selaMakeThinSets ( l_int32 index, l_int32 debug );
l_ok jbCorrelation ( const char *dirin, l_float32 thresh, l_float32 weight, l_int32 components, const char *rootname, l_int32 firstpage, l_int32 npages, l_int32 renderflag );
l_ok jbRankHaus ( const char *dirin, l_int32 size, l_float32 rank, l_int32 components, const char *rootname, l_int32 firstpage, l_int32 npages, l_int32 renderflag );
JBCLASSER * jbWordsInTextlines ( const char *dirin, l_int32 reduction, l_int32 maxwidth, l_int32 maxheight, l_float32 thresh, l_float32 weight, NUMA **pnatl, l_int32 firstpage, l_int32 npages );
l_ok pixGetWordsInTextlines ( PIX *pixs, l_int32 minwidth, l_int32 minheight, l_int32 maxwidth, l_int32 maxheight, BOXA **pboxad, PIXA **ppixad, NUMA **pnai );
l_ok pixGetWordBoxesInTextlines ( PIX *pixs, l_int32 minwidth, l_int32 minheight, l_int32 maxwidth, l_int32 maxheight, BOXA **pboxad, NUMA **pnai );
l_ok pixFindWordAndCharacterBoxes ( PIX *pixs, BOX *boxs, l_int32 thresh, BOXA **pboxaw, BOXAA **pboxaac, const char *debugdir );
NUMAA * boxaExtractSortedPattern ( BOXA *boxa, NUMA *na );
l_ok numaaCompareImagesByBoxes ( NUMAA *naa1, NUMAA *naa2, l_int32 nperline, l_int32 nreq, l_int32 maxshiftx, l_int32 maxshifty, l_int32 delx, l_int32 dely, l_int32 *psame, l_int32 debugflag );
l_ok pixColorContent ( PIX *pixs, l_int32 rwhite, l_int32 gwhite, l_int32 bwhite, l_int32 mingray, PIX **ppixr, PIX **ppixg, PIX **ppixb );
PIX * pixColorMagnitude ( PIX *pixs, l_int32 rwhite, l_int32 gwhite, l_int32 bwhite, l_int32 type );
PIX * pixMaskOverColorPixels ( PIX *pixs, l_int32 threshdiff, l_int32 mindist );
PIX * pixMaskOverColorRange ( PIX *pixs, l_int32 rmin, l_int32 rmax, l_int32 gmin, l_int32 gmax, l_int32 bmin, l_int32 bmax );
l_ok pixColorFraction ( PIX *pixs, l_int32 darkthresh, l_int32 lightthresh, l_int32 diffthresh, l_int32 factor, l_float32 *ppixfract, l_float32 *pcolorfract );
l_ok pixFindColorRegions ( PIX *pixs, PIX *pixm, l_int32 factor, l_int32 lightthresh, l_int32 darkthresh, l_int32 mindiff, l_int32 colordiff, l_float32 edgefract, l_float32 *pcolorfract, PIX **pcolormask1, PIX **pcolormask2, PIXA *pixadb );
l_ok pixNumSignificantGrayColors ( PIX *pixs, l_int32 darkthresh, l_int32 lightthresh, l_float32 minfract, l_int32 factor, l_int32 *pncolors );
l_ok pixColorsForQuantization ( PIX *pixs, l_int32 thresh, l_int32 *pncolors, l_int32 *piscolor, l_int32 debug );
l_ok pixNumColors ( PIX *pixs, l_int32 factor, l_int32 *pncolors );
l_ok pixGetMostPopulatedColors ( PIX *pixs, l_int32 sigbits, l_int32 factor, l_int32 ncolors, l_uint32 **parray, PIXCMAP **pcmap );
PIX * pixSimpleColorQuantize ( PIX *pixs, l_int32 sigbits, l_int32 factor, l_int32 ncolors );
NUMA * pixGetRGBHistogram ( PIX *pixs, l_int32 sigbits, l_int32 factor );
l_ok makeRGBIndexTables ( l_uint32 **prtab, l_uint32 **pgtab, l_uint32 **pbtab, l_int32 sigbits );
l_ok getRGBFromIndex ( l_uint32 index, l_int32 sigbits, l_int32 *prval, l_int32 *pgval, l_int32 *pbval );
l_ok pixHasHighlightRed ( PIX *pixs, l_int32 factor, l_float32 fract, l_float32 fthresh, l_int32 *phasred, l_float32 *pratio, PIX **ppixdb );
PIX * pixColorGrayRegions ( PIX *pixs, BOXA *boxa, l_int32 type, l_int32 thresh, l_int32 rval, l_int32 gval, l_int32 bval );
l_ok pixColorGray ( PIX *pixs, BOX *box, l_int32 type, l_int32 thresh, l_int32 rval, l_int32 gval, l_int32 bval );
PIX * pixColorGrayMasked ( PIX *pixs, PIX *pixm, l_int32 type, l_int32 thresh, l_int32 rval, l_int32 gval, l_int32 bval );
PIX * pixSnapColor ( PIX *pixd, PIX *pixs, l_uint32 srcval, l_uint32 dstval, l_int32 diff );
PIX * pixSnapColorCmap ( PIX *pixd, PIX *pixs, l_uint32 srcval, l_uint32 dstval, l_int32 diff );
PIX * pixLinearMapToTargetColor ( PIX *pixd, PIX *pixs, l_uint32 srcval, l_uint32 dstval );
l_ok pixelLinearMapToTargetColor ( l_uint32 scolor, l_uint32 srcmap, l_uint32 dstmap, l_uint32 *pdcolor );
PIX * pixShiftByComponent ( PIX *pixd, PIX *pixs, l_uint32 srcval, l_uint32 dstval );
l_ok pixelShiftByComponent ( l_int32 rval, l_int32 gval, l_int32 bval, l_uint32 srcval, l_uint32 dstval, l_uint32 *ppixel );
l_ok pixelFractionalShift ( l_int32 rval, l_int32 gval, l_int32 bval, l_float32 fraction, l_uint32 *ppixel );
PIXCMAP * pixcmapCreate ( l_int32 depth );
PIXCMAP * pixcmapCreateRandom ( l_int32 depth, l_int32 hasblack, l_int32 haswhite );
PIXCMAP * pixcmapCreateLinear ( l_int32 d, l_int32 nlevels );
PIXCMAP * pixcmapCopy ( PIXCMAP *cmaps );
void pixcmapDestroy ( PIXCMAP **pcmap );
l_ok pixcmapIsValid ( PIXCMAP *cmap, l_int32 *pvalid );
l_ok pixcmapAddColor ( PIXCMAP *cmap, l_int32 rval, l_int32 gval, l_int32 bval );
l_ok pixcmapAddRGBA ( PIXCMAP *cmap, l_int32 rval, l_int32 gval, l_int32 bval, l_int32 aval );
l_ok pixcmapAddNewColor ( PIXCMAP *cmap, l_int32 rval, l_int32 gval, l_int32 bval, l_int32 *pindex );
l_ok pixcmapAddNearestColor ( PIXCMAP *cmap, l_int32 rval, l_int32 gval, l_int32 bval, l_int32 *pindex );
l_ok pixcmapUsableColor ( PIXCMAP *cmap, l_int32 rval, l_int32 gval, l_int32 bval, l_int32 *pusable );
l_ok pixcmapAddBlackOrWhite ( PIXCMAP *cmap, l_int32 color, l_int32 *pindex );
l_ok pixcmapSetBlackAndWhite ( PIXCMAP *cmap, l_int32 setblack, l_int32 setwhite );
l_int32 pixcmapGetCount ( PIXCMAP *cmap );
l_int32 pixcmapGetFreeCount ( PIXCMAP *cmap );
l_int32 pixcmapGetDepth ( PIXCMAP *cmap );
l_ok pixcmapGetMinDepth ( PIXCMAP *cmap, l_int32 *pmindepth );
l_ok pixcmapClear ( PIXCMAP *cmap );
l_ok pixcmapGetColor ( PIXCMAP *cmap, l_int32 index, l_int32 *prval, l_int32 *pgval, l_int32 *pbval );
l_ok pixcmapGetColor32 ( PIXCMAP *cmap, l_int32 index, l_uint32 *pval32 );
l_ok pixcmapGetRGBA ( PIXCMAP *cmap, l_int32 index, l_int32 *prval, l_int32 *pgval, l_int32 *pbval, l_int32 *paval );
l_ok pixcmapGetRGBA32 ( PIXCMAP *cmap, l_int32 index, l_uint32 *pval32 );
l_ok pixcmapResetColor ( PIXCMAP *cmap, l_int32 index, l_int32 rval, l_int32 gval, l_int32 bval );
l_ok pixcmapSetAlpha ( PIXCMAP *cmap, l_int32 index, l_int32 aval );
l_int32 pixcmapGetIndex ( PIXCMAP *cmap, l_int32 rval, l_int32 gval, l_int32 bval, l_int32 *pindex );
l_ok pixcmapHasColor ( PIXCMAP *cmap, l_int32 *pcolor );
l_ok pixcmapIsOpaque ( PIXCMAP *cmap, l_int32 *popaque );
l_ok pixcmapIsBlackAndWhite ( PIXCMAP *cmap, l_int32 *pblackwhite );
l_ok pixcmapCountGrayColors ( PIXCMAP *cmap, l_int32 *pngray );
l_ok pixcmapGetRankIntensity ( PIXCMAP *cmap, l_float32 rankval, l_int32 *pindex );
l_ok pixcmapGetNearestIndex ( PIXCMAP *cmap, l_int32 rval, l_int32 gval, l_int32 bval, l_int32 *pindex );
l_ok pixcmapGetNearestGrayIndex ( PIXCMAP *cmap, l_int32 val, l_int32 *pindex );
l_ok pixcmapGetDistanceToColor ( PIXCMAP *cmap, l_int32 index, l_int32 rval, l_int32 gval, l_int32 bval, l_int32 *pdist );
l_ok pixcmapGetRangeValues ( PIXCMAP *cmap, l_int32 select, l_int32 *pminval, l_int32 *pmaxval, l_int32 *pminindex, l_int32 *pmaxindex );
PIXCMAP * pixcmapGrayToColor ( l_uint32 color );
PIXCMAP * pixcmapColorToGray ( PIXCMAP *cmaps, l_float32 rwt, l_float32 gwt, l_float32 bwt );
PIXCMAP * pixcmapConvertTo4 ( PIXCMAP *cmaps );
PIXCMAP * pixcmapConvertTo8 ( PIXCMAP *cmaps );
PIXCMAP * pixcmapRead ( const char *filename );
PIXCMAP * pixcmapReadStream ( FILE *fp );
PIXCMAP * pixcmapReadMem ( const l_uint8 *data, size_t size );
l_ok pixcmapWrite ( const char *filename, PIXCMAP *cmap );
l_ok pixcmapWriteStream ( FILE *fp, PIXCMAP *cmap );
l_ok pixcmapWriteMem ( l_uint8 **pdata, size_t *psize, PIXCMAP *cmap );
l_ok pixcmapToArrays ( PIXCMAP *cmap, l_int32 **prmap, l_int32 **pgmap, l_int32 **pbmap, l_int32 **pamap );
l_ok pixcmapToRGBTable ( PIXCMAP *cmap, l_uint32 **ptab, l_int32 *pncolors );
l_ok pixcmapSerializeToMemory ( PIXCMAP *cmap, l_int32 cpc, l_int32 *pncolors, l_uint8 **pdata );
PIXCMAP * pixcmapDeserializeFromMemory ( l_uint8 *data, l_int32 cpc, l_int32 ncolors );
char * pixcmapConvertToHex ( l_uint8 *data, l_int32 ncolors );
l_ok pixcmapGammaTRC ( PIXCMAP *cmap, l_float32 gamma, l_int32 minval, l_int32 maxval );
l_ok pixcmapContrastTRC ( PIXCMAP *cmap, l_float32 factor );
l_ok pixcmapShiftIntensity ( PIXCMAP *cmap, l_float32 fraction );
l_ok pixcmapShiftByComponent ( PIXCMAP *cmap, l_uint32 srcval, l_uint32 dstval );
PIX * pixColorMorph ( PIX *pixs, l_int32 type, l_int32 hsize, l_int32 vsize );
PIX * pixOctreeColorQuant ( PIX *pixs, l_int32 colors, l_int32 ditherflag );
PIX * pixOctreeColorQuantGeneral ( PIX *pixs, l_int32 colors, l_int32 ditherflag, l_float32 validthresh, l_float32 colorthresh );
l_ok makeRGBToIndexTables ( l_uint32 **prtab, l_uint32 **pgtab, l_uint32 **pbtab, l_int32 cqlevels );
void getOctcubeIndexFromRGB ( l_int32 rval, l_int32 gval, l_int32 bval, l_uint32 *rtab, l_uint32 *gtab, l_uint32 *btab, l_uint32 *pindex );
PIX * pixOctreeQuantByPopulation ( PIX *pixs, l_int32 level, l_int32 ditherflag );
PIX * pixOctreeQuantNumColors ( PIX *pixs, l_int32 maxcolors, l_int32 subsample );
PIX * pixOctcubeQuantMixedWithGray ( PIX *pixs, l_int32 depth, l_int32 graylevels, l_int32 delta );
PIX * pixFixedOctcubeQuant256 ( PIX *pixs, l_int32 ditherflag );
PIX * pixFewColorsOctcubeQuant1 ( PIX *pixs, l_int32 level );
PIX * pixFewColorsOctcubeQuant2 ( PIX *pixs, l_int32 level, NUMA *na, l_int32 ncolors, l_int32 *pnerrors );
PIX * pixFewColorsOctcubeQuantMixed ( PIX *pixs, l_int32 level, l_int32 darkthresh, l_int32 lightthresh, l_int32 diffthresh, l_float32 minfract, l_int32 maxspan );
PIX * pixFixedOctcubeQuantGenRGB ( PIX *pixs, l_int32 level );
PIX * pixQuantFromCmap ( PIX *pixs, PIXCMAP *cmap, l_int32 mindepth, l_int32 level, l_int32 metric );
PIX * pixOctcubeQuantFromCmap ( PIX *pixs, PIXCMAP *cmap, l_int32 mindepth, l_int32 level, l_int32 metric );
NUMA * pixOctcubeHistogram ( PIX *pixs, l_int32 level, l_int32 *pncolors );
l_int32 * pixcmapToOctcubeLUT ( PIXCMAP *cmap, l_int32 level, l_int32 metric );
l_ok pixRemoveUnusedColors ( PIX *pixs );
l_ok pixNumberOccupiedOctcubes ( PIX *pix, l_int32 level, l_int32 mincount, l_float32 minfract, l_int32 *pncolors );
PIX * pixMedianCutQuant ( PIX *pixs, l_int32 ditherflag );
PIX * pixMedianCutQuantGeneral ( PIX *pixs, l_int32 ditherflag, l_int32 outdepth, l_int32 maxcolors, l_int32 sigbits, l_int32 maxsub, l_int32 checkbw );
PIX * pixMedianCutQuantMixed ( PIX *pixs, l_int32 ncolor, l_int32 ngray, l_int32 darkthresh, l_int32 lightthresh, l_int32 diffthresh );
PIX * pixFewColorsMedianCutQuantMixed ( PIX *pixs, l_int32 ncolor, l_int32 ngray, l_int32 maxncolors, l_int32 darkthresh, l_int32 lightthresh, l_int32 diffthresh );
l_int32 * pixMedianCutHisto ( PIX *pixs, l_int32 sigbits, l_int32 subsample );
PIX * pixColorSegment ( PIX *pixs, l_int32 maxdist, l_int32 maxcolors, l_int32 selsize, l_int32 finalcolors, l_int32 debugflag );
PIX * pixColorSegmentCluster ( PIX *pixs, l_int32 maxdist, l_int32 maxcolors, l_int32 debugflag );
l_ok pixAssignToNearestColor ( PIX *pixd, PIX *pixs, PIX *pixm, l_int32 level, l_int32 *countarray );
l_ok pixColorSegmentClean ( PIX *pixs, l_int32 selsize, l_int32 *countarray );
l_ok pixColorSegmentRemoveColors ( PIX *pixd, PIX *pixs, l_int32 finalcolors );
PIX * pixConvertRGBToHSV ( PIX *pixd, PIX *pixs );
PIX * pixConvertHSVToRGB ( PIX *pixd, PIX *pixs );
l_ok convertRGBToHSV ( l_int32 rval, l_int32 gval, l_int32 bval, l_int32 *phval, l_int32 *psval, l_int32 *pvval );
l_ok convertHSVToRGB ( l_int32 hval, l_int32 sval, l_int32 vval, l_int32 *prval, l_int32 *pgval, l_int32 *pbval );
l_ok pixcmapConvertRGBToHSV ( PIXCMAP *cmap );
l_ok pixcmapConvertHSVToRGB ( PIXCMAP *cmap );
PIX * pixConvertRGBToHue ( PIX *pixs );
PIX * pixConvertRGBToSaturation ( PIX *pixs );
PIX * pixConvertRGBToValue ( PIX *pixs );
PIX * pixMakeRangeMaskHS ( PIX *pixs, l_int32 huecenter, l_int32 huehw, l_int32 satcenter, l_int32 sathw, l_int32 regionflag );
PIX * pixMakeRangeMaskHV ( PIX *pixs, l_int32 huecenter, l_int32 huehw, l_int32 valcenter, l_int32 valhw, l_int32 regionflag );
PIX * pixMakeRangeMaskSV ( PIX *pixs, l_int32 satcenter, l_int32 sathw, l_int32 valcenter, l_int32 valhw, l_int32 regionflag );
PIX * pixMakeHistoHS ( PIX *pixs, l_int32 factor, NUMA **pnahue, NUMA **pnasat );
PIX * pixMakeHistoHV ( PIX *pixs, l_int32 factor, NUMA **pnahue, NUMA **pnaval );
PIX * pixMakeHistoSV ( PIX *pixs, l_int32 factor, NUMA **pnasat, NUMA **pnaval );
l_ok pixFindHistoPeaksHSV ( PIX *pixs, l_int32 type, l_int32 width, l_int32 height, l_int32 npeaks, l_float32 erasefactor, PTA **ppta, NUMA **pnatot, PIXA **ppixa );
PIX * displayHSVColorRange ( l_int32 hval, l_int32 sval, l_int32 vval, l_int32 huehw, l_int32 sathw, l_int32 nsamp, l_int32 factor );
PIX * pixConvertRGBToYUV ( PIX *pixd, PIX *pixs );
PIX * pixConvertYUVToRGB ( PIX *pixd, PIX *pixs );
l_ok convertRGBToYUV ( l_int32 rval, l_int32 gval, l_int32 bval, l_int32 *pyval, l_int32 *puval, l_int32 *pvval );
l_ok convertYUVToRGB ( l_int32 yval, l_int32 uval, l_int32 vval, l_int32 *prval, l_int32 *pgval, l_int32 *pbval );
l_ok pixcmapConvertRGBToYUV ( PIXCMAP *cmap );
l_ok pixcmapConvertYUVToRGB ( PIXCMAP *cmap );
FPIXA * pixConvertRGBToXYZ ( PIX *pixs );
PIX * fpixaConvertXYZToRGB ( FPIXA *fpixa );
l_ok convertRGBToXYZ ( l_int32 rval, l_int32 gval, l_int32 bval, l_float32 *pfxval, l_float32 *pfyval, l_float32 *pfzval );
l_ok convertXYZToRGB ( l_float32 fxval, l_float32 fyval, l_float32 fzval, l_int32 blackout, l_int32 *prval, l_int32 *pgval, l_int32 *pbval );
FPIXA * fpixaConvertXYZToLAB ( FPIXA *fpixas );
FPIXA * fpixaConvertLABToXYZ ( FPIXA *fpixas );
l_ok convertXYZToLAB ( l_float32 xval, l_float32 yval, l_float32 zval, l_float32 *plval, l_float32 *paval, l_float32 *pbval );
l_ok convertLABToXYZ ( l_float32 lval, l_float32 aval, l_float32 bval, l_float32 *pxval, l_float32 *pyval, l_float32 *pzval );
FPIXA * pixConvertRGBToLAB ( PIX *pixs );
PIX * fpixaConvertLABToRGB ( FPIXA *fpixa );
l_ok convertRGBToLAB ( l_int32 rval, l_int32 gval, l_int32 bval, l_float32 *pflval, l_float32 *pfaval, l_float32 *pfbval );
l_ok convertLABToRGB ( l_float32 flval, l_float32 faval, l_float32 fbval, l_int32 *prval, l_int32 *pgval, l_int32 *pbval );
l_ok pixEqual ( PIX *pix1, PIX *pix2, l_int32 *psame );
l_ok pixEqualWithAlpha ( PIX *pix1, PIX *pix2, l_int32 use_alpha, l_int32 *psame );
l_ok pixEqualWithCmap ( PIX *pix1, PIX *pix2, l_int32 *psame );
l_ok cmapEqual ( PIXCMAP *cmap1, PIXCMAP *cmap2, l_int32 ncomps, l_int32 *psame );
l_ok pixUsesCmapColor ( PIX *pixs, l_int32 *pcolor );
l_ok pixCorrelationBinary ( PIX *pix1, PIX *pix2, l_float32 *pval );
PIX * pixDisplayDiffBinary ( PIX *pix1, PIX *pix2 );
l_ok pixCompareBinary ( PIX *pix1, PIX *pix2, l_int32 comptype, l_float32 *pfract, PIX **ppixdiff );
l_ok pixCompareGrayOrRGB ( PIX *pix1, PIX *pix2, l_int32 comptype, l_int32 plottype, l_int32 *psame, l_float32 *pdiff, l_float32 *prmsdiff, PIX **ppixdiff );
l_ok pixCompareGray ( PIX *pix1, PIX *pix2, l_int32 comptype, l_int32 plottype, l_int32 *psame, l_float32 *pdiff, l_float32 *prmsdiff, PIX **ppixdiff );
l_ok pixCompareRGB ( PIX *pix1, PIX *pix2, l_int32 comptype, l_int32 plottype, l_int32 *psame, l_float32 *pdiff, l_float32 *prmsdiff, PIX **ppixdiff );
l_ok pixCompareTiled ( PIX *pix1, PIX *pix2, l_int32 sx, l_int32 sy, l_int32 type, PIX **ppixdiff );
NUMA * pixCompareRankDifference ( PIX *pix1, PIX *pix2, l_int32 factor );
l_ok pixTestForSimilarity ( PIX *pix1, PIX *pix2, l_int32 factor, l_int32 mindiff, l_float32 maxfract, l_float32 maxave, l_int32 *psimilar, l_int32 details );
l_ok pixGetDifferenceStats ( PIX *pix1, PIX *pix2, l_int32 factor, l_int32 mindiff, l_float32 *pfractdiff, l_float32 *pavediff, l_int32 details );
NUMA * pixGetDifferenceHistogram ( PIX *pix1, PIX *pix2, l_int32 factor );
l_ok pixGetPerceptualDiff ( PIX *pixs1, PIX *pixs2, l_int32 sampling, l_int32 dilation, l_int32 mindiff, l_float32 *pfract, PIX **ppixdiff1, PIX **ppixdiff2 );
l_ok pixGetPSNR ( PIX *pix1, PIX *pix2, l_int32 factor, l_float32 *ppsnr );
l_ok pixaComparePhotoRegionsByHisto ( PIXA *pixa, l_float32 minratio, l_float32 textthresh, l_int32 factor, l_int32 nx, l_int32 ny, l_float32 simthresh, NUMA **pnai, l_float32 **pscores, PIX **ppixd, l_int32 debug );
l_ok pixComparePhotoRegionsByHisto ( PIX *pix1, PIX *pix2, BOX *box1, BOX *box2, l_float32 minratio, l_int32 factor, l_int32 nx, l_int32 ny, l_float32 *pscore, l_int32 debugflag );
l_ok pixGenPhotoHistos ( PIX *pixs, BOX *box, l_int32 factor, l_float32 thresh, l_int32 nx, l_int32 ny, NUMAA **pnaa, l_int32 *pw, l_int32 *ph, l_int32 debugindex );
PIX * pixPadToCenterCentroid ( PIX *pixs, l_int32 factor );
l_ok pixCentroid8 ( PIX *pixs, l_int32 factor, l_float32 *pcx, l_float32 *pcy );
l_ok pixDecideIfPhotoImage ( PIX *pix, l_int32 factor, l_int32 nx, l_int32 ny, l_float32 thresh, NUMAA **pnaa, PIXA *pixadebug );
l_ok compareTilesByHisto ( NUMAA *naa1, NUMAA *naa2, l_float32 minratio, l_int32 w1, l_int32 h1, l_int32 w2, l_int32 h2, l_float32 *pscore, PIXA *pixadebug );
l_ok pixCompareGrayByHisto ( PIX *pix1, PIX *pix2, BOX *box1, BOX *box2, l_float32 minratio, l_int32 maxgray, l_int32 factor, l_int32 nx, l_int32 ny, l_float32 *pscore, l_int32 debugflag );
l_ok pixCropAlignedToCentroid ( PIX *pix1, PIX *pix2, l_int32 factor, BOX **pbox1, BOX **pbox2 );
l_uint8 * l_compressGrayHistograms ( NUMAA *naa, l_int32 w, l_int32 h, size_t *psize );
NUMAA * l_uncompressGrayHistograms ( l_uint8 *bytea, size_t size, l_int32 *pw, l_int32 *ph );
l_ok pixCompareWithTranslation ( PIX *pix1, PIX *pix2, l_int32 thresh, l_int32 *pdelx, l_int32 *pdely, l_float32 *pscore, l_int32 debugflag );
l_ok pixBestCorrelation ( PIX *pix1, PIX *pix2, l_int32 area1, l_int32 area2, l_int32 etransx, l_int32 etransy, l_int32 maxshift, l_int32 *tab8, l_int32 *pdelx, l_int32 *pdely, l_float32 *pscore, l_int32 debugflag );
BOXA * pixConnComp ( PIX *pixs, PIXA **ppixa, l_int32 connectivity );
BOXA * pixConnCompPixa ( PIX *pixs, PIXA **ppixa, l_int32 connectivity );
BOXA * pixConnCompBB ( PIX *pixs, l_int32 connectivity );
l_ok pixCountConnComp ( PIX *pixs, l_int32 connectivity, l_int32 *pcount );
l_int32 nextOnPixelInRaster ( PIX *pixs, l_int32 xstart, l_int32 ystart, l_int32 *px, l_int32 *py );
BOX * pixSeedfillBB ( PIX *pixs, L_STACK *stack, l_int32 x, l_int32 y, l_int32 connectivity );
BOX * pixSeedfill4BB ( PIX *pixs, L_STACK *stack, l_int32 x, l_int32 y );
BOX * pixSeedfill8BB ( PIX *pixs, L_STACK *stack, l_int32 x, l_int32 y );
l_ok pixSeedfill ( PIX *pixs, L_STACK *stack, l_int32 x, l_int32 y, l_int32 connectivity );
l_ok pixSeedfill4 ( PIX *pixs, L_STACK *stack, l_int32 x, l_int32 y );
l_ok pixSeedfill8 ( PIX *pixs, L_STACK *stack, l_int32 x, l_int32 y );
l_ok convertFilesTo1bpp ( const char *dirin, const char *substr, l_int32 upscaling, l_int32 thresh, l_int32 firstpage, l_int32 npages, const char *dirout, l_int32 outformat );
PIX * pixBlockconv ( PIX *pix, l_int32 wc, l_int32 hc );
PIX * pixBlockconvGray ( PIX *pixs, PIX *pixacc, l_int32 wc, l_int32 hc );
PIX * pixBlockconvAccum ( PIX *pixs );
PIX * pixBlockconvGrayUnnormalized ( PIX *pixs, l_int32 wc, l_int32 hc );
PIX * pixBlockconvTiled ( PIX *pix, l_int32 wc, l_int32 hc, l_int32 nx, l_int32 ny );
PIX * pixBlockconvGrayTile ( PIX *pixs, PIX *pixacc, l_int32 wc, l_int32 hc );
l_ok pixWindowedStats ( PIX *pixs, l_int32 wc, l_int32 hc, l_int32 hasborder, PIX **ppixm, PIX **ppixms, FPIX **pfpixv, FPIX **pfpixrv );
PIX * pixWindowedMean ( PIX *pixs, l_int32 wc, l_int32 hc, l_int32 hasborder, l_int32 normflag );
PIX * pixWindowedMeanSquare ( PIX *pixs, l_int32 wc, l_int32 hc, l_int32 hasborder );
l_ok pixWindowedVariance ( PIX *pixm, PIX *pixms, FPIX **pfpixv, FPIX **pfpixrv );
DPIX * pixMeanSquareAccum ( PIX *pixs );
PIX * pixBlockrank ( PIX *pixs, PIX *pixacc, l_int32 wc, l_int32 hc, l_float32 rank );
PIX * pixBlocksum ( PIX *pixs, PIX *pixacc, l_int32 wc, l_int32 hc );
PIX * pixCensusTransform ( PIX *pixs, l_int32 halfsize, PIX *pixacc );
PIX * pixConvolve ( PIX *pixs, L_KERNEL *kel, l_int32 outdepth, l_int32 normflag );
PIX * pixConvolveSep ( PIX *pixs, L_KERNEL *kelx, L_KERNEL *kely, l_int32 outdepth, l_int32 normflag );
PIX * pixConvolveRGB ( PIX *pixs, L_KERNEL *kel );
PIX * pixConvolveRGBSep ( PIX *pixs, L_KERNEL *kelx, L_KERNEL *kely );
FPIX * fpixConvolve ( FPIX *fpixs, L_KERNEL *kel, l_int32 normflag );
FPIX * fpixConvolveSep ( FPIX *fpixs, L_KERNEL *kelx, L_KERNEL *kely, l_int32 normflag );
PIX * pixConvolveWithBias ( PIX *pixs, L_KERNEL *kel1, L_KERNEL *kel2, l_int32 force8, l_int32 *pbias );
void l_setConvolveSampling ( l_int32 xfact, l_int32 yfact );
PIX * pixAddGaussianNoise ( PIX *pixs, l_float32 stdev );
l_float32 gaussDistribSampling (  );
l_ok pixCorrelationScore ( PIX *pix1, PIX *pix2, l_int32 area1, l_int32 area2, l_float32 delx, l_float32 dely, l_int32 maxdiffw, l_int32 maxdiffh, l_int32 *tab, l_float32 *pscore );
l_int32 pixCorrelationScoreThresholded ( PIX *pix1, PIX *pix2, l_int32 area1, l_int32 area2, l_float32 delx, l_float32 dely, l_int32 maxdiffw, l_int32 maxdiffh, l_int32 *tab, l_int32 *downcount, l_float32 score_threshold );
l_ok pixCorrelationScoreSimple ( PIX *pix1, PIX *pix2, l_int32 area1, l_int32 area2, l_float32 delx, l_float32 dely, l_int32 maxdiffw, l_int32 maxdiffh, l_int32 *tab, l_float32 *pscore );
l_ok pixCorrelationScoreShifted ( PIX *pix1, PIX *pix2, l_int32 area1, l_int32 area2, l_int32 delx, l_int32 dely, l_int32 *tab, l_float32 *pscore );
L_DEWARP * dewarpCreate ( PIX *pixs, l_int32 pageno );
L_DEWARP * dewarpCreateRef ( l_int32 pageno, l_int32 refpage );
void dewarpDestroy ( L_DEWARP **pdew );
L_DEWARPA * dewarpaCreate ( l_int32 nptrs, l_int32 sampling, l_int32 redfactor, l_int32 minlines, l_int32 maxdist );
L_DEWARPA * dewarpaCreateFromPixacomp ( PIXAC *pixac, l_int32 useboth, l_int32 sampling, l_int32 minlines, l_int32 maxdist );
void dewarpaDestroy ( L_DEWARPA **pdewa );
l_ok dewarpaDestroyDewarp ( L_DEWARPA *dewa, l_int32 pageno );
l_ok dewarpaInsertDewarp ( L_DEWARPA *dewa, L_DEWARP *dew );
L_DEWARP * dewarpaGetDewarp ( L_DEWARPA *dewa, l_int32 index );
l_ok dewarpaSetCurvatures ( L_DEWARPA *dewa, l_int32 max_linecurv, l_int32 min_diff_linecurv, l_int32 max_diff_linecurv, l_int32 max_edgecurv, l_int32 max_diff_edgecurv, l_int32 max_edgeslope );
l_ok dewarpaUseBothArrays ( L_DEWARPA *dewa, l_int32 useboth );
l_ok dewarpaSetCheckColumns ( L_DEWARPA *dewa, l_int32 check_columns );
l_ok dewarpaSetMaxDistance ( L_DEWARPA *dewa, l_int32 maxdist );
L_DEWARP * dewarpRead ( const char *filename );
L_DEWARP * dewarpReadStream ( FILE *fp );
L_DEWARP * dewarpReadMem ( const l_uint8 *data, size_t size );
l_ok dewarpWrite ( const char *filename, L_DEWARP *dew );
l_ok dewarpWriteStream ( FILE *fp, L_DEWARP *dew );
l_ok dewarpWriteMem ( l_uint8 **pdata, size_t *psize, L_DEWARP *dew );
L_DEWARPA * dewarpaRead ( const char *filename );
L_DEWARPA * dewarpaReadStream ( FILE *fp );
L_DEWARPA * dewarpaReadMem ( const l_uint8 *data, size_t size );
l_ok dewarpaWrite ( const char *filename, L_DEWARPA *dewa );
l_ok dewarpaWriteStream ( FILE *fp, L_DEWARPA *dewa );
l_ok dewarpaWriteMem ( l_uint8 **pdata, size_t *psize, L_DEWARPA *dewa );
l_ok dewarpBuildPageModel ( L_DEWARP *dew, const char *debugfile );
l_ok dewarpFindVertDisparity ( L_DEWARP *dew, PTAA *ptaa, l_int32 rotflag );
l_ok dewarpFindHorizDisparity ( L_DEWARP *dew, PTAA *ptaa );
PTAA * dewarpGetTextlineCenters ( PIX *pixs, l_int32 debugflag );
PTAA * dewarpRemoveShortLines ( PIX *pixs, PTAA *ptaas, l_float32 fract, l_int32 debugflag );
l_ok dewarpFindHorizSlopeDisparity ( L_DEWARP *dew, PIX *pixb, l_float32 fractthresh, l_int32 parity );
l_ok dewarpBuildLineModel ( L_DEWARP *dew, l_int32 opensize, const char *debugfile );
l_ok dewarpaModelStatus ( L_DEWARPA *dewa, l_int32 pageno, l_int32 *pvsuccess, l_int32 *phsuccess );
l_ok dewarpaApplyDisparity ( L_DEWARPA *dewa, l_int32 pageno, PIX *pixs, l_int32 grayin, l_int32 x, l_int32 y, PIX **ppixd, const char *debugfile );
l_ok dewarpaApplyDisparityBoxa ( L_DEWARPA *dewa, l_int32 pageno, PIX *pixs, BOXA *boxas, l_int32 mapdir, l_int32 x, l_int32 y, BOXA **pboxad, const char *debugfile );
l_ok dewarpMinimize ( L_DEWARP *dew );
l_ok dewarpPopulateFullRes ( L_DEWARP *dew, PIX *pix, l_int32 x, l_int32 y );
l_ok dewarpSinglePage ( PIX *pixs, l_int32 thresh, l_int32 adaptive, l_int32 useboth, l_int32 check_columns, PIX **ppixd, L_DEWARPA **pdewa, l_int32 debug );
l_ok dewarpSinglePageInit ( PIX *pixs, l_int32 thresh, l_int32 adaptive, l_int32 useboth, l_int32 check_columns, PIX **ppixb, L_DEWARPA **pdewa );
l_ok dewarpSinglePageRun ( PIX *pixs, PIX *pixb, L_DEWARPA *dewa, PIX **ppixd, l_int32 debug );
l_ok dewarpaListPages ( L_DEWARPA *dewa );
l_ok dewarpaSetValidModels ( L_DEWARPA *dewa, l_int32 notests, l_int32 debug );
l_ok dewarpaInsertRefModels ( L_DEWARPA *dewa, l_int32 notests, l_int32 debug );
l_ok dewarpaStripRefModels ( L_DEWARPA *dewa );
l_ok dewarpaRestoreModels ( L_DEWARPA *dewa );
l_ok dewarpaInfo ( FILE *fp, L_DEWARPA *dewa );
l_ok dewarpaModelStats ( L_DEWARPA *dewa, l_int32 *pnnone, l_int32 *pnvsuccess, l_int32 *pnvvalid, l_int32 *pnhsuccess, l_int32 *pnhvalid, l_int32 *pnref );
l_ok dewarpaShowArrays ( L_DEWARPA *dewa, l_float32 scalefact, l_int32 first, l_int32 last );
l_ok dewarpDebug ( L_DEWARP *dew, const char *subdirs, l_int32 index );
l_ok dewarpShowResults ( L_DEWARPA *dewa, SARRAY *sa, BOXA *boxa, l_int32 firstpage, l_int32 lastpage, const char *pdfout );
L_DNA * l_dnaCreate ( l_int32 n );
L_DNA * l_dnaCreateFromIArray ( l_int32 *iarray, l_int32 size );
L_DNA * l_dnaCreateFromDArray ( l_float64 *darray, l_int32 size, l_int32 copyflag );
L_DNA * l_dnaMakeSequence ( l_float64 startval, l_float64 increment, l_int32 size );
void l_dnaDestroy ( L_DNA **pda );
L_DNA * l_dnaCopy ( L_DNA *da );
L_DNA * l_dnaClone ( L_DNA *da );
l_ok l_dnaEmpty ( L_DNA *da );
l_ok l_dnaAddNumber ( L_DNA *da, l_float64 val );
l_ok l_dnaInsertNumber ( L_DNA *da, l_int32 index, l_float64 val );
l_ok l_dnaRemoveNumber ( L_DNA *da, l_int32 index );
l_ok l_dnaReplaceNumber ( L_DNA *da, l_int32 index, l_float64 val );
l_int32 l_dnaGetCount ( L_DNA *da );
l_ok l_dnaSetCount ( L_DNA *da, l_int32 newcount );
l_ok l_dnaGetDValue ( L_DNA *da, l_int32 index, l_float64 *pval );
l_ok l_dnaGetIValue ( L_DNA *da, l_int32 index, l_int32 *pival );
l_ok l_dnaSetValue ( L_DNA *da, l_int32 index, l_float64 val );
l_ok l_dnaShiftValue ( L_DNA *da, l_int32 index, l_float64 diff );
l_int32 * l_dnaGetIArray ( L_DNA *da );
l_float64 * l_dnaGetDArray ( L_DNA *da, l_int32 copyflag );
l_int32 l_dnaGetRefcount ( L_DNA *da );
l_ok l_dnaChangeRefcount ( L_DNA *da, l_int32 delta );
l_ok l_dnaGetParameters ( L_DNA *da, l_float64 *pstartx, l_float64 *pdelx );
l_ok l_dnaSetParameters ( L_DNA *da, l_float64 startx, l_float64 delx );
l_ok l_dnaCopyParameters ( L_DNA *dad, L_DNA *das );
L_DNA * l_dnaRead ( const char *filename );
L_DNA * l_dnaReadStream ( FILE *fp );
l_ok l_dnaWrite ( const char *filename, L_DNA *da );
l_ok l_dnaWriteStream ( FILE *fp, L_DNA *da );
L_DNAA * l_dnaaCreate ( l_int32 n );
L_DNAA * l_dnaaCreateFull ( l_int32 nptr, l_int32 n );
l_ok l_dnaaTruncate ( L_DNAA *daa );
void l_dnaaDestroy ( L_DNAA **pdaa );
l_ok l_dnaaAddDna ( L_DNAA *daa, L_DNA *da, l_int32 copyflag );
l_int32 l_dnaaGetCount ( L_DNAA *daa );
l_int32 l_dnaaGetDnaCount ( L_DNAA *daa, l_int32 index );
l_int32 l_dnaaGetNumberCount ( L_DNAA *daa );
L_DNA * l_dnaaGetDna ( L_DNAA *daa, l_int32 index, l_int32 accessflag );
l_ok l_dnaaReplaceDna ( L_DNAA *daa, l_int32 index, L_DNA *da );
l_ok l_dnaaGetValue ( L_DNAA *daa, l_int32 i, l_int32 j, l_float64 *pval );
l_ok l_dnaaAddNumber ( L_DNAA *daa, l_int32 index, l_float64 val );
L_DNAA * l_dnaaRead ( const char *filename );
L_DNAA * l_dnaaReadStream ( FILE *fp );
l_ok l_dnaaWrite ( const char *filename, L_DNAA *daa );
l_ok l_dnaaWriteStream ( FILE *fp, L_DNAA *daa );
l_ok l_dnaJoin ( L_DNA *dad, L_DNA *das, l_int32 istart, l_int32 iend );
L_DNA * l_dnaaFlattenToDna ( L_DNAA *daa );
NUMA * l_dnaConvertToNuma ( L_DNA *da );
L_DNA * numaConvertToDna ( NUMA *na );
L_DNA * l_dnaUnionByAset ( L_DNA *da1, L_DNA *da2 );
L_DNA * l_dnaRemoveDupsByAset ( L_DNA *das );
L_DNA * l_dnaIntersectionByAset ( L_DNA *da1, L_DNA *da2 );
L_ASET * l_asetCreateFromDna ( L_DNA *da );
L_DNA * l_dnaDiffAdjValues ( L_DNA *das );
L_DNAHASH * l_dnaHashCreate ( l_int32 nbuckets, l_int32 initsize );
void l_dnaHashDestroy ( L_DNAHASH **pdahash );
l_int32 l_dnaHashGetCount ( L_DNAHASH *dahash );
l_int32 l_dnaHashGetTotalCount ( L_DNAHASH *dahash );
L_DNA * l_dnaHashGetDna ( L_DNAHASH *dahash, l_uint64 key, l_int32 copyflag );
l_ok l_dnaHashAdd ( L_DNAHASH *dahash, l_uint64 key, l_float64 value );
L_DNAHASH * l_dnaHashCreateFromDna ( L_DNA *da );
l_ok l_dnaRemoveDupsByHash ( L_DNA *das, L_DNA **pdad, L_DNAHASH **pdahash );
l_ok l_dnaMakeHistoByHash ( L_DNA *das, L_DNAHASH **pdahash, L_DNA **pdav, L_DNA **pdac );
L_DNA * l_dnaIntersectionByHash ( L_DNA *da1, L_DNA *da2 );
l_ok l_dnaFindValByHash ( L_DNA *da, L_DNAHASH *dahash, l_float64 val, l_int32 *pindex );
PIX * pixMorphDwa_2 ( PIX *pixd, PIX *pixs, l_int32 operation, char *selname );
PIX * pixFMorphopGen_2 ( PIX *pixd, PIX *pixs, l_int32 operation, char *selname );
l_int32 fmorphopgen_low_2 ( l_uint32 *datad, l_int32 w, l_int32 h, l_int32 wpld, l_uint32 *datas, l_int32 wpls, l_int32 index );
PIX * pixSobelEdgeFilter ( PIX *pixs, l_int32 orientflag );
PIX * pixTwoSidedEdgeFilter ( PIX *pixs, l_int32 orientflag );
l_ok pixMeasureEdgeSmoothness ( PIX *pixs, l_int32 side, l_int32 minjump, l_int32 minreversal, l_float32 *pjpl, l_float32 *pjspl, l_float32 *prpl, const char *debugfile );
NUMA * pixGetEdgeProfile ( PIX *pixs, l_int32 side, const char *debugfile );
l_int32 pixGetLastOffPixelInRun ( PIX *pixs, l_int32 x, l_int32 y, l_int32 direction, l_int32 *ploc );
l_int32 pixGetLastOnPixelInRun ( PIX *pixs, l_int32 x, l_int32 y, l_int32 direction, l_int32 *ploc );
char * encodeBase64 ( l_uint8 *inarray, l_int32 insize, l_int32 *poutsize );
l_uint8 * decodeBase64 ( const char *inarray, l_int32 insize, l_int32 *poutsize );
char * encodeAscii85 ( l_uint8 *inarray, l_int32 insize, l_int32 *poutsize );
l_uint8 * decodeAscii85 ( char *inarray, l_int32 insize, l_int32 *poutsize );
char * reformatPacked64 ( char *inarray, l_int32 insize, l_int32 leadspace, l_int32 linechars, l_int32 addquotes, l_int32 *poutsize );
PIX * pixGammaTRC ( PIX *pixd, PIX *pixs, l_float32 gamma, l_int32 minval, l_int32 maxval );
PIX * pixGammaTRCMasked ( PIX *pixd, PIX *pixs, PIX *pixm, l_float32 gamma, l_int32 minval, l_int32 maxval );
PIX * pixGammaTRCWithAlpha ( PIX *pixd, PIX *pixs, l_float32 gamma, l_int32 minval, l_int32 maxval );
NUMA * numaGammaTRC ( l_float32 gamma, l_int32 minval, l_int32 maxval );
PIX * pixContrastTRC ( PIX *pixd, PIX *pixs, l_float32 factor );
PIX * pixContrastTRCMasked ( PIX *pixd, PIX *pixs, PIX *pixm, l_float32 factor );
NUMA * numaContrastTRC ( l_float32 factor );
PIX * pixEqualizeTRC ( PIX *pixd, PIX *pixs, l_float32 fract, l_int32 factor );
NUMA * numaEqualizeTRC ( PIX *pix, l_float32 fract, l_int32 factor );
l_int32 pixTRCMap ( PIX *pixs, PIX *pixm, NUMA *na );
PIX * pixUnsharpMasking ( PIX *pixs, l_int32 halfwidth, l_float32 fract );
PIX * pixUnsharpMaskingGray ( PIX *pixs, l_int32 halfwidth, l_float32 fract );
PIX * pixUnsharpMaskingFast ( PIX *pixs, l_int32 halfwidth, l_float32 fract, l_int32 direction );
PIX * pixUnsharpMaskingGrayFast ( PIX *pixs, l_int32 halfwidth, l_float32 fract, l_int32 direction );
PIX * pixUnsharpMaskingGray1D ( PIX *pixs, l_int32 halfwidth, l_float32 fract, l_int32 direction );
PIX * pixUnsharpMaskingGray2D ( PIX *pixs, l_int32 halfwidth, l_float32 fract );
PIX * pixModifyHue ( PIX *pixd, PIX *pixs, l_float32 fract );
PIX * pixModifySaturation ( PIX *pixd, PIX *pixs, l_float32 fract );
l_int32 pixMeasureSaturation ( PIX *pixs, l_int32 factor, l_float32 *psat );
PIX * pixModifyBrightness ( PIX *pixd, PIX *pixs, l_float32 fract );
PIX * pixMosaicColorShiftRGB ( PIX *pixs, l_float32 roff, l_float32 goff, l_float32 boff, l_float32 delta, l_int32 nincr );
PIX * pixColorShiftRGB ( PIX *pixs, l_float32 rfract, l_float32 gfract, l_float32 bfract );
PIX * pixDarkenGray ( PIX *pixd, PIX *pixs, l_int32 thresh, l_int32 satlimit );
PIX * pixMultConstantColor ( PIX *pixs, l_float32 rfact, l_float32 gfact, l_float32 bfact );
PIX * pixMultMatrixColor ( PIX *pixs, L_KERNEL *kel );
PIX * pixHalfEdgeByBandpass ( PIX *pixs, l_int32 sm1h, l_int32 sm1v, l_int32 sm2h, l_int32 sm2v );
l_ok fhmtautogen ( SELA *sela, l_int32 fileindex, const char *filename );
l_ok fhmtautogen1 ( SELA *sela, l_int32 fileindex, const char *filename );
l_ok fhmtautogen2 ( SELA *sela, l_int32 fileindex, const char *filename );
PIX * pixHMTDwa_1 ( PIX *pixd, PIX *pixs, const char *selname );
PIX * pixFHMTGen_1 ( PIX *pixd, PIX *pixs, const char *selname );
l_int32 fhmtgen_low_1 ( l_uint32 *datad, l_int32 w, l_int32 h, l_int32 wpld, l_uint32 *datas, l_int32 wpls, l_int32 index );
l_ok pixItalicWords ( PIX *pixs, BOXA *boxaw, PIX *pixw, BOXA **pboxa, l_int32 debugflag );
PIX * pixOrientCorrect ( PIX *pixs, l_float32 minupconf, l_float32 minratio, l_float32 *pupconf, l_float32 *pleftconf, l_int32 *protation, l_int32 debug );
l_ok pixOrientDetect ( PIX *pixs, l_float32 *pupconf, l_float32 *pleftconf, l_int32 mincount, l_int32 debug );
l_ok makeOrientDecision ( l_float32 upconf, l_float32 leftconf, l_float32 minupconf, l_float32 minratio, l_int32 *porient, l_int32 debug );
l_ok pixUpDownDetect ( PIX *pixs, l_float32 *pconf, l_int32 mincount, l_int32 debug );
l_ok pixUpDownDetectGeneral ( PIX *pixs, l_float32 *pconf, l_int32 mincount, l_int32 npixels, l_int32 debug );
l_ok pixOrientDetectDwa ( PIX *pixs, l_float32 *pupconf, l_float32 *pleftconf, l_int32 mincount, l_int32 debug );
l_ok pixUpDownDetectDwa ( PIX *pixs, l_float32 *pconf, l_int32 mincount, l_int32 debug );
l_ok pixUpDownDetectGeneralDwa ( PIX *pixs, l_float32 *pconf, l_int32 mincount, l_int32 npixels, l_int32 debug );
l_ok pixMirrorDetect ( PIX *pixs, l_float32 *pconf, l_int32 mincount, l_int32 debug );
l_ok pixMirrorDetectDwa ( PIX *pixs, l_float32 *pconf, l_int32 mincount, l_int32 debug );
PIX * pixFlipFHMTGen ( PIX *pixd, PIX *pixs, const char *selname );
l_ok fmorphautogen ( SELA *sela, l_int32 fileindex, const char *filename );
l_ok fmorphautogen1 ( SELA *sela, l_int32 fileindex, const char *filename );
l_int32 fmorphautogen2 ( SELA *sela, l_int32 fileindex, const char *filename );
PIX * pixMorphDwa_1 ( PIX *pixd, PIX *pixs, l_int32 operation, char *selname );
PIX * pixFMorphopGen_1 ( PIX *pixd, PIX *pixs, l_int32 operation, char *selname );
l_int32 fmorphopgen_low_1 ( l_uint32 *datad, l_int32 w, l_int32 h, l_int32 wpld, l_uint32 *datas, l_int32 wpls, l_int32 index );
FPIX * fpixCreate ( l_int32 width, l_int32 height );
FPIX * fpixCreateTemplate ( FPIX *fpixs );
FPIX * fpixClone ( FPIX *fpix );
FPIX * fpixCopy ( FPIX *fpixd, FPIX *fpixs );
l_ok fpixResizeImageData ( FPIX *fpixd, FPIX *fpixs );
void fpixDestroy ( FPIX **pfpix );
l_ok fpixGetDimensions ( FPIX *fpix, l_int32 *pw, l_int32 *ph );
l_ok fpixSetDimensions ( FPIX *fpix, l_int32 w, l_int32 h );
l_int32 fpixGetWpl ( FPIX *fpix );
l_ok fpixSetWpl ( FPIX *fpix, l_int32 wpl );
l_int32 fpixGetRefcount ( FPIX *fpix );
l_ok fpixChangeRefcount ( FPIX *fpix, l_int32 delta );
l_ok fpixGetResolution ( FPIX *fpix, l_int32 *pxres, l_int32 *pyres );
l_ok fpixSetResolution ( FPIX *fpix, l_int32 xres, l_int32 yres );
l_ok fpixCopyResolution ( FPIX *fpixd, FPIX *fpixs );
l_float32 * fpixGetData ( FPIX *fpix );
l_ok fpixSetData ( FPIX *fpix, l_float32 *data );
l_ok fpixGetPixel ( FPIX *fpix, l_int32 x, l_int32 y, l_float32 *pval );
l_ok fpixSetPixel ( FPIX *fpix, l_int32 x, l_int32 y, l_float32 val );
FPIXA * fpixaCreate ( l_int32 n );
FPIXA * fpixaCopy ( FPIXA *fpixa, l_int32 copyflag );
void fpixaDestroy ( FPIXA **pfpixa );
l_ok fpixaAddFPix ( FPIXA *fpixa, FPIX *fpix, l_int32 copyflag );
l_int32 fpixaGetCount ( FPIXA *fpixa );
l_ok fpixaChangeRefcount ( FPIXA *fpixa, l_int32 delta );
FPIX * fpixaGetFPix ( FPIXA *fpixa, l_int32 index, l_int32 accesstype );
l_ok fpixaGetFPixDimensions ( FPIXA *fpixa, l_int32 index, l_int32 *pw, l_int32 *ph );
l_float32 * fpixaGetData ( FPIXA *fpixa, l_int32 index );
l_ok fpixaGetPixel ( FPIXA *fpixa, l_int32 index, l_int32 x, l_int32 y, l_float32 *pval );
l_ok fpixaSetPixel ( FPIXA *fpixa, l_int32 index, l_int32 x, l_int32 y, l_float32 val );
DPIX * dpixCreate ( l_int32 width, l_int32 height );
DPIX * dpixCreateTemplate ( DPIX *dpixs );
DPIX * dpixClone ( DPIX *dpix );
DPIX * dpixCopy ( DPIX *dpixd, DPIX *dpixs );
l_ok dpixResizeImageData ( DPIX *dpixd, DPIX *dpixs );
void dpixDestroy ( DPIX **pdpix );
l_ok dpixGetDimensions ( DPIX *dpix, l_int32 *pw, l_int32 *ph );
l_ok dpixSetDimensions ( DPIX *dpix, l_int32 w, l_int32 h );
l_int32 dpixGetWpl ( DPIX *dpix );
l_ok dpixSetWpl ( DPIX *dpix, l_int32 wpl );
l_int32 dpixGetRefcount ( DPIX *dpix );
l_ok dpixChangeRefcount ( DPIX *dpix, l_int32 delta );
l_ok dpixGetResolution ( DPIX *dpix, l_int32 *pxres, l_int32 *pyres );
l_ok dpixSetResolution ( DPIX *dpix, l_int32 xres, l_int32 yres );
l_ok dpixCopyResolution ( DPIX *dpixd, DPIX *dpixs );
l_float64 * dpixGetData ( DPIX *dpix );
l_ok dpixSetData ( DPIX *dpix, l_float64 *data );
l_ok dpixGetPixel ( DPIX *dpix, l_int32 x, l_int32 y, l_float64 *pval );
l_ok dpixSetPixel ( DPIX *dpix, l_int32 x, l_int32 y, l_float64 val );
FPIX * fpixRead ( const char *filename );
FPIX * fpixReadStream ( FILE *fp );
FPIX * fpixReadMem ( const l_uint8 *data, size_t size );
l_ok fpixWrite ( const char *filename, FPIX *fpix );
l_ok fpixWriteStream ( FILE *fp, FPIX *fpix );
l_ok fpixWriteMem ( l_uint8 **pdata, size_t *psize, FPIX *fpix );
FPIX * fpixEndianByteSwap ( FPIX *fpixd, FPIX *fpixs );
DPIX * dpixRead ( const char *filename );
DPIX * dpixReadStream ( FILE *fp );
DPIX * dpixReadMem ( const l_uint8 *data, size_t size );
l_ok dpixWrite ( const char *filename, DPIX *dpix );
l_ok dpixWriteStream ( FILE *fp, DPIX *dpix );
l_ok dpixWriteMem ( l_uint8 **pdata, size_t *psize, DPIX *dpix );
DPIX * dpixEndianByteSwap ( DPIX *dpixd, DPIX *dpixs );
l_ok fpixPrintStream ( FILE *fp, FPIX *fpix, l_int32 factor );
FPIX * pixConvertToFPix ( PIX *pixs, l_int32 ncomps );
DPIX * pixConvertToDPix ( PIX *pixs, l_int32 ncomps );
PIX * fpixConvertToPix ( FPIX *fpixs, l_int32 outdepth, l_int32 negvals, l_int32 errorflag );
PIX * fpixDisplayMaxDynamicRange ( FPIX *fpixs );
DPIX * fpixConvertToDPix ( FPIX *fpix );
PIX * dpixConvertToPix ( DPIX *dpixs, l_int32 outdepth, l_int32 negvals, l_int32 errorflag );
FPIX * dpixConvertToFPix ( DPIX *dpix );
l_ok fpixGetMin ( FPIX *fpix, l_float32 *pminval, l_int32 *pxminloc, l_int32 *pyminloc );
l_ok fpixGetMax ( FPIX *fpix, l_float32 *pmaxval, l_int32 *pxmaxloc, l_int32 *pymaxloc );
l_ok dpixGetMin ( DPIX *dpix, l_float64 *pminval, l_int32 *pxminloc, l_int32 *pyminloc );
l_ok dpixGetMax ( DPIX *dpix, l_float64 *pmaxval, l_int32 *pxmaxloc, l_int32 *pymaxloc );
FPIX * fpixScaleByInteger ( FPIX *fpixs, l_int32 factor );
DPIX * dpixScaleByInteger ( DPIX *dpixs, l_int32 factor );
FPIX * fpixLinearCombination ( FPIX *fpixd, FPIX *fpixs1, FPIX *fpixs2, l_float32 a, l_float32 b );
l_ok fpixAddMultConstant ( FPIX *fpix, l_float32 addc, l_float32 multc );
DPIX * dpixLinearCombination ( DPIX *dpixd, DPIX *dpixs1, DPIX *dpixs2, l_float32 a, l_float32 b );
l_ok dpixAddMultConstant ( DPIX *dpix, l_float64 addc, l_float64 multc );
l_ok fpixSetAllArbitrary ( FPIX *fpix, l_float32 inval );
l_ok dpixSetAllArbitrary ( DPIX *dpix, l_float64 inval );
FPIX * fpixAddBorder ( FPIX *fpixs, l_int32 left, l_int32 right, l_int32 top, l_int32 bot );
FPIX * fpixRemoveBorder ( FPIX *fpixs, l_int32 left, l_int32 right, l_int32 top, l_int32 bot );
FPIX * fpixAddMirroredBorder ( FPIX *fpixs, l_int32 left, l_int32 right, l_int32 top, l_int32 bot );
FPIX * fpixAddContinuedBorder ( FPIX *fpixs, l_int32 left, l_int32 right, l_int32 top, l_int32 bot );
FPIX * fpixAddSlopeBorder ( FPIX *fpixs, l_int32 left, l_int32 right, l_int32 top, l_int32 bot );
l_ok fpixRasterop ( FPIX *fpixd, l_int32 dx, l_int32 dy, l_int32 dw, l_int32 dh, FPIX *fpixs, l_int32 sx, l_int32 sy );
FPIX * fpixRotateOrth ( FPIX *fpixs, l_int32 quads );
FPIX * fpixRotate180 ( FPIX *fpixd, FPIX *fpixs );
FPIX * fpixRotate90 ( FPIX *fpixs, l_int32 direction );
FPIX * fpixFlipLR ( FPIX *fpixd, FPIX *fpixs );
FPIX * fpixFlipTB ( FPIX *fpixd, FPIX *fpixs );
FPIX * fpixAffinePta ( FPIX *fpixs, PTA *ptad, PTA *ptas, l_int32 border, l_float32 inval );
FPIX * fpixAffine ( FPIX *fpixs, l_float32 *vc, l_float32 inval );
FPIX * fpixProjectivePta ( FPIX *fpixs, PTA *ptad, PTA *ptas, l_int32 border, l_float32 inval );
FPIX * fpixProjective ( FPIX *fpixs, l_float32 *vc, l_float32 inval );
l_ok linearInterpolatePixelFloat ( l_float32 *datas, l_int32 w, l_int32 h, l_float32 x, l_float32 y, l_float32 inval, l_float32 *pval );
PIX * fpixThresholdToPix ( FPIX *fpix, l_float32 thresh );
FPIX * pixComponentFunction ( PIX *pix, l_float32 rnum, l_float32 gnum, l_float32 bnum, l_float32 rdenom, l_float32 gdenom, l_float32 bdenom );
PIX * pixReadStreamGif ( FILE *fp );
PIX * pixReadMemGif ( const l_uint8 *cdata, size_t size );
l_ok pixWriteStreamGif ( FILE *fp, PIX *pix );
l_ok pixWriteMemGif ( l_uint8 **pdata, size_t *psize, PIX *pix );
GPLOT * gplotCreate ( const char *rootname, l_int32 outformat, const char *title, const char *xlabel, const char *ylabel );
void gplotDestroy ( GPLOT **pgplot );
l_ok gplotAddPlot ( GPLOT *gplot, NUMA *nax, NUMA *nay, l_int32 plotstyle, const char *plottitle );
l_ok gplotSetScaling ( GPLOT *gplot, l_int32 scaling );
l_ok gplotMakeOutput ( GPLOT *gplot );
l_ok gplotGenCommandFile ( GPLOT *gplot );
l_ok gplotGenDataFiles ( GPLOT *gplot );
l_ok gplotSimple1 ( NUMA *na, l_int32 outformat, const char *outroot, const char *title );
l_ok gplotSimple2 ( NUMA *na1, NUMA *na2, l_int32 outformat, const char *outroot, const char *title );
l_ok gplotSimpleN ( NUMAA *naa, l_int32 outformat, const char *outroot, const char *title );
l_ok gplotSimpleXY1 ( NUMA *nax, NUMA *nay, l_int32 plotstyle, l_int32 outformat, const char *outroot, const char *title );
l_ok gplotSimpleXY2 ( NUMA *nax, NUMA *nay1, NUMA *nay2, l_int32 plotstyle, l_int32 outformat, const char *outroot, const char *title );
l_ok gplotSimpleXYN ( NUMA *nax, NUMAA *naay, l_int32 plotstyle, l_int32 outformat, const char *outroot, const char *title );
GPLOT * gplotRead ( const char *filename );
l_ok gplotWrite ( const char *filename, GPLOT *gplot );
PTA * generatePtaLine ( l_int32 x1, l_int32 y1, l_int32 x2, l_int32 y2 );
PTA * generatePtaWideLine ( l_int32 x1, l_int32 y1, l_int32 x2, l_int32 y2, l_int32 width );
PTA * generatePtaBox ( BOX *box, l_int32 width );
PTA * generatePtaBoxa ( BOXA *boxa, l_int32 width, l_int32 removedups );
PTA * generatePtaHashBox ( BOX *box, l_int32 spacing, l_int32 width, l_int32 orient, l_int32 outline );
PTA * generatePtaHashBoxa ( BOXA *boxa, l_int32 spacing, l_int32 width, l_int32 orient, l_int32 outline, l_int32 removedups );
PTAA * generatePtaaBoxa ( BOXA *boxa );
PTAA * generatePtaaHashBoxa ( BOXA *boxa, l_int32 spacing, l_int32 width, l_int32 orient, l_int32 outline );
PTA * generatePtaPolyline ( PTA *ptas, l_int32 width, l_int32 closeflag, l_int32 removedups );
PTA * generatePtaGrid ( l_int32 w, l_int32 h, l_int32 nx, l_int32 ny, l_int32 width );
PTA * convertPtaLineTo4cc ( PTA *ptas );
PTA * generatePtaFilledCircle ( l_int32 radius );
PTA * generatePtaFilledSquare ( l_int32 side );
PTA * generatePtaLineFromPt ( l_int32 x, l_int32 y, l_float64 length, l_float64 radang );
l_ok locatePtRadially ( l_int32 xr, l_int32 yr, l_float64 dist, l_float64 radang, l_float64 *px, l_float64 *py );
l_ok pixRenderPlotFromNuma ( PIX **ppix, NUMA *na, l_int32 plotloc, l_int32 linewidth, l_int32 max, l_uint32 color );
PTA * makePlotPtaFromNuma ( NUMA *na, l_int32 size, l_int32 plotloc, l_int32 linewidth, l_int32 max );
l_ok pixRenderPlotFromNumaGen ( PIX **ppix, NUMA *na, l_int32 orient, l_int32 linewidth, l_int32 refpos, l_int32 max, l_int32 drawref, l_uint32 color );
PTA * makePlotPtaFromNumaGen ( NUMA *na, l_int32 orient, l_int32 linewidth, l_int32 refpos, l_int32 max, l_int32 drawref );
l_ok pixRenderPta ( PIX *pix, PTA *pta, l_int32 op );
l_ok pixRenderPtaArb ( PIX *pix, PTA *pta, l_uint8 rval, l_uint8 gval, l_uint8 bval );
l_ok pixRenderPtaBlend ( PIX *pix, PTA *pta, l_uint8 rval, l_uint8 gval, l_uint8 bval, l_float32 fract );
l_ok pixRenderLine ( PIX *pix, l_int32 x1, l_int32 y1, l_int32 x2, l_int32 y2, l_int32 width, l_int32 op );
l_ok pixRenderLineArb ( PIX *pix, l_int32 x1, l_int32 y1, l_int32 x2, l_int32 y2, l_int32 width, l_uint8 rval, l_uint8 gval, l_uint8 bval );
l_ok pixRenderLineBlend ( PIX *pix, l_int32 x1, l_int32 y1, l_int32 x2, l_int32 y2, l_int32 width, l_uint8 rval, l_uint8 gval, l_uint8 bval, l_float32 fract );
l_ok pixRenderBox ( PIX *pix, BOX *box, l_int32 width, l_int32 op );
l_ok pixRenderBoxArb ( PIX *pix, BOX *box, l_int32 width, l_uint8 rval, l_uint8 gval, l_uint8 bval );
l_ok pixRenderBoxBlend ( PIX *pix, BOX *box, l_int32 width, l_uint8 rval, l_uint8 gval, l_uint8 bval, l_float32 fract );
l_ok pixRenderBoxa ( PIX *pix, BOXA *boxa, l_int32 width, l_int32 op );
l_ok pixRenderBoxaArb ( PIX *pix, BOXA *boxa, l_int32 width, l_uint8 rval, l_uint8 gval, l_uint8 bval );
l_ok pixRenderBoxaBlend ( PIX *pix, BOXA *boxa, l_int32 width, l_uint8 rval, l_uint8 gval, l_uint8 bval, l_float32 fract, l_int32 removedups );
l_ok pixRenderHashBox ( PIX *pix, BOX *box, l_int32 spacing, l_int32 width, l_int32 orient, l_int32 outline, l_int32 op );
l_ok pixRenderHashBoxArb ( PIX *pix, BOX *box, l_int32 spacing, l_int32 width, l_int32 orient, l_int32 outline, l_int32 rval, l_int32 gval, l_int32 bval );
l_ok pixRenderHashBoxBlend ( PIX *pix, BOX *box, l_int32 spacing, l_int32 width, l_int32 orient, l_int32 outline, l_int32 rval, l_int32 gval, l_int32 bval, l_float32 fract );
l_ok pixRenderHashMaskArb ( PIX *pix, PIX *pixm, l_int32 x, l_int32 y, l_int32 spacing, l_int32 width, l_int32 orient, l_int32 outline, l_int32 rval, l_int32 gval, l_int32 bval );
l_ok pixRenderHashBoxa ( PIX *pix, BOXA *boxa, l_int32 spacing, l_int32 width, l_int32 orient, l_int32 outline, l_int32 op );
l_ok pixRenderHashBoxaArb ( PIX *pix, BOXA *boxa, l_int32 spacing, l_int32 width, l_int32 orient, l_int32 outline, l_int32 rval, l_int32 gval, l_int32 bval );
l_ok pixRenderHashBoxaBlend ( PIX *pix, BOXA *boxa, l_int32 spacing, l_int32 width, l_int32 orient, l_int32 outline, l_int32 rval, l_int32 gval, l_int32 bval, l_float32 fract );
l_ok pixRenderPolyline ( PIX *pix, PTA *ptas, l_int32 width, l_int32 op, l_int32 closeflag );
l_ok pixRenderPolylineArb ( PIX *pix, PTA *ptas, l_int32 width, l_uint8 rval, l_uint8 gval, l_uint8 bval, l_int32 closeflag );
l_ok pixRenderPolylineBlend ( PIX *pix, PTA *ptas, l_int32 width, l_uint8 rval, l_uint8 gval, l_uint8 bval, l_float32 fract, l_int32 closeflag, l_int32 removedups );
l_ok pixRenderGridArb ( PIX *pix, l_int32 nx, l_int32 ny, l_int32 width, l_uint8 rval, l_uint8 gval, l_uint8 bval );
PIX * pixRenderRandomCmapPtaa ( PIX *pix, PTAA *ptaa, l_int32 polyflag, l_int32 width, l_int32 closeflag );
PIX * pixRenderPolygon ( PTA *ptas, l_int32 width, l_int32 *pxmin, l_int32 *pymin );
PIX * pixFillPolygon ( PIX *pixs, PTA *pta, l_int32 xmin, l_int32 ymin );
PIX * pixRenderContours ( PIX *pixs, l_int32 startval, l_int32 incr, l_int32 outdepth );
PIX * fpixAutoRenderContours ( FPIX *fpix, l_int32 ncontours );
PIX * fpixRenderContours ( FPIX *fpixs, l_float32 incr, l_float32 proxim );
PTA * pixGeneratePtaBoundary ( PIX *pixs, l_int32 width );
PIX * pixErodeGray ( PIX *pixs, l_int32 hsize, l_int32 vsize );
PIX * pixDilateGray ( PIX *pixs, l_int32 hsize, l_int32 vsize );
PIX * pixOpenGray ( PIX *pixs, l_int32 hsize, l_int32 vsize );
PIX * pixCloseGray ( PIX *pixs, l_int32 hsize, l_int32 vsize );
PIX * pixErodeGray3 ( PIX *pixs, l_int32 hsize, l_int32 vsize );
PIX * pixDilateGray3 ( PIX *pixs, l_int32 hsize, l_int32 vsize );
PIX * pixOpenGray3 ( PIX *pixs, l_int32 hsize, l_int32 vsize );
PIX * pixCloseGray3 ( PIX *pixs, l_int32 hsize, l_int32 vsize );
PIX * pixDitherToBinary ( PIX *pixs );
PIX * pixDitherToBinarySpec ( PIX *pixs, l_int32 lowerclip, l_int32 upperclip );
void ditherToBinaryLineLow ( l_uint32 *lined, l_int32 w, l_uint32 *bufs1, l_uint32 *bufs2, l_int32 lowerclip, l_int32 upperclip, l_int32 lastlineflag );
PIX * pixThresholdToBinary ( PIX *pixs, l_int32 thresh );
void thresholdToBinaryLineLow ( l_uint32 *lined, l_int32 w, l_uint32 *lines, l_int32 d, l_int32 thresh );
PIX * pixVarThresholdToBinary ( PIX *pixs, PIX *pixg );
PIX * pixAdaptThresholdToBinary ( PIX *pixs, PIX *pixm, l_float32 gamma );
PIX * pixAdaptThresholdToBinaryGen ( PIX *pixs, PIX *pixm, l_float32 gamma, l_int32 blackval, l_int32 whiteval, l_int32 thresh );
PIX * pixGenerateMaskByValue ( PIX *pixs, l_int32 val, l_int32 usecmap );
PIX * pixGenerateMaskByBand ( PIX *pixs, l_int32 lower, l_int32 upper, l_int32 inband, l_int32 usecmap );
PIX * pixDitherTo2bpp ( PIX *pixs, l_int32 cmapflag );
PIX * pixDitherTo2bppSpec ( PIX *pixs, l_int32 lowerclip, l_int32 upperclip, l_int32 cmapflag );
PIX * pixThresholdTo2bpp ( PIX *pixs, l_int32 nlevels, l_int32 cmapflag );
PIX * pixThresholdTo4bpp ( PIX *pixs, l_int32 nlevels, l_int32 cmapflag );
PIX * pixThresholdOn8bpp ( PIX *pixs, l_int32 nlevels, l_int32 cmapflag );
PIX * pixThresholdGrayArb ( PIX *pixs, const char *edgevals, l_int32 outdepth, l_int32 use_average, l_int32 setblack, l_int32 setwhite );
l_int32 * makeGrayQuantIndexTable ( l_int32 nlevels );
l_ok makeGrayQuantTableArb ( NUMA *na, l_int32 outdepth, l_int32 **ptab, PIXCMAP **pcmap );
PIX * pixGenerateMaskByBand32 ( PIX *pixs, l_uint32 refval, l_int32 delm, l_int32 delp, l_float32 fractm, l_float32 fractp );
PIX * pixGenerateMaskByDiscr32 ( PIX *pixs, l_uint32 refval1, l_uint32 refval2, l_int32 distflag );
PIX * pixGrayQuantFromHisto ( PIX *pixd, PIX *pixs, PIX *pixm, l_float32 minfract, l_int32 maxsize );
PIX * pixGrayQuantFromCmap ( PIX *pixs, PIXCMAP *cmap, l_int32 mindepth );
L_HEAP * lheapCreate ( l_int32 nalloc, l_int32 direction );
void lheapDestroy ( L_HEAP **plh, l_int32 freeflag );
l_ok lheapAdd ( L_HEAP *lh, void *item );
void * lheapRemove ( L_HEAP *lh );
l_int32 lheapGetCount ( L_HEAP *lh );
l_ok lheapSwapUp ( L_HEAP *lh, l_int32 index );
l_ok lheapSwapDown ( L_HEAP *lh );
l_ok lheapSort ( L_HEAP *lh );
l_ok lheapSortStrictOrder ( L_HEAP *lh );
l_ok lheapPrint ( FILE *fp, L_HEAP *lh );
JBCLASSER * jbRankHausInit ( l_int32 components, l_int32 maxwidth, l_int32 maxheight, l_int32 size, l_float32 rank );
JBCLASSER * jbCorrelationInit ( l_int32 components, l_int32 maxwidth, l_int32 maxheight, l_float32 thresh, l_float32 weightfactor );
JBCLASSER * jbCorrelationInitWithoutComponents ( l_int32 components, l_int32 maxwidth, l_int32 maxheight, l_float32 thresh, l_float32 weightfactor );
l_ok jbAddPages ( JBCLASSER *classer, SARRAY *safiles );
l_ok jbAddPage ( JBCLASSER *classer, PIX *pixs );
l_ok jbAddPageComponents ( JBCLASSER *classer, PIX *pixs, BOXA *boxas, PIXA *pixas );
l_ok jbClassifyRankHaus ( JBCLASSER *classer, BOXA *boxa, PIXA *pixas );
l_int32 pixHaustest ( PIX *pix1, PIX *pix2, PIX *pix3, PIX *pix4, l_float32 delx, l_float32 dely, l_int32 maxdiffw, l_int32 maxdiffh );
l_int32 pixRankHaustest ( PIX *pix1, PIX *pix2, PIX *pix3, PIX *pix4, l_float32 delx, l_float32 dely, l_int32 maxdiffw, l_int32 maxdiffh, l_int32 area1, l_int32 area3, l_float32 rank, l_int32 *tab8 );
l_ok jbClassifyCorrelation ( JBCLASSER *classer, BOXA *boxa, PIXA *pixas );
l_ok jbGetComponents ( PIX *pixs, l_int32 components, l_int32 maxwidth, l_int32 maxheight, BOXA **pboxad, PIXA **ppixad );
l_ok pixWordMaskByDilation ( PIX *pixs, PIX **ppixm, l_int32 *psize, PIXA *pixadb );
l_ok pixWordBoxesByDilation ( PIX *pixs, l_int32 minwidth, l_int32 minheight, l_int32 maxwidth, l_int32 maxheight, BOXA **pboxa, l_int32 *psize, PIXA *pixadb );
PIXA * jbAccumulateComposites ( PIXAA *pixaa, NUMA **pna, PTA **pptat );
PIXA * jbTemplatesFromComposites ( PIXA *pixac, NUMA *na );
JBCLASSER * jbClasserCreate ( l_int32 method, l_int32 components );
void jbClasserDestroy ( JBCLASSER **pclasser );
JBDATA * jbDataSave ( JBCLASSER *classer );
void jbDataDestroy ( JBDATA **pdata );
l_ok jbDataWrite ( const char *rootout, JBDATA *jbdata );
JBDATA * jbDataRead ( const char *rootname );
PIXA * jbDataRender ( JBDATA *data, l_int32 debugflag );
l_ok jbGetULCorners ( JBCLASSER *classer, PIX *pixs, BOXA *boxa );
l_ok jbGetLLCorners ( JBCLASSER *classer );
l_ok readHeaderJp2k ( const char *filename, l_int32 *pw, l_int32 *ph, l_int32 *pbps, l_int32 *pspp );
l_ok freadHeaderJp2k ( FILE *fp, l_int32 *pw, l_int32 *ph, l_int32 *pbps, l_int32 *pspp );
l_ok readHeaderMemJp2k ( const l_uint8 *data, size_t size, l_int32 *pw, l_int32 *ph, l_int32 *pbps, l_int32 *pspp );
l_int32 fgetJp2kResolution ( FILE *fp, l_int32 *pxres, l_int32 *pyres );
PIX * pixReadJp2k ( const char *filename, l_uint32 reduction, BOX *box, l_int32 hint, l_int32 debug );
PIX * pixReadStreamJp2k ( FILE *fp, l_uint32 reduction, BOX *box, l_int32 hint, l_int32 debug );
l_ok pixWriteJp2k ( const char *filename, PIX *pix, l_int32 quality, l_int32 nlevels, l_int32 hint, l_int32 debug );
l_ok pixWriteStreamJp2k ( FILE *fp, PIX *pix, l_int32 quality, l_int32 nlevels, l_int32 hint, l_int32 debug );
PIX * pixReadMemJp2k ( const l_uint8 *data, size_t size, l_uint32 reduction, BOX *box, l_int32 hint, l_int32 debug );
l_ok pixWriteMemJp2k ( l_uint8 **pdata, size_t *psize, PIX *pix, l_int32 quality, l_int32 nlevels, l_int32 hint, l_int32 debug );
PIX * pixReadJpeg ( const char *filename, l_int32 cmapflag, l_int32 reduction, l_int32 *pnwarn, l_int32 hint );
PIX * pixReadStreamJpeg ( FILE *fp, l_int32 cmapflag, l_int32 reduction, l_int32 *pnwarn, l_int32 hint );
l_ok readHeaderJpeg ( const char *filename, l_int32 *pw, l_int32 *ph, l_int32 *pspp, l_int32 *pycck, l_int32 *pcmyk );
l_ok freadHeaderJpeg ( FILE *fp, l_int32 *pw, l_int32 *ph, l_int32 *pspp, l_int32 *pycck, l_int32 *pcmyk );
l_int32 fgetJpegResolution ( FILE *fp, l_int32 *pxres, l_int32 *pyres );
l_int32 fgetJpegComment ( FILE *fp, l_uint8 **pcomment );
l_ok pixWriteJpeg ( const char *filename, PIX *pix, l_int32 quality, l_int32 progressive );
l_ok pixWriteStreamJpeg ( FILE *fp, PIX *pixs, l_int32 quality, l_int32 progressive );
PIX * pixReadMemJpeg ( const l_uint8 *data, size_t size, l_int32 cmflag, l_int32 reduction, l_int32 *pnwarn, l_int32 hint );
l_ok readHeaderMemJpeg ( const l_uint8 *data, size_t size, l_int32 *pw, l_int32 *ph, l_int32 *pspp, l_int32 *pycck, l_int32 *pcmyk );
l_ok readResolutionMemJpeg ( const l_uint8 *data, size_t size, l_int32 *pxres, l_int32 *pyres );
l_ok pixWriteMemJpeg ( l_uint8 **pdata, size_t *psize, PIX *pix, l_int32 quality, l_int32 progressive );
l_ok pixSetChromaSampling ( PIX *pix, l_int32 sampling );
L_KERNEL * kernelCreate ( l_int32 height, l_int32 width );
void kernelDestroy ( L_KERNEL **pkel );
L_KERNEL * kernelCopy ( L_KERNEL *kels );
l_ok kernelGetElement ( L_KERNEL *kel, l_int32 row, l_int32 col, l_float32 *pval );
l_ok kernelSetElement ( L_KERNEL *kel, l_int32 row, l_int32 col, l_float32 val );
l_ok kernelGetParameters ( L_KERNEL *kel, l_int32 *psy, l_int32 *psx, l_int32 *pcy, l_int32 *pcx );
l_ok kernelSetOrigin ( L_KERNEL *kel, l_int32 cy, l_int32 cx );
l_ok kernelGetSum ( L_KERNEL *kel, l_float32 *psum );
l_ok kernelGetMinMax ( L_KERNEL *kel, l_float32 *pmin, l_float32 *pmax );
L_KERNEL * kernelNormalize ( L_KERNEL *kels, l_float32 normsum );
L_KERNEL * kernelInvert ( L_KERNEL *kels );
l_float32 ** create2dFloatArray ( l_int32 sy, l_int32 sx );
L_KERNEL * kernelRead ( const char *fname );
L_KERNEL * kernelReadStream ( FILE *fp );
l_ok kernelWrite ( const char *fname, L_KERNEL *kel );
l_ok kernelWriteStream ( FILE *fp, L_KERNEL *kel );
L_KERNEL * kernelCreateFromString ( l_int32 h, l_int32 w, l_int32 cy, l_int32 cx, const char *kdata );
L_KERNEL * kernelCreateFromFile ( const char *filename );
L_KERNEL * kernelCreateFromPix ( PIX *pix, l_int32 cy, l_int32 cx );
PIX * kernelDisplayInPix ( L_KERNEL *kel, l_int32 size, l_int32 gthick );
NUMA * parseStringForNumbers ( const char *str, const char *seps );
L_KERNEL * makeFlatKernel ( l_int32 height, l_int32 width, l_int32 cy, l_int32 cx );
L_KERNEL * makeGaussianKernel ( l_int32 halfheight, l_int32 halfwidth, l_float32 stdev, l_float32 max );
l_ok makeGaussianKernelSep ( l_int32 halfheight, l_int32 halfwidth, l_float32 stdev, l_float32 max, L_KERNEL **pkelx, L_KERNEL **pkely );
L_KERNEL * makeDoGKernel ( l_int32 halfheight, l_int32 halfwidth, l_float32 stdev, l_float32 ratio );
char * getImagelibVersions (  );
void listDestroy ( DLLIST **phead );
l_ok listAddToHead ( DLLIST **phead, void *data );
l_ok listAddToTail ( DLLIST **phead, DLLIST **ptail, void *data );
l_ok listInsertBefore ( DLLIST **phead, DLLIST *elem, void *data );
l_ok listInsertAfter ( DLLIST **phead, DLLIST *elem, void *data );
void * listRemoveElement ( DLLIST **phead, DLLIST *elem );
void * listRemoveFromHead ( DLLIST **phead );
void * listRemoveFromTail ( DLLIST **phead, DLLIST **ptail );
DLLIST * listFindElement ( DLLIST *head, void *data );
DLLIST * listFindTail ( DLLIST *head );
l_int32 listGetCount ( DLLIST *head );
l_ok listReverse ( DLLIST **phead );
l_ok listJoin ( DLLIST **phead1, DLLIST **phead2 );
L_AMAP * l_amapCreate ( l_int32 keytype );
RB_TYPE * l_amapFind ( L_AMAP *m, RB_TYPE key );
void l_amapInsert ( L_AMAP *m, RB_TYPE key, RB_TYPE value );
void l_amapDelete ( L_AMAP *m, RB_TYPE key );
void l_amapDestroy ( L_AMAP **pm );
L_AMAP_NODE * l_amapGetFirst ( L_AMAP *m );
L_AMAP_NODE * l_amapGetNext ( L_AMAP_NODE *n );
L_AMAP_NODE * l_amapGetLast ( L_AMAP *m );
L_AMAP_NODE * l_amapGetPrev ( L_AMAP_NODE *n );
l_int32 l_amapSize ( L_AMAP *m );
L_ASET * l_asetCreate ( l_int32 keytype );
RB_TYPE * l_asetFind ( L_ASET *s, RB_TYPE key );
void l_asetInsert ( L_ASET *s, RB_TYPE key );
void l_asetDelete ( L_ASET *s, RB_TYPE key );
void l_asetDestroy ( L_ASET **ps );
L_ASET_NODE * l_asetGetFirst ( L_ASET *s );
L_ASET_NODE * l_asetGetNext ( L_ASET_NODE *n );
L_ASET_NODE * l_asetGetLast ( L_ASET *s );
L_ASET_NODE * l_asetGetPrev ( L_ASET_NODE *n );
l_int32 l_asetSize ( L_ASET *s );
PIX * generateBinaryMaze ( l_int32 w, l_int32 h, l_int32 xi, l_int32 yi, l_float32 wallps, l_float32 ranis );
PTA * pixSearchBinaryMaze ( PIX *pixs, l_int32 xi, l_int32 yi, l_int32 xf, l_int32 yf, PIX **ppixd );
PTA * pixSearchGrayMaze ( PIX *pixs, l_int32 xi, l_int32 yi, l_int32 xf, l_int32 yf, PIX **ppixd );
PIX * pixDilate ( PIX *pixd, PIX *pixs, SEL *sel );
PIX * pixErode ( PIX *pixd, PIX *pixs, SEL *sel );
PIX * pixHMT ( PIX *pixd, PIX *pixs, SEL *sel );
PIX * pixOpen ( PIX *pixd, PIX *pixs, SEL *sel );
PIX * pixClose ( PIX *pixd, PIX *pixs, SEL *sel );
PIX * pixCloseSafe ( PIX *pixd, PIX *pixs, SEL *sel );
PIX * pixOpenGeneralized ( PIX *pixd, PIX *pixs, SEL *sel );
PIX * pixCloseGeneralized ( PIX *pixd, PIX *pixs, SEL *sel );
PIX * pixDilateBrick ( PIX *pixd, PIX *pixs, l_int32 hsize, l_int32 vsize );
PIX * pixErodeBrick ( PIX *pixd, PIX *pixs, l_int32 hsize, l_int32 vsize );
PIX * pixOpenBrick ( PIX *pixd, PIX *pixs, l_int32 hsize, l_int32 vsize );
PIX * pixCloseBrick ( PIX *pixd, PIX *pixs, l_int32 hsize, l_int32 vsize );
PIX * pixCloseSafeBrick ( PIX *pixd, PIX *pixs, l_int32 hsize, l_int32 vsize );
l_int32 selectComposableSels ( l_int32 size, l_int32 direction, SEL **psel1, SEL **psel2 );
l_ok selectComposableSizes ( l_int32 size, l_int32 *pfactor1, l_int32 *pfactor2 );
PIX * pixDilateCompBrick ( PIX *pixd, PIX *pixs, l_int32 hsize, l_int32 vsize );
PIX * pixErodeCompBrick ( PIX *pixd, PIX *pixs, l_int32 hsize, l_int32 vsize );
PIX * pixOpenCompBrick ( PIX *pixd, PIX *pixs, l_int32 hsize, l_int32 vsize );
PIX * pixCloseCompBrick ( PIX *pixd, PIX *pixs, l_int32 hsize, l_int32 vsize );
PIX * pixCloseSafeCompBrick ( PIX *pixd, PIX *pixs, l_int32 hsize, l_int32 vsize );
void resetMorphBoundaryCondition ( l_int32 bc );
l_uint32 getMorphBorderPixelColor ( l_int32 type, l_int32 depth );
PIX * pixExtractBoundary ( PIX *pixs, l_int32 type );
PIX * pixMorphSequenceMasked ( PIX *pixs, PIX *pixm, const char *sequence, l_int32 dispsep );
PIX * pixMorphSequenceByComponent ( PIX *pixs, const char *sequence, l_int32 connectivity, l_int32 minw, l_int32 minh, BOXA **pboxa );
PIXA * pixaMorphSequenceByComponent ( PIXA *pixas, const char *sequence, l_int32 minw, l_int32 minh );
PIX * pixMorphSequenceByRegion ( PIX *pixs, PIX *pixm, const char *sequence, l_int32 connectivity, l_int32 minw, l_int32 minh, BOXA **pboxa );
PIXA * pixaMorphSequenceByRegion ( PIX *pixs, PIXA *pixam, const char *sequence, l_int32 minw, l_int32 minh );
PIX * pixUnionOfMorphOps ( PIX *pixs, SELA *sela, l_int32 type );
PIX * pixIntersectionOfMorphOps ( PIX *pixs, SELA *sela, l_int32 type );
PIX * pixSelectiveConnCompFill ( PIX *pixs, l_int32 connectivity, l_int32 minw, l_int32 minh );
l_ok pixRemoveMatchedPattern ( PIX *pixs, PIX *pixp, PIX *pixe, l_int32 x0, l_int32 y0, l_int32 dsize );
PIX * pixDisplayMatchedPattern ( PIX *pixs, PIX *pixp, PIX *pixe, l_int32 x0, l_int32 y0, l_uint32 color, l_float32 scale, l_int32 nlevels );
PIXA * pixaExtendByMorph ( PIXA *pixas, l_int32 type, l_int32 niters, SEL *sel, l_int32 include );
PIXA * pixaExtendByScaling ( PIXA *pixas, NUMA *nasc, l_int32 type, l_int32 include );
PIX * pixSeedfillMorph ( PIX *pixs, PIX *pixm, l_int32 maxiters, l_int32 connectivity );
NUMA * pixRunHistogramMorph ( PIX *pixs, l_int32 runtype, l_int32 direction, l_int32 maxsize );
PIX * pixTophat ( PIX *pixs, l_int32 hsize, l_int32 vsize, l_int32 type );
PIX * pixHDome ( PIX *pixs, l_int32 height, l_int32 connectivity );
PIX * pixFastTophat ( PIX *pixs, l_int32 xsize, l_int32 ysize, l_int32 type );
PIX * pixMorphGradient ( PIX *pixs, l_int32 hsize, l_int32 vsize, l_int32 smoothing );
PTA * pixaCentroids ( PIXA *pixa );
l_ok pixCentroid ( PIX *pix, l_int32 *centtab, l_int32 *sumtab, l_float32 *pxave, l_float32 *pyave );
PIX * pixDilateBrickDwa ( PIX *pixd, PIX *pixs, l_int32 hsize, l_int32 vsize );
PIX * pixErodeBrickDwa ( PIX *pixd, PIX *pixs, l_int32 hsize, l_int32 vsize );
PIX * pixOpenBrickDwa ( PIX *pixd, PIX *pixs, l_int32 hsize, l_int32 vsize );
PIX * pixCloseBrickDwa ( PIX *pixd, PIX *pixs, l_int32 hsize, l_int32 vsize );
PIX * pixDilateCompBrickDwa ( PIX *pixd, PIX *pixs, l_int32 hsize, l_int32 vsize );
PIX * pixErodeCompBrickDwa ( PIX *pixd, PIX *pixs, l_int32 hsize, l_int32 vsize );
PIX * pixOpenCompBrickDwa ( PIX *pixd, PIX *pixs, l_int32 hsize, l_int32 vsize );
PIX * pixCloseCompBrickDwa ( PIX *pixd, PIX *pixs, l_int32 hsize, l_int32 vsize );
PIX * pixDilateCompBrickExtendDwa ( PIX *pixd, PIX *pixs, l_int32 hsize, l_int32 vsize );
PIX * pixErodeCompBrickExtendDwa ( PIX *pixd, PIX *pixs, l_int32 hsize, l_int32 vsize );
PIX * pixOpenCompBrickExtendDwa ( PIX *pixd, PIX *pixs, l_int32 hsize, l_int32 vsize );
PIX * pixCloseCompBrickExtendDwa ( PIX *pixd, PIX *pixs, l_int32 hsize, l_int32 vsize );
l_ok getExtendedCompositeParameters ( l_int32 size, l_int32 *pn, l_int32 *pextra, l_int32 *pactualsize );
PIX * pixMorphSequence ( PIX *pixs, const char *sequence, l_int32 dispsep );
PIX * pixMorphCompSequence ( PIX *pixs, const char *sequence, l_int32 dispsep );
PIX * pixMorphSequenceDwa ( PIX *pixs, const char *sequence, l_int32 dispsep );
PIX * pixMorphCompSequenceDwa ( PIX *pixs, const char *sequence, l_int32 dispsep );
l_int32 morphSequenceVerify ( SARRAY *sa );
PIX * pixGrayMorphSequence ( PIX *pixs, const char *sequence, l_int32 dispsep, l_int32 dispy );
PIX * pixColorMorphSequence ( PIX *pixs, const char *sequence, l_int32 dispsep, l_int32 dispy );
NUMA * numaCreate ( l_int32 n );
NUMA * numaCreateFromIArray ( l_int32 *iarray, l_int32 size );
NUMA * numaCreateFromFArray ( l_float32 *farray, l_int32 size, l_int32 copyflag );
NUMA * numaCreateFromString ( const char *str );
void numaDestroy ( NUMA **pna );
NUMA * numaCopy ( NUMA *na );
NUMA * numaClone ( NUMA *na );
l_ok numaEmpty ( NUMA *na );
l_ok numaAddNumber ( NUMA *na, l_float32 val );
l_ok numaInsertNumber ( NUMA *na, l_int32 index, l_float32 val );
l_ok numaRemoveNumber ( NUMA *na, l_int32 index );
l_ok numaReplaceNumber ( NUMA *na, l_int32 index, l_float32 val );
l_int32 numaGetCount ( NUMA *na );
l_ok numaSetCount ( NUMA *na, l_int32 newcount );
l_ok numaGetFValue ( NUMA *na, l_int32 index, l_float32 *pval );
l_ok numaGetIValue ( NUMA *na, l_int32 index, l_int32 *pival );
l_ok numaSetValue ( NUMA *na, l_int32 index, l_float32 val );
l_ok numaShiftValue ( NUMA *na, l_int32 index, l_float32 diff );
l_int32 * numaGetIArray ( NUMA *na );
l_float32 * numaGetFArray ( NUMA *na, l_int32 copyflag );
l_int32 numaGetRefcount ( NUMA *na );
l_ok numaChangeRefcount ( NUMA *na, l_int32 delta );
l_ok numaGetParameters ( NUMA *na, l_float32 *pstartx, l_float32 *pdelx );
l_ok numaSetParameters ( NUMA *na, l_float32 startx, l_float32 delx );
l_ok numaCopyParameters ( NUMA *nad, NUMA *nas );
SARRAY * numaConvertToSarray ( NUMA *na, l_int32 size1, l_int32 size2, l_int32 addzeros, l_int32 type );
NUMA * numaRead ( const char *filename );
NUMA * numaReadStream ( FILE *fp );
NUMA * numaReadMem ( const l_uint8 *data, size_t size );
l_ok numaWriteDebug ( const char *filename, NUMA *na );
l_ok numaWrite ( const char *filename, NUMA *na );
l_ok numaWriteStream ( FILE *fp, NUMA *na );
l_ok numaWriteMem ( l_uint8 **pdata, size_t *psize, NUMA *na );
NUMAA * numaaCreate ( l_int32 n );
NUMAA * numaaCreateFull ( l_int32 nptr, l_int32 n );
l_ok numaaTruncate ( NUMAA *naa );
void numaaDestroy ( NUMAA **pnaa );
l_ok numaaAddNuma ( NUMAA *naa, NUMA *na, l_int32 copyflag );
l_int32 numaaGetCount ( NUMAA *naa );
l_int32 numaaGetNumaCount ( NUMAA *naa, l_int32 index );
l_int32 numaaGetNumberCount ( NUMAA *naa );
NUMA ** numaaGetPtrArray ( NUMAA *naa );
NUMA * numaaGetNuma ( NUMAA *naa, l_int32 index, l_int32 accessflag );
l_ok numaaReplaceNuma ( NUMAA *naa, l_int32 index, NUMA *na );
l_ok numaaGetValue ( NUMAA *naa, l_int32 i, l_int32 j, l_float32 *pfval, l_int32 *pival );
l_ok numaaAddNumber ( NUMAA *naa, l_int32 index, l_float32 val );
NUMAA * numaaRead ( const char *filename );
NUMAA * numaaReadStream ( FILE *fp );
NUMAA * numaaReadMem ( const l_uint8 *data, size_t size );
l_ok numaaWrite ( const char *filename, NUMAA *naa );
l_ok numaaWriteStream ( FILE *fp, NUMAA *naa );
l_ok numaaWriteMem ( l_uint8 **pdata, size_t *psize, NUMAA *naa );
NUMA * numaArithOp ( NUMA *nad, NUMA *na1, NUMA *na2, l_int32 op );
NUMA * numaLogicalOp ( NUMA *nad, NUMA *na1, NUMA *na2, l_int32 op );
NUMA * numaInvert ( NUMA *nad, NUMA *nas );
l_int32 numaSimilar ( NUMA *na1, NUMA *na2, l_float32 maxdiff, l_int32 *psimilar );
l_ok numaAddToNumber ( NUMA *na, l_int32 index, l_float32 val );
l_ok numaGetMin ( NUMA *na, l_float32 *pminval, l_int32 *piminloc );
l_ok numaGetMax ( NUMA *na, l_float32 *pmaxval, l_int32 *pimaxloc );
l_ok numaGetSum ( NUMA *na, l_float32 *psum );
NUMA * numaGetPartialSums ( NUMA *na );
l_ok numaGetSumOnInterval ( NUMA *na, l_int32 first, l_int32 last, l_float32 *psum );
l_ok numaHasOnlyIntegers ( NUMA *na, l_int32 maxsamples, l_int32 *pallints );
NUMA * numaSubsample ( NUMA *nas, l_int32 subfactor );
NUMA * numaMakeDelta ( NUMA *nas );
NUMA * numaMakeSequence ( l_float32 startval, l_float32 increment, l_int32 size );
NUMA * numaMakeConstant ( l_float32 val, l_int32 size );
NUMA * numaMakeAbsValue ( NUMA *nad, NUMA *nas );
NUMA * numaAddBorder ( NUMA *nas, l_int32 left, l_int32 right, l_float32 val );
NUMA * numaAddSpecifiedBorder ( NUMA *nas, l_int32 left, l_int32 right, l_int32 type );
NUMA * numaRemoveBorder ( NUMA *nas, l_int32 left, l_int32 right );
l_ok numaCountNonzeroRuns ( NUMA *na, l_int32 *pcount );
l_ok numaGetNonzeroRange ( NUMA *na, l_float32 eps, l_int32 *pfirst, l_int32 *plast );
l_ok numaGetCountRelativeToZero ( NUMA *na, l_int32 type, l_int32 *pcount );
NUMA * numaClipToInterval ( NUMA *nas, l_int32 first, l_int32 last );
NUMA * numaMakeThresholdIndicator ( NUMA *nas, l_float32 thresh, l_int32 type );
NUMA * numaUniformSampling ( NUMA *nas, l_int32 nsamp );
NUMA * numaReverse ( NUMA *nad, NUMA *nas );
NUMA * numaLowPassIntervals ( NUMA *nas, l_float32 thresh, l_float32 maxn );
NUMA * numaThresholdEdges ( NUMA *nas, l_float32 thresh1, l_float32 thresh2, l_float32 maxn );
l_int32 numaGetSpanValues ( NUMA *na, l_int32 span, l_int32 *pstart, l_int32 *pend );
l_int32 numaGetEdgeValues ( NUMA *na, l_int32 edge, l_int32 *pstart, l_int32 *pend, l_int32 *psign );
l_ok numaInterpolateEqxVal ( l_float32 startx, l_float32 deltax, NUMA *nay, l_int32 type, l_float32 xval, l_float32 *pyval );
l_ok numaInterpolateArbxVal ( NUMA *nax, NUMA *nay, l_int32 type, l_float32 xval, l_float32 *pyval );
l_ok numaInterpolateEqxInterval ( l_float32 startx, l_float32 deltax, NUMA *nasy, l_int32 type, l_float32 x0, l_float32 x1, l_int32 npts, NUMA **pnax, NUMA **pnay );
l_ok numaInterpolateArbxInterval ( NUMA *nax, NUMA *nay, l_int32 type, l_float32 x0, l_float32 x1, l_int32 npts, NUMA **pnadx, NUMA **pnady );
l_ok numaFitMax ( NUMA *na, l_float32 *pmaxval, NUMA *naloc, l_float32 *pmaxloc );
l_ok numaDifferentiateInterval ( NUMA *nax, NUMA *nay, l_float32 x0, l_float32 x1, l_int32 npts, NUMA **pnadx, NUMA **pnady );
l_ok numaIntegrateInterval ( NUMA *nax, NUMA *nay, l_float32 x0, l_float32 x1, l_int32 npts, l_float32 *psum );
l_ok numaSortGeneral ( NUMA *na, NUMA **pnasort, NUMA **pnaindex, NUMA **pnainvert, l_int32 sortorder, l_int32 sorttype );
NUMA * numaSortAutoSelect ( NUMA *nas, l_int32 sortorder );
NUMA * numaSortIndexAutoSelect ( NUMA *nas, l_int32 sortorder );
l_int32 numaChooseSortType ( NUMA *nas );
NUMA * numaSort ( NUMA *naout, NUMA *nain, l_int32 sortorder );
NUMA * numaBinSort ( NUMA *nas, l_int32 sortorder );
NUMA * numaGetSortIndex ( NUMA *na, l_int32 sortorder );
NUMA * numaGetBinSortIndex ( NUMA *nas, l_int32 sortorder );
NUMA * numaSortByIndex ( NUMA *nas, NUMA *naindex );
l_int32 numaIsSorted ( NUMA *nas, l_int32 sortorder, l_int32 *psorted );
l_ok numaSortPair ( NUMA *nax, NUMA *nay, l_int32 sortorder, NUMA **pnasx, NUMA **pnasy );
NUMA * numaInvertMap ( NUMA *nas );
NUMA * numaPseudorandomSequence ( l_int32 size, l_int32 seed );
NUMA * numaRandomPermutation ( NUMA *nas, l_int32 seed );
l_ok numaGetRankValue ( NUMA *na, l_float32 fract, NUMA *nasort, l_int32 usebins, l_float32 *pval );
l_ok numaGetMedian ( NUMA *na, l_float32 *pval );
l_ok numaGetBinnedMedian ( NUMA *na, l_int32 *pval );
l_ok numaGetMeanDevFromMedian ( NUMA *na, l_float32 med, l_float32 *pdev );
l_ok numaGetMedianDevFromMedian ( NUMA *na, l_float32 *pmed, l_float32 *pdev );
l_ok numaGetMode ( NUMA *na, l_float32 *pval, l_int32 *pcount );
l_ok numaJoin ( NUMA *nad, NUMA *nas, l_int32 istart, l_int32 iend );
l_ok numaaJoin ( NUMAA *naad, NUMAA *naas, l_int32 istart, l_int32 iend );
NUMA * numaaFlattenToNuma ( NUMAA *naa );
NUMA * numaErode ( NUMA *nas, l_int32 size );
NUMA * numaDilate ( NUMA *nas, l_int32 size );
NUMA * numaOpen ( NUMA *nas, l_int32 size );
NUMA * numaClose ( NUMA *nas, l_int32 size );
NUMA * numaTransform ( NUMA *nas, l_float32 shift, l_float32 scale );
l_ok numaSimpleStats ( NUMA *na, l_int32 first, l_int32 last, l_float32 *pmean, l_float32 *pvar, l_float32 *prvar );
l_ok numaWindowedStats ( NUMA *nas, l_int32 wc, NUMA **pnam, NUMA **pnams, NUMA **pnav, NUMA **pnarv );
NUMA * numaWindowedMean ( NUMA *nas, l_int32 wc );
NUMA * numaWindowedMeanSquare ( NUMA *nas, l_int32 wc );
l_ok numaWindowedVariance ( NUMA *nam, NUMA *nams, NUMA **pnav, NUMA **pnarv );
NUMA * numaWindowedMedian ( NUMA *nas, l_int32 halfwin );
NUMA * numaConvertToInt ( NUMA *nas );
NUMA * numaMakeHistogram ( NUMA *na, l_int32 maxbins, l_int32 *pbinsize, l_int32 *pbinstart );
NUMA * numaMakeHistogramAuto ( NUMA *na, l_int32 maxbins );
NUMA * numaMakeHistogramClipped ( NUMA *na, l_float32 binsize, l_float32 maxsize );
NUMA * numaRebinHistogram ( NUMA *nas, l_int32 newsize );
NUMA * numaNormalizeHistogram ( NUMA *nas, l_float32 tsum );
l_ok numaGetStatsUsingHistogram ( NUMA *na, l_int32 maxbins, l_float32 *pmin, l_float32 *pmax, l_float32 *pmean, l_float32 *pvariance, l_float32 *pmedian, l_float32 rank, l_float32 *prval, NUMA **phisto );
l_ok numaGetHistogramStats ( NUMA *nahisto, l_float32 startx, l_float32 deltax, l_float32 *pxmean, l_float32 *pxmedian, l_float32 *pxmode, l_float32 *pxvariance );
l_ok numaGetHistogramStatsOnInterval ( NUMA *nahisto, l_float32 startx, l_float32 deltax, l_int32 ifirst, l_int32 ilast, l_float32 *pxmean, l_float32 *pxmedian, l_float32 *pxmode, l_float32 *pxvariance );
l_ok numaMakeRankFromHistogram ( l_float32 startx, l_float32 deltax, NUMA *nasy, l_int32 npts, NUMA **pnax, NUMA **pnay );
l_ok numaHistogramGetRankFromVal ( NUMA *na, l_float32 rval, l_float32 *prank );
l_ok numaHistogramGetValFromRank ( NUMA *na, l_float32 rank, l_float32 *prval );
l_ok numaDiscretizeRankAndIntensity ( NUMA *na, l_int32 nbins, NUMA **pnarbin, NUMA **pnam, NUMA **pnar, NUMA **pnabb );
l_ok numaGetRankBinValues ( NUMA *na, l_int32 nbins, NUMA **pnarbin, NUMA **pnam );
l_ok numaSplitDistribution ( NUMA *na, l_float32 scorefract, l_int32 *psplitindex, l_float32 *pave1, l_float32 *pave2, l_float32 *pnum1, l_float32 *pnum2, NUMA **pnascore );
l_ok grayHistogramsToEMD ( NUMAA *naa1, NUMAA *naa2, NUMA **pnad );
l_ok numaEarthMoverDistance ( NUMA *na1, NUMA *na2, l_float32 *pdist );
l_ok grayInterHistogramStats ( NUMAA *naa, l_int32 wc, NUMA **pnam, NUMA **pnams, NUMA **pnav, NUMA **pnarv );
NUMA * numaFindPeaks ( NUMA *nas, l_int32 nmax, l_float32 fract1, l_float32 fract2 );
NUMA * numaFindExtrema ( NUMA *nas, l_float32 delta, NUMA **pnav );
l_ok numaCountReversals ( NUMA *nas, l_float32 minreversal, l_int32 *pnr, l_float32 *prd );
l_ok numaSelectCrossingThreshold ( NUMA *nax, NUMA *nay, l_float32 estthresh, l_float32 *pbestthresh );
NUMA * numaCrossingsByThreshold ( NUMA *nax, NUMA *nay, l_float32 thresh );
NUMA * numaCrossingsByPeaks ( NUMA *nax, NUMA *nay, l_float32 delta );
l_ok numaEvalBestHaarParameters ( NUMA *nas, l_float32 relweight, l_int32 nwidth, l_int32 nshift, l_float32 minwidth, l_float32 maxwidth, l_float32 *pbestwidth, l_float32 *pbestshift, l_float32 *pbestscore );
l_ok numaEvalHaarSum ( NUMA *nas, l_float32 width, l_float32 shift, l_float32 relweight, l_float32 *pscore );
NUMA * genConstrainedNumaInRange ( l_int32 first, l_int32 last, l_int32 nmax, l_int32 use_pairs );
l_ok pixGetRegionsBinary ( PIX *pixs, PIX **ppixhm, PIX **ppixtm, PIX **ppixtb, PIXA *pixadb );
PIX * pixGenHalftoneMask ( PIX *pixs, PIX **ppixtext, l_int32 *phtfound, l_int32 debug );
PIX * pixGenerateHalftoneMask ( PIX *pixs, PIX **ppixtext, l_int32 *phtfound, PIXA *pixadb );
PIX * pixGenTextlineMask ( PIX *pixs, PIX **ppixvws, l_int32 *ptlfound, PIXA *pixadb );
PIX * pixGenTextblockMask ( PIX *pixs, PIX *pixvws, PIXA *pixadb );
BOX * pixFindPageForeground ( PIX *pixs, l_int32 threshold, l_int32 mindist, l_int32 erasedist, l_int32 showmorph, PIXAC *pixac );
l_ok pixSplitIntoCharacters ( PIX *pixs, l_int32 minw, l_int32 minh, BOXA **pboxa, PIXA **ppixa, PIX **ppixdebug );
BOXA * pixSplitComponentWithProfile ( PIX *pixs, l_int32 delta, l_int32 mindel, PIX **ppixdebug );
PIXA * pixExtractTextlines ( PIX *pixs, l_int32 maxw, l_int32 maxh, l_int32 minw, l_int32 minh, l_int32 adjw, l_int32 adjh, PIXA *pixadb );
PIXA * pixExtractRawTextlines ( PIX *pixs, l_int32 maxw, l_int32 maxh, l_int32 adjw, l_int32 adjh, PIXA *pixadb );
l_ok pixCountTextColumns ( PIX *pixs, l_float32 deltafract, l_float32 peakfract, l_float32 clipfract, l_int32 *pncols, PIXA *pixadb );
l_ok pixDecideIfText ( PIX *pixs, BOX *box, l_int32 *pistext, PIXA *pixadb );
l_ok pixFindThreshFgExtent ( PIX *pixs, l_int32 thresh, l_int32 *ptop, l_int32 *pbot );
l_ok pixDecideIfTable ( PIX *pixs, BOX *box, l_int32 orient, l_int32 *pscore, PIXA *pixadb );
PIX * pixPrepare1bpp ( PIX *pixs, BOX *box, l_float32 cropfract, l_int32 outres );
l_ok pixEstimateBackground ( PIX *pixs, l_int32 darkthresh, l_float32 edgecrop, l_int32 *pbg );
l_ok pixFindLargeRectangles ( PIX *pixs, l_int32 polarity, l_int32 nrect, BOXA **pboxa, PIX **ppixdb );
l_ok pixFindLargestRectangle ( PIX *pixs, l_int32 polarity, BOX **pbox, PIX **ppixdb );
l_ok pixSetSelectCmap ( PIX *pixs, BOX *box, l_int32 sindex, l_int32 rval, l_int32 gval, l_int32 bval );
l_ok pixColorGrayRegionsCmap ( PIX *pixs, BOXA *boxa, l_int32 type, l_int32 rval, l_int32 gval, l_int32 bval );
l_ok pixColorGrayCmap ( PIX *pixs, BOX *box, l_int32 type, l_int32 rval, l_int32 gval, l_int32 bval );
l_ok pixColorGrayMaskedCmap ( PIX *pixs, PIX *pixm, l_int32 type, l_int32 rval, l_int32 gval, l_int32 bval );
l_ok addColorizedGrayToCmap ( PIXCMAP *cmap, l_int32 type, l_int32 rval, l_int32 gval, l_int32 bval, NUMA **pna );
l_ok pixSetSelectMaskedCmap ( PIX *pixs, PIX *pixm, l_int32 x, l_int32 y, l_int32 sindex, l_int32 rval, l_int32 gval, l_int32 bval );
l_ok pixSetMaskedCmap ( PIX *pixs, PIX *pixm, l_int32 x, l_int32 y, l_int32 rval, l_int32 gval, l_int32 bval );
char * parseForProtos ( const char *filein, const char *prestring );
BOXA * boxaGetWhiteblocks ( BOXA *boxas, BOX *box, l_int32 sortflag, l_int32 maxboxes, l_float32 maxoverlap, l_int32 maxperim, l_float32 fract, l_int32 maxpops );
BOXA * boxaPruneSortedOnOverlap ( BOXA *boxas, l_float32 maxoverlap );
l_ok convertFilesToPdf ( const char *dirname, const char *substr, l_int32 res, l_float32 scalefactor, l_int32 type, l_int32 quality, const char *title, const char *fileout );
l_ok saConvertFilesToPdf ( SARRAY *sa, l_int32 res, l_float32 scalefactor, l_int32 type, l_int32 quality, const char *title, const char *fileout );
l_ok saConvertFilesToPdfData ( SARRAY *sa, l_int32 res, l_float32 scalefactor, l_int32 type, l_int32 quality, const char *title, l_uint8 **pdata, size_t *pnbytes );
l_ok selectDefaultPdfEncoding ( PIX *pix, l_int32 *ptype );
l_ok convertUnscaledFilesToPdf ( const char *dirname, const char *substr, const char *title, const char *fileout );
l_ok saConvertUnscaledFilesToPdf ( SARRAY *sa, const char *title, const char *fileout );
l_ok saConvertUnscaledFilesToPdfData ( SARRAY *sa, const char *title, l_uint8 **pdata, size_t *pnbytes );
l_ok convertUnscaledToPdfData ( const char *fname, const char *title, l_uint8 **pdata, size_t *pnbytes );
l_ok pixaConvertToPdf ( PIXA *pixa, l_int32 res, l_float32 scalefactor, l_int32 type, l_int32 quality, const char *title, const char *fileout );
l_ok pixaConvertToPdfData ( PIXA *pixa, l_int32 res, l_float32 scalefactor, l_int32 type, l_int32 quality, const char *title, l_uint8 **pdata, size_t *pnbytes );
l_ok convertToPdf ( const char *filein, l_int32 type, l_int32 quality, const char *fileout, l_int32 x, l_int32 y, l_int32 res, const char *title, L_PDF_DATA **plpd, l_int32 position );
l_ok convertImageDataToPdf ( l_uint8 *imdata, size_t size, l_int32 type, l_int32 quality, const char *fileout, l_int32 x, l_int32 y, l_int32 res, const char *title, L_PDF_DATA **plpd, l_int32 position );
l_ok convertToPdfData ( const char *filein, l_int32 type, l_int32 quality, l_uint8 **pdata, size_t *pnbytes, l_int32 x, l_int32 y, l_int32 res, const char *title, L_PDF_DATA **plpd, l_int32 position );
l_ok convertImageDataToPdfData ( l_uint8 *imdata, size_t size, l_int32 type, l_int32 quality, l_uint8 **pdata, size_t *pnbytes, l_int32 x, l_int32 y, l_int32 res, const char *title, L_PDF_DATA **plpd, l_int32 position );
l_ok pixConvertToPdf ( PIX *pix, l_int32 type, l_int32 quality, const char *fileout, l_int32 x, l_int32 y, l_int32 res, const char *title, L_PDF_DATA **plpd, l_int32 position );
l_ok pixWriteStreamPdf ( FILE *fp, PIX *pix, l_int32 res, const char *title );
l_ok pixWriteMemPdf ( l_uint8 **pdata, size_t *pnbytes, PIX *pix, l_int32 res, const char *title );
l_ok convertSegmentedFilesToPdf ( const char *dirname, const char *substr, l_int32 res, l_int32 type, l_int32 thresh, BOXAA *baa, l_int32 quality, l_float32 scalefactor, const char *title, const char *fileout );
BOXAA * convertNumberedMasksToBoxaa ( const char *dirname, const char *substr, l_int32 numpre, l_int32 numpost );
l_ok convertToPdfSegmented ( const char *filein, l_int32 res, l_int32 type, l_int32 thresh, BOXA *boxa, l_int32 quality, l_float32 scalefactor, const char *title, const char *fileout );
l_ok pixConvertToPdfSegmented ( PIX *pixs, l_int32 res, l_int32 type, l_int32 thresh, BOXA *boxa, l_int32 quality, l_float32 scalefactor, const char *title, const char *fileout );
l_ok convertToPdfDataSegmented ( const char *filein, l_int32 res, l_int32 type, l_int32 thresh, BOXA *boxa, l_int32 quality, l_float32 scalefactor, const char *title, l_uint8 **pdata, size_t *pnbytes );
l_ok pixConvertToPdfDataSegmented ( PIX *pixs, l_int32 res, l_int32 type, l_int32 thresh, BOXA *boxa, l_int32 quality, l_float32 scalefactor, const char *title, l_uint8 **pdata, size_t *pnbytes );
l_ok concatenatePdf ( const char *dirname, const char *substr, const char *fileout );
l_ok saConcatenatePdf ( SARRAY *sa, const char *fileout );
l_ok ptraConcatenatePdf ( L_PTRA *pa, const char *fileout );
l_ok concatenatePdfToData ( const char *dirname, const char *substr, l_uint8 **pdata, size_t *pnbytes );
l_ok saConcatenatePdfToData ( SARRAY *sa, l_uint8 **pdata, size_t *pnbytes );
l_ok pixConvertToPdfData ( PIX *pix, l_int32 type, l_int32 quality, l_uint8 **pdata, size_t *pnbytes, l_int32 x, l_int32 y, l_int32 res, const char *title, L_PDF_DATA **plpd, l_int32 position );
l_ok ptraConcatenatePdfToData ( L_PTRA *pa_data, SARRAY *sa, l_uint8 **pdata, size_t *pnbytes );
l_ok convertTiffMultipageToPdf ( const char *filein, const char *fileout );
l_ok l_generateCIDataForPdf ( const char *fname, PIX *pix, l_int32 quality, L_COMP_DATA **pcid );
L_COMP_DATA * l_generateFlateDataPdf ( const char *fname, PIX *pixs );
L_COMP_DATA * l_generateJpegData ( const char *fname, l_int32 ascii85flag );
L_COMP_DATA * l_generateJpegDataMem ( l_uint8 *data, size_t nbytes, l_int32 ascii85flag );
l_ok l_generateCIData ( const char *fname, l_int32 type, l_int32 quality, l_int32 ascii85, L_COMP_DATA **pcid );
l_ok pixGenerateCIData ( PIX *pixs, l_int32 type, l_int32 quality, l_int32 ascii85, L_COMP_DATA **pcid );
L_COMP_DATA * l_generateFlateData ( const char *fname, l_int32 ascii85flag );
L_COMP_DATA * l_generateG4Data ( const char *fname, l_int32 ascii85flag );
l_ok cidConvertToPdfData ( L_COMP_DATA *cid, const char *title, l_uint8 **pdata, size_t *pnbytes );
void l_CIDataDestroy ( L_COMP_DATA **pcid );
void l_pdfSetG4ImageMask ( l_int32 flag );
void l_pdfSetDateAndVersion ( l_int32 flag );
void setPixMemoryManager ( alloc_fn allocator, dealloc_fn deallocator );
PIX * pixCreate ( l_int32 width, l_int32 height, l_int32 depth );
PIX * pixCreateNoInit ( l_int32 width, l_int32 height, l_int32 depth );
PIX * pixCreateTemplate ( PIX *pixs );
PIX * pixCreateTemplateNoInit ( PIX *pixs );
PIX * pixCreateHeader ( l_int32 width, l_int32 height, l_int32 depth );
PIX * pixClone ( PIX *pixs );
void pixDestroy ( PIX **ppix );
PIX * pixCopy ( PIX *pixd, PIX *pixs );
l_ok pixResizeImageData ( PIX *pixd, const PIX *pixs );
l_ok pixCopyColormap ( PIX *pixd, PIX *pixs );
l_int32 pixSizesEqual ( const PIX *pix1, const PIX *pix2 );
l_ok pixTransferAllData ( PIX *pixd, PIX **ppixs, l_int32 copytext, l_int32 copyformat );
l_ok pixSwapAndDestroy ( PIX **ppixd, PIX **ppixs );
l_int32 pixGetWidth ( const PIX *pix );
l_int32 pixSetWidth ( PIX *pix, l_int32 width );
l_int32 pixGetHeight ( const PIX *pix );
l_int32 pixSetHeight ( PIX *pix, l_int32 height );
l_int32 pixGetDepth ( const PIX *pix );
l_int32 pixSetDepth ( PIX *pix, l_int32 depth );
l_ok pixGetDimensions ( const PIX *pix, l_int32 *pw, l_int32 *ph, l_int32 *pd );
l_ok pixSetDimensions ( PIX *pix, l_int32 w, l_int32 h, l_int32 d );
l_ok pixCopyDimensions ( PIX *pixd, const PIX *pixs );
l_int32 pixGetSpp ( const PIX *pix );
l_int32 pixSetSpp ( PIX *pix, l_int32 spp );
l_ok pixCopySpp ( PIX *pixd, const PIX *pixs );
l_int32 pixGetWpl ( const PIX *pix );
l_int32 pixSetWpl ( PIX *pix, l_int32 wpl );
l_int32 pixGetRefcount ( const PIX *pix );
l_int32 pixChangeRefcount ( PIX *pix, l_int32 delta );
l_int32 pixGetXRes ( const PIX *pix );
l_int32 pixSetXRes ( PIX *pix, l_int32 res );
l_int32 pixGetYRes ( const PIX *pix );
l_int32 pixSetYRes ( PIX *pix, l_int32 res );
l_ok pixGetResolution ( const PIX *pix, l_int32 *pxres, l_int32 *pyres );
l_ok pixSetResolution ( PIX *pix, l_int32 xres, l_int32 yres );
l_int32 pixCopyResolution ( PIX *pixd, const PIX *pixs );
l_int32 pixScaleResolution ( PIX *pix, l_float32 xscale, l_float32 yscale );
l_int32 pixGetInputFormat ( const PIX *pix );
l_int32 pixSetInputFormat ( PIX *pix, l_int32 informat );
l_int32 pixCopyInputFormat ( PIX *pixd, const PIX *pixs );
l_int32 pixSetSpecial ( PIX *pix, l_int32 special );
char * pixGetText ( PIX *pix );
l_ok pixSetText ( PIX *pix, const char *textstring );
l_ok pixAddText ( PIX *pix, const char *textstring );
l_int32 pixCopyText ( PIX *pixd, PIX *pixs );
PIXCMAP * pixGetColormap ( PIX *pix );
l_ok pixSetColormap ( PIX *pix, PIXCMAP *colormap );
l_ok pixDestroyColormap ( PIX *pix );
l_uint32 * pixGetData ( PIX *pix );
l_int32 pixSetData ( PIX *pix, l_uint32 *data );
l_uint32 * pixExtractData ( PIX *pixs );
l_int32 pixFreeData ( PIX *pix );
void ** pixGetLinePtrs ( PIX *pix, l_int32 *psize );
l_ok pixPrintStreamInfo ( FILE *fp, PIX *pix, const char *text );
l_ok pixGetPixel ( PIX *pix, l_int32 x, l_int32 y, l_uint32 *pval );
l_ok pixSetPixel ( PIX *pix, l_int32 x, l_int32 y, l_uint32 val );
l_ok pixGetRGBPixel ( PIX *pix, l_int32 x, l_int32 y, l_int32 *prval, l_int32 *pgval, l_int32 *pbval );
l_ok pixSetRGBPixel ( PIX *pix, l_int32 x, l_int32 y, l_int32 rval, l_int32 gval, l_int32 bval );
l_ok pixGetRandomPixel ( PIX *pix, l_uint32 *pval, l_int32 *px, l_int32 *py );
l_ok pixClearPixel ( PIX *pix, l_int32 x, l_int32 y );
l_ok pixFlipPixel ( PIX *pix, l_int32 x, l_int32 y );
void setPixelLow ( l_uint32 *line, l_int32 x, l_int32 depth, l_uint32 val );
l_ok pixGetBlackOrWhiteVal ( PIX *pixs, l_int32 op, l_uint32 *pval );
l_ok pixClearAll ( PIX *pix );
l_ok pixSetAll ( PIX *pix );
l_ok pixSetAllGray ( PIX *pix, l_int32 grayval );
l_ok pixSetAllArbitrary ( PIX *pix, l_uint32 val );
l_ok pixSetBlackOrWhite ( PIX *pixs, l_int32 op );
l_ok pixSetComponentArbitrary ( PIX *pix, l_int32 comp, l_int32 val );
l_ok pixClearInRect ( PIX *pix, BOX *box );
l_ok pixSetInRect ( PIX *pix, BOX *box );
l_ok pixSetInRectArbitrary ( PIX *pix, BOX *box, l_uint32 val );
l_ok pixBlendInRect ( PIX *pixs, BOX *box, l_uint32 val, l_float32 fract );
l_ok pixSetPadBits ( PIX *pix, l_int32 val );
l_ok pixSetPadBitsBand ( PIX *pix, l_int32 by, l_int32 bh, l_int32 val );
l_ok pixSetOrClearBorder ( PIX *pixs, l_int32 left, l_int32 right, l_int32 top, l_int32 bot, l_int32 op );
l_ok pixSetBorderVal ( PIX *pixs, l_int32 left, l_int32 right, l_int32 top, l_int32 bot, l_uint32 val );
l_ok pixSetBorderRingVal ( PIX *pixs, l_int32 dist, l_uint32 val );
l_ok pixSetMirroredBorder ( PIX *pixs, l_int32 left, l_int32 right, l_int32 top, l_int32 bot );
PIX * pixCopyBorder ( PIX *pixd, PIX *pixs, l_int32 left, l_int32 right, l_int32 top, l_int32 bot );
PIX * pixAddBorder ( PIX *pixs, l_int32 npix, l_uint32 val );
PIX * pixAddBlackOrWhiteBorder ( PIX *pixs, l_int32 left, l_int32 right, l_int32 top, l_int32 bot, l_int32 op );
PIX * pixAddBorderGeneral ( PIX *pixs, l_int32 left, l_int32 right, l_int32 top, l_int32 bot, l_uint32 val );
PIX * pixRemoveBorder ( PIX *pixs, l_int32 npix );
PIX * pixRemoveBorderGeneral ( PIX *pixs, l_int32 left, l_int32 right, l_int32 top, l_int32 bot );
PIX * pixRemoveBorderToSize ( PIX *pixs, l_int32 wd, l_int32 hd );
PIX * pixAddMirroredBorder ( PIX *pixs, l_int32 left, l_int32 right, l_int32 top, l_int32 bot );
PIX * pixAddRepeatedBorder ( PIX *pixs, l_int32 left, l_int32 right, l_int32 top, l_int32 bot );
PIX * pixAddMixedBorder ( PIX *pixs, l_int32 left, l_int32 right, l_int32 top, l_int32 bot );
PIX * pixAddContinuedBorder ( PIX *pixs, l_int32 left, l_int32 right, l_int32 top, l_int32 bot );
l_ok pixShiftAndTransferAlpha ( PIX *pixd, PIX *pixs, l_float32 shiftx, l_float32 shifty );
PIX * pixDisplayLayersRGBA ( PIX *pixs, l_uint32 val, l_int32 maxw );
PIX * pixCreateRGBImage ( PIX *pixr, PIX *pixg, PIX *pixb );
PIX * pixGetRGBComponent ( PIX *pixs, l_int32 comp );
l_ok pixSetRGBComponent ( PIX *pixd, PIX *pixs, l_int32 comp );
PIX * pixGetRGBComponentCmap ( PIX *pixs, l_int32 comp );
l_ok pixCopyRGBComponent ( PIX *pixd, PIX *pixs, l_int32 comp );
l_ok composeRGBPixel ( l_int32 rval, l_int32 gval, l_int32 bval, l_uint32 *ppixel );
l_ok composeRGBAPixel ( l_int32 rval, l_int32 gval, l_int32 bval, l_int32 aval, l_uint32 *ppixel );
void extractRGBValues ( l_uint32 pixel, l_int32 *prval, l_int32 *pgval, l_int32 *pbval );
void extractRGBAValues ( l_uint32 pixel, l_int32 *prval, l_int32 *pgval, l_int32 *pbval, l_int32 *paval );
l_int32 extractMinMaxComponent ( l_uint32 pixel, l_int32 type );
l_ok pixGetRGBLine ( PIX *pixs, l_int32 row, l_uint8 *bufr, l_uint8 *bufg, l_uint8 *bufb );
PIX * pixEndianByteSwapNew ( PIX *pixs );
l_ok pixEndianByteSwap ( PIX *pixs );
l_int32 lineEndianByteSwap ( l_uint32 *datad, l_uint32 *datas, l_int32 wpl );
PIX * pixEndianTwoByteSwapNew ( PIX *pixs );
l_ok pixEndianTwoByteSwap ( PIX *pixs );
l_ok pixGetRasterData ( PIX *pixs, l_uint8 **pdata, size_t *pnbytes );
l_ok pixAlphaIsOpaque ( PIX *pix, l_int32 *popaque );
l_uint8 ** pixSetupByteProcessing ( PIX *pix, l_int32 *pw, l_int32 *ph );
l_ok pixCleanupByteProcessing ( PIX *pix, l_uint8 **lineptrs );
void l_setAlphaMaskBorder ( l_float32 val1, l_float32 val2 );
l_ok pixSetMasked ( PIX *pixd, PIX *pixm, l_uint32 val );
l_ok pixSetMaskedGeneral ( PIX *pixd, PIX *pixm, l_uint32 val, l_int32 x, l_int32 y );
l_ok pixCombineMasked ( PIX *pixd, PIX *pixs, PIX *pixm );
l_ok pixCombineMaskedGeneral ( PIX *pixd, PIX *pixs, PIX *pixm, l_int32 x, l_int32 y );
l_ok pixPaintThroughMask ( PIX *pixd, PIX *pixm, l_int32 x, l_int32 y, l_uint32 val );
l_ok pixPaintSelfThroughMask ( PIX *pixd, PIX *pixm, l_int32 x, l_int32 y, l_int32 searchdir, l_int32 mindist, l_int32 tilesize, l_int32 ntiles, l_int32 distblend );
PIX * pixMakeMaskFromVal ( PIX *pixs, l_int32 val );
PIX * pixMakeMaskFromLUT ( PIX *pixs, l_int32 *tab );
PIX * pixMakeArbMaskFromRGB ( PIX *pixs, l_float32 rc, l_float32 gc, l_float32 bc, l_float32 thresh );
PIX * pixSetUnderTransparency ( PIX *pixs, l_uint32 val, l_int32 debug );
PIX * pixMakeAlphaFromMask ( PIX *pixs, l_int32 dist, BOX **pbox );
l_ok pixGetColorNearMaskBoundary ( PIX *pixs, PIX *pixm, BOX *box, l_int32 dist, l_uint32 *pval, l_int32 debug );
PIX * pixInvert ( PIX *pixd, PIX *pixs );
PIX * pixOr ( PIX *pixd, PIX *pixs1, PIX *pixs2 );
PIX * pixAnd ( PIX *pixd, PIX *pixs1, PIX *pixs2 );
PIX * pixXor ( PIX *pixd, PIX *pixs1, PIX *pixs2 );
PIX * pixSubtract ( PIX *pixd, PIX *pixs1, PIX *pixs2 );
l_ok pixZero ( PIX *pix, l_int32 *pempty );
l_ok pixForegroundFraction ( PIX *pix, l_float32 *pfract );
NUMA * pixaCountPixels ( PIXA *pixa );
l_ok pixCountPixels ( PIX *pixs, l_int32 *pcount, l_int32 *tab8 );
l_ok pixCountPixelsInRect ( PIX *pixs, BOX *box, l_int32 *pcount, l_int32 *tab8 );
NUMA * pixCountByRow ( PIX *pix, BOX *box );
NUMA * pixCountByColumn ( PIX *pix, BOX *box );
NUMA * pixCountPixelsByRow ( PIX *pix, l_int32 *tab8 );
NUMA * pixCountPixelsByColumn ( PIX *pix );
l_ok pixCountPixelsInRow ( PIX *pix, l_int32 row, l_int32 *pcount, l_int32 *tab8 );
NUMA * pixGetMomentByColumn ( PIX *pix, l_int32 order );
l_ok pixThresholdPixelSum ( PIX *pix, l_int32 thresh, l_int32 *pabove, l_int32 *tab8 );
l_int32 * makePixelSumTab8 ( void );
l_int32 * makePixelCentroidTab8 ( void );
NUMA * pixAverageByRow ( PIX *pix, BOX *box, l_int32 type );
NUMA * pixAverageByColumn ( PIX *pix, BOX *box, l_int32 type );
l_ok pixAverageInRect ( PIX *pix, BOX *box, l_float32 *pave );
NUMA * pixVarianceByRow ( PIX *pix, BOX *box );
NUMA * pixVarianceByColumn ( PIX *pix, BOX *box );
l_ok pixVarianceInRect ( PIX *pix, BOX *box, l_float32 *prootvar );
NUMA * pixAbsDiffByRow ( PIX *pix, BOX *box );
NUMA * pixAbsDiffByColumn ( PIX *pix, BOX *box );
l_ok pixAbsDiffInRect ( PIX *pix, BOX *box, l_int32 dir, l_float32 *pabsdiff );
l_ok pixAbsDiffOnLine ( PIX *pix, l_int32 x1, l_int32 y1, l_int32 x2, l_int32 y2, l_float32 *pabsdiff );
l_int32 pixCountArbInRect ( PIX *pixs, BOX *box, l_int32 val, l_int32 factor, l_int32 *pcount );
PIX * pixMirroredTiling ( PIX *pixs, l_int32 w, l_int32 h );
l_ok pixFindRepCloseTile ( PIX *pixs, BOX *box, l_int32 searchdir, l_int32 mindist, l_int32 tsize, l_int32 ntiles, BOX **pboxtile, l_int32 debug );
NUMA * pixGetGrayHistogram ( PIX *pixs, l_int32 factor );
NUMA * pixGetGrayHistogramMasked ( PIX *pixs, PIX *pixm, l_int32 x, l_int32 y, l_int32 factor );
NUMA * pixGetGrayHistogramInRect ( PIX *pixs, BOX *box, l_int32 factor );
NUMAA * pixGetGrayHistogramTiled ( PIX *pixs, l_int32 factor, l_int32 nx, l_int32 ny );
l_ok pixGetColorHistogram ( PIX *pixs, l_int32 factor, NUMA **pnar, NUMA **pnag, NUMA **pnab );
l_ok pixGetColorHistogramMasked ( PIX *pixs, PIX *pixm, l_int32 x, l_int32 y, l_int32 factor, NUMA **pnar, NUMA **pnag, NUMA **pnab );
NUMA * pixGetCmapHistogram ( PIX *pixs, l_int32 factor );
NUMA * pixGetCmapHistogramMasked ( PIX *pixs, PIX *pixm, l_int32 x, l_int32 y, l_int32 factor );
NUMA * pixGetCmapHistogramInRect ( PIX *pixs, BOX *box, l_int32 factor );
l_int32 pixCountRGBColors ( PIX *pixs );
L_AMAP * pixGetColorAmapHistogram ( PIX *pixs, l_int32 factor );
l_int32 amapGetCountForColor ( L_AMAP *amap, l_uint32 val );
l_ok pixGetRankValue ( PIX *pixs, l_int32 factor, l_float32 rank, l_uint32 *pvalue );
l_ok pixGetRankValueMaskedRGB ( PIX *pixs, PIX *pixm, l_int32 x, l_int32 y, l_int32 factor, l_float32 rank, l_float32 *prval, l_float32 *pgval, l_float32 *pbval );
l_ok pixGetRankValueMasked ( PIX *pixs, PIX *pixm, l_int32 x, l_int32 y, l_int32 factor, l_float32 rank, l_float32 *pval, NUMA **pna );
l_ok pixGetPixelAverage ( PIX *pixs, PIX *pixm, l_int32 x, l_int32 y, l_int32 factor, l_uint32 *pval );
l_ok pixGetPixelStats ( PIX *pixs, l_int32 factor, l_int32 type, l_uint32 *pvalue );
l_ok pixGetAverageMaskedRGB ( PIX *pixs, PIX *pixm, l_int32 x, l_int32 y, l_int32 factor, l_int32 type, l_float32 *prval, l_float32 *pgval, l_float32 *pbval );
l_ok pixGetAverageMasked ( PIX *pixs, PIX *pixm, l_int32 x, l_int32 y, l_int32 factor, l_int32 type, l_float32 *pval );
l_ok pixGetAverageTiledRGB ( PIX *pixs, l_int32 sx, l_int32 sy, l_int32 type, PIX **ppixr, PIX **ppixg, PIX **ppixb );
PIX * pixGetAverageTiled ( PIX *pixs, l_int32 sx, l_int32 sy, l_int32 type );
l_int32 pixRowStats ( PIX *pixs, BOX *box, NUMA **pnamean, NUMA **pnamedian, NUMA **pnamode, NUMA **pnamodecount, NUMA **pnavar, NUMA **pnarootvar );
l_int32 pixColumnStats ( PIX *pixs, BOX *box, NUMA **pnamean, NUMA **pnamedian, NUMA **pnamode, NUMA **pnamodecount, NUMA **pnavar, NUMA **pnarootvar );
l_ok pixGetRangeValues ( PIX *pixs, l_int32 factor, l_int32 color, l_int32 *pminval, l_int32 *pmaxval );
l_ok pixGetExtremeValue ( PIX *pixs, l_int32 factor, l_int32 type, l_int32 *prval, l_int32 *pgval, l_int32 *pbval, l_int32 *pgrayval );
l_ok pixGetMaxValueInRect ( PIX *pixs, BOX *box, l_uint32 *pmaxval, l_int32 *pxmax, l_int32 *pymax );
l_ok pixGetBinnedComponentRange ( PIX *pixs, l_int32 nbins, l_int32 factor, l_int32 color, l_int32 *pminval, l_int32 *pmaxval, l_uint32 **pcarray, l_int32 fontsize );
l_ok pixGetRankColorArray ( PIX *pixs, l_int32 nbins, l_int32 type, l_int32 factor, l_uint32 **pcarray, l_int32 debugflag, l_int32 fontsize );
l_ok pixGetBinnedColor ( PIX *pixs, PIX *pixg, l_int32 factor, l_int32 nbins, NUMA *nalut, l_uint32 **pcarray, l_int32 debugflag );
PIX * pixDisplayColorArray ( l_uint32 *carray, l_int32 ncolors, l_int32 side, l_int32 ncols, l_int32 fontsize );
PIX * pixRankBinByStrip ( PIX *pixs, l_int32 direction, l_int32 size, l_int32 nbins, l_int32 type );
PIX * pixaGetAlignedStats ( PIXA *pixa, l_int32 type, l_int32 nbins, l_int32 thresh );
l_ok pixaExtractColumnFromEachPix ( PIXA *pixa, l_int32 col, PIX *pixd );
l_ok pixGetRowStats ( PIX *pixs, l_int32 type, l_int32 nbins, l_int32 thresh, l_float32 *colvect );
l_ok pixGetColumnStats ( PIX *pixs, l_int32 type, l_int32 nbins, l_int32 thresh, l_float32 *rowvect );
l_ok pixSetPixelColumn ( PIX *pix, l_int32 col, l_float32 *colvect );
l_ok pixThresholdForFgBg ( PIX *pixs, l_int32 factor, l_int32 thresh, l_int32 *pfgval, l_int32 *pbgval );
l_ok pixSplitDistributionFgBg ( PIX *pixs, l_float32 scorefract, l_int32 factor, l_int32 *pthresh, l_int32 *pfgval, l_int32 *pbgval, PIX **ppixdb );
l_ok pixaFindDimensions ( PIXA *pixa, NUMA **pnaw, NUMA **pnah );
l_ok pixFindAreaPerimRatio ( PIX *pixs, l_int32 *tab, l_float32 *pfract );
NUMA * pixaFindPerimToAreaRatio ( PIXA *pixa );
l_ok pixFindPerimToAreaRatio ( PIX *pixs, l_int32 *tab, l_float32 *pfract );
NUMA * pixaFindPerimSizeRatio ( PIXA *pixa );
l_ok pixFindPerimSizeRatio ( PIX *pixs, l_int32 *tab, l_float32 *pratio );
NUMA * pixaFindAreaFraction ( PIXA *pixa );
l_ok pixFindAreaFraction ( PIX *pixs, l_int32 *tab, l_float32 *pfract );
NUMA * pixaFindAreaFractionMasked ( PIXA *pixa, PIX *pixm, l_int32 debug );
l_ok pixFindAreaFractionMasked ( PIX *pixs, BOX *box, PIX *pixm, l_int32 *tab, l_float32 *pfract );
NUMA * pixaFindWidthHeightRatio ( PIXA *pixa );
NUMA * pixaFindWidthHeightProduct ( PIXA *pixa );
l_ok pixFindOverlapFraction ( PIX *pixs1, PIX *pixs2, l_int32 x2, l_int32 y2, l_int32 *tab, l_float32 *pratio, l_int32 *pnoverlap );
BOXA * pixFindRectangleComps ( PIX *pixs, l_int32 dist, l_int32 minw, l_int32 minh );
l_ok pixConformsToRectangle ( PIX *pixs, BOX *box, l_int32 dist, l_int32 *pconforms );
PIXA * pixClipRectangles ( PIX *pixs, BOXA *boxa );
PIX * pixClipRectangle ( PIX *pixs, BOX *box, BOX **pboxc );
PIX * pixClipMasked ( PIX *pixs, PIX *pixm, l_int32 x, l_int32 y, l_uint32 outval );
l_ok pixCropToMatch ( PIX *pixs1, PIX *pixs2, PIX **ppixd1, PIX **ppixd2 );
PIX * pixCropToSize ( PIX *pixs, l_int32 w, l_int32 h );
PIX * pixResizeToMatch ( PIX *pixs, PIX *pixt, l_int32 w, l_int32 h );
PIX * pixSelectComponentBySize ( PIX *pixs, l_int32 rankorder, l_int32 type, l_int32 connectivity, BOX **pbox );
PIX * pixFilterComponentBySize ( PIX *pixs, l_int32 rankorder, l_int32 type, l_int32 connectivity, BOX **pbox );
PIX * pixMakeFrameMask ( l_int32 w, l_int32 h, l_float32 hf1, l_float32 hf2, l_float32 vf1, l_float32 vf2 );
PIX * pixMakeCoveringOfRectangles ( PIX *pixs, l_int32 maxiters );
l_ok pixFractionFgInMask ( PIX *pix1, PIX *pix2, l_float32 *pfract );
l_ok pixClipToForeground ( PIX *pixs, PIX **ppixd, BOX **pbox );
l_ok pixTestClipToForeground ( PIX *pixs, l_int32 *pcanclip );
l_ok pixClipBoxToForeground ( PIX *pixs, BOX *boxs, PIX **ppixd, BOX **pboxd );
l_ok pixScanForForeground ( PIX *pixs, BOX *box, l_int32 scanflag, l_int32 *ploc );
l_ok pixClipBoxToEdges ( PIX *pixs, BOX *boxs, l_int32 lowthresh, l_int32 highthresh, l_int32 maxwidth, l_int32 factor, PIX **ppixd, BOX **pboxd );
l_ok pixScanForEdge ( PIX *pixs, BOX *box, l_int32 lowthresh, l_int32 highthresh, l_int32 maxwidth, l_int32 factor, l_int32 scanflag, l_int32 *ploc );
NUMA * pixExtractOnLine ( PIX *pixs, l_int32 x1, l_int32 y1, l_int32 x2, l_int32 y2, l_int32 factor );
l_float32 pixAverageOnLine ( PIX *pixs, l_int32 x1, l_int32 y1, l_int32 x2, l_int32 y2, l_int32 factor );
NUMA * pixAverageIntensityProfile ( PIX *pixs, l_float32 fract, l_int32 dir, l_int32 first, l_int32 last, l_int32 factor1, l_int32 factor2 );
NUMA * pixReversalProfile ( PIX *pixs, l_float32 fract, l_int32 dir, l_int32 first, l_int32 last, l_int32 minreversal, l_int32 factor1, l_int32 factor2 );
l_ok pixWindowedVarianceOnLine ( PIX *pixs, l_int32 dir, l_int32 loc, l_int32 c1, l_int32 c2, l_int32 size, NUMA **pnad );
l_ok pixMinMaxNearLine ( PIX *pixs, l_int32 x1, l_int32 y1, l_int32 x2, l_int32 y2, l_int32 dist, l_int32 direction, NUMA **pnamin, NUMA **pnamax, l_float32 *pminave, l_float32 *pmaxave );
PIX * pixRankRowTransform ( PIX *pixs );
PIX * pixRankColumnTransform ( PIX *pixs );
PIXA * pixaCreate ( l_int32 n );
PIXA * pixaCreateFromPix ( PIX *pixs, l_int32 n, l_int32 cellw, l_int32 cellh );
PIXA * pixaCreateFromBoxa ( PIX *pixs, BOXA *boxa, l_int32 start, l_int32 num, l_int32 *pcropwarn );
PIXA * pixaSplitPix ( PIX *pixs, l_int32 nx, l_int32 ny, l_int32 borderwidth, l_uint32 bordercolor );
void pixaDestroy ( PIXA **ppixa );
PIXA * pixaCopy ( PIXA *pixa, l_int32 copyflag );
l_ok pixaAddPix ( PIXA *pixa, PIX *pix, l_int32 copyflag );
l_ok pixaAddBox ( PIXA *pixa, BOX *box, l_int32 copyflag );
l_ok pixaExtendArrayToSize ( PIXA *pixa, l_int32 size );
l_int32 pixaGetCount ( PIXA *pixa );
l_ok pixaChangeRefcount ( PIXA *pixa, l_int32 delta );
PIX * pixaGetPix ( PIXA *pixa, l_int32 index, l_int32 accesstype );
l_ok pixaGetPixDimensions ( PIXA *pixa, l_int32 index, l_int32 *pw, l_int32 *ph, l_int32 *pd );
BOXA * pixaGetBoxa ( PIXA *pixa, l_int32 accesstype );
l_int32 pixaGetBoxaCount ( PIXA *pixa );
BOX * pixaGetBox ( PIXA *pixa, l_int32 index, l_int32 accesstype );
l_ok pixaGetBoxGeometry ( PIXA *pixa, l_int32 index, l_int32 *px, l_int32 *py, l_int32 *pw, l_int32 *ph );
l_ok pixaSetBoxa ( PIXA *pixa, BOXA *boxa, l_int32 accesstype );
PIX ** pixaGetPixArray ( PIXA *pixa );
l_ok pixaVerifyDepth ( PIXA *pixa, l_int32 *psame, l_int32 *pmaxd );
l_ok pixaVerifyDimensions ( PIXA *pixa, l_int32 *psame, l_int32 *pmaxw, l_int32 *pmaxh );
l_ok pixaIsFull ( PIXA *pixa, l_int32 *pfullpa, l_int32 *pfullba );
l_ok pixaCountText ( PIXA *pixa, l_int32 *pntext );
l_ok pixaSetText ( PIXA *pixa, const char *text, SARRAY *sa );
void *** pixaGetLinePtrs ( PIXA *pixa, l_int32 *psize );
l_ok pixaWriteStreamInfo ( FILE *fp, PIXA *pixa );
l_ok pixaReplacePix ( PIXA *pixa, l_int32 index, PIX *pix, BOX *box );
l_ok pixaInsertPix ( PIXA *pixa, l_int32 index, PIX *pixs, BOX *box );
l_ok pixaRemovePix ( PIXA *pixa, l_int32 index );
l_ok pixaRemovePixAndSave ( PIXA *pixa, l_int32 index, PIX **ppix, BOX **pbox );
l_ok pixaRemoveSelected ( PIXA *pixa, NUMA *naindex );
l_ok pixaInitFull ( PIXA *pixa, PIX *pix, BOX *box );
l_ok pixaClear ( PIXA *pixa );
l_ok pixaJoin ( PIXA *pixad, PIXA *pixas, l_int32 istart, l_int32 iend );
PIXA * pixaInterleave ( PIXA *pixa1, PIXA *pixa2, l_int32 copyflag );
l_ok pixaaJoin ( PIXAA *paad, PIXAA *paas, l_int32 istart, l_int32 iend );
PIXAA * pixaaCreate ( l_int32 n );
PIXAA * pixaaCreateFromPixa ( PIXA *pixa, l_int32 n, l_int32 type, l_int32 copyflag );
void pixaaDestroy ( PIXAA **ppaa );
l_ok pixaaAddPixa ( PIXAA *paa, PIXA *pixa, l_int32 copyflag );
l_ok pixaaExtendArray ( PIXAA *paa );
l_ok pixaaAddPix ( PIXAA *paa, l_int32 index, PIX *pix, BOX *box, l_int32 copyflag );
l_ok pixaaAddBox ( PIXAA *paa, BOX *box, l_int32 copyflag );
l_int32 pixaaGetCount ( PIXAA *paa, NUMA **pna );
PIXA * pixaaGetPixa ( PIXAA *paa, l_int32 index, l_int32 accesstype );
BOXA * pixaaGetBoxa ( PIXAA *paa, l_int32 accesstype );
PIX * pixaaGetPix ( PIXAA *paa, l_int32 index, l_int32 ipix, l_int32 accessflag );
l_ok pixaaVerifyDepth ( PIXAA *paa, l_int32 *psame, l_int32 *pmaxd );
l_ok pixaaVerifyDimensions ( PIXAA *paa, l_int32 *psame, l_int32 *pmaxw, l_int32 *pmaxh );
l_int32 pixaaIsFull ( PIXAA *paa, l_int32 *pfull );
l_ok pixaaInitFull ( PIXAA *paa, PIXA *pixa );
l_ok pixaaReplacePixa ( PIXAA *paa, l_int32 index, PIXA *pixa );
l_ok pixaaClear ( PIXAA *paa );
l_ok pixaaTruncate ( PIXAA *paa );
PIXA * pixaRead ( const char *filename );
PIXA * pixaReadStream ( FILE *fp );
PIXA * pixaReadMem ( const l_uint8 *data, size_t size );
l_ok pixaWriteDebug ( const char *fname, PIXA *pixa );
l_ok pixaWrite ( const char *filename, PIXA *pixa );
l_ok pixaWriteStream ( FILE *fp, PIXA *pixa );
l_ok pixaWriteMem ( l_uint8 **pdata, size_t *psize, PIXA *pixa );
PIXA * pixaReadBoth ( const char *filename );
PIXAA * pixaaReadFromFiles ( const char *dirname, const char *substr, l_int32 first, l_int32 nfiles );
PIXAA * pixaaRead ( const char *filename );
PIXAA * pixaaReadStream ( FILE *fp );
PIXAA * pixaaReadMem ( const l_uint8 *data, size_t size );
l_ok pixaaWrite ( const char *filename, PIXAA *paa );
l_ok pixaaWriteStream ( FILE *fp, PIXAA *paa );
l_ok pixaaWriteMem ( l_uint8 **pdata, size_t *psize, PIXAA *paa );
PIXACC * pixaccCreate ( l_int32 w, l_int32 h, l_int32 negflag );
PIXACC * pixaccCreateFromPix ( PIX *pix, l_int32 negflag );
void pixaccDestroy ( PIXACC **ppixacc );
PIX * pixaccFinal ( PIXACC *pixacc, l_int32 outdepth );
PIX * pixaccGetPix ( PIXACC *pixacc );
l_int32 pixaccGetOffset ( PIXACC *pixacc );
l_ok pixaccAdd ( PIXACC *pixacc, PIX *pix );
l_ok pixaccSubtract ( PIXACC *pixacc, PIX *pix );
l_ok pixaccMultConst ( PIXACC *pixacc, l_float32 factor );
l_ok pixaccMultConstAccumulate ( PIXACC *pixacc, PIX *pix, l_float32 factor );
PIX * pixSelectBySize ( PIX *pixs, l_int32 width, l_int32 height, l_int32 connectivity, l_int32 type, l_int32 relation, l_int32 *pchanged );
PIXA * pixaSelectBySize ( PIXA *pixas, l_int32 width, l_int32 height, l_int32 type, l_int32 relation, l_int32 *pchanged );
NUMA * pixaMakeSizeIndicator ( PIXA *pixa, l_int32 width, l_int32 height, l_int32 type, l_int32 relation );
PIX * pixSelectByPerimToAreaRatio ( PIX *pixs, l_float32 thresh, l_int32 connectivity, l_int32 type, l_int32 *pchanged );
PIXA * pixaSelectByPerimToAreaRatio ( PIXA *pixas, l_float32 thresh, l_int32 type, l_int32 *pchanged );
PIX * pixSelectByPerimSizeRatio ( PIX *pixs, l_float32 thresh, l_int32 connectivity, l_int32 type, l_int32 *pchanged );
PIXA * pixaSelectByPerimSizeRatio ( PIXA *pixas, l_float32 thresh, l_int32 type, l_int32 *pchanged );
PIX * pixSelectByAreaFraction ( PIX *pixs, l_float32 thresh, l_int32 connectivity, l_int32 type, l_int32 *pchanged );
PIXA * pixaSelectByAreaFraction ( PIXA *pixas, l_float32 thresh, l_int32 type, l_int32 *pchanged );
PIX * pixSelectByWidthHeightRatio ( PIX *pixs, l_float32 thresh, l_int32 connectivity, l_int32 type, l_int32 *pchanged );
PIXA * pixaSelectByWidthHeightRatio ( PIXA *pixas, l_float32 thresh, l_int32 type, l_int32 *pchanged );
PIXA * pixaSelectByNumConnComp ( PIXA *pixas, l_int32 nmin, l_int32 nmax, l_int32 connectivity, l_int32 *pchanged );
PIXA * pixaSelectWithIndicator ( PIXA *pixas, NUMA *na, l_int32 *pchanged );
l_ok pixRemoveWithIndicator ( PIX *pixs, PIXA *pixa, NUMA *na );
l_ok pixAddWithIndicator ( PIX *pixs, PIXA *pixa, NUMA *na );
PIXA * pixaSelectWithString ( PIXA *pixas, const char *str, l_int32 *perror );
PIX * pixaRenderComponent ( PIX *pixs, PIXA *pixa, l_int32 index );
PIXA * pixaSort ( PIXA *pixas, l_int32 sorttype, l_int32 sortorder, NUMA **pnaindex, l_int32 copyflag );
PIXA * pixaBinSort ( PIXA *pixas, l_int32 sorttype, l_int32 sortorder, NUMA **pnaindex, l_int32 copyflag );
PIXA * pixaSortByIndex ( PIXA *pixas, NUMA *naindex, l_int32 copyflag );
PIXAA * pixaSort2dByIndex ( PIXA *pixas, NUMAA *naa, l_int32 copyflag );
PIXA * pixaSelectRange ( PIXA *pixas, l_int32 first, l_int32 last, l_int32 copyflag );
PIXAA * pixaaSelectRange ( PIXAA *paas, l_int32 first, l_int32 last, l_int32 copyflag );
PIXAA * pixaaScaleToSize ( PIXAA *paas, l_int32 wd, l_int32 hd );
PIXAA * pixaaScaleToSizeVar ( PIXAA *paas, NUMA *nawd, NUMA *nahd );
PIXA * pixaScaleToSize ( PIXA *pixas, l_int32 wd, l_int32 hd );
PIXA * pixaScaleToSizeRel ( PIXA *pixas, l_int32 delw, l_int32 delh );
PIXA * pixaScale ( PIXA *pixas, l_float32 scalex, l_float32 scaley );
PIXA * pixaScaleBySampling ( PIXA *pixas, l_float32 scalex, l_float32 scaley );
PIXA * pixaRotate ( PIXA *pixas, l_float32 angle, l_int32 type, l_int32 incolor, l_int32 width, l_int32 height );
PIXA * pixaRotateOrth ( PIXA *pixas, l_int32 rotation );
PIXA * pixaTranslate ( PIXA *pixas, l_int32 hshift, l_int32 vshift, l_int32 incolor );
PIXA * pixaAddBorderGeneral ( PIXA *pixad, PIXA *pixas, l_int32 left, l_int32 right, l_int32 top, l_int32 bot, l_uint32 val );
PIXA * pixaaFlattenToPixa ( PIXAA *paa, NUMA **pnaindex, l_int32 copyflag );
l_ok pixaaSizeRange ( PIXAA *paa, l_int32 *pminw, l_int32 *pminh, l_int32 *pmaxw, l_int32 *pmaxh );
l_ok pixaSizeRange ( PIXA *pixa, l_int32 *pminw, l_int32 *pminh, l_int32 *pmaxw, l_int32 *pmaxh );
PIXA * pixaClipToPix ( PIXA *pixas, PIX *pixs );
l_ok pixaClipToForeground ( PIXA *pixas, PIXA **ppixad, BOXA **pboxa );
l_ok pixaGetRenderingDepth ( PIXA *pixa, l_int32 *pdepth );
l_ok pixaHasColor ( PIXA *pixa, l_int32 *phascolor );
l_ok pixaAnyColormaps ( PIXA *pixa, l_int32 *phascmap );
l_ok pixaGetDepthInfo ( PIXA *pixa, l_int32 *pmaxdepth, l_int32 *psame );
PIXA * pixaConvertToSameDepth ( PIXA *pixas );
l_ok pixaEqual ( PIXA *pixa1, PIXA *pixa2, l_int32 maxdist, NUMA **pnaindex, l_int32 *psame );
l_ok pixaSetFullSizeBoxa ( PIXA *pixa );
PIX * pixaDisplay ( PIXA *pixa, l_int32 w, l_int32 h );
PIX * pixaDisplayOnColor ( PIXA *pixa, l_int32 w, l_int32 h, l_uint32 bgcolor );
PIX * pixaDisplayRandomCmap ( PIXA *pixa, l_int32 w, l_int32 h );
PIX * pixaDisplayLinearly ( PIXA *pixas, l_int32 direction, l_float32 scalefactor, l_int32 background, l_int32 spacing, l_int32 border, BOXA **pboxa );
PIX * pixaDisplayOnLattice ( PIXA *pixa, l_int32 cellw, l_int32 cellh, l_int32 *pncols, BOXA **pboxa );
PIX * pixaDisplayUnsplit ( PIXA *pixa, l_int32 nx, l_int32 ny, l_int32 borderwidth, l_uint32 bordercolor );
PIX * pixaDisplayTiled ( PIXA *pixa, l_int32 maxwidth, l_int32 background, l_int32 spacing );
PIX * pixaDisplayTiledInRows ( PIXA *pixa, l_int32 outdepth, l_int32 maxwidth, l_float32 scalefactor, l_int32 background, l_int32 spacing, l_int32 border );
PIX * pixaDisplayTiledInColumns ( PIXA *pixas, l_int32 nx, l_float32 scalefactor, l_int32 spacing, l_int32 border );
PIX * pixaDisplayTiledAndScaled ( PIXA *pixa, l_int32 outdepth, l_int32 tilewidth, l_int32 ncols, l_int32 background, l_int32 spacing, l_int32 border );
PIX * pixaDisplayTiledWithText ( PIXA *pixa, l_int32 maxwidth, l_float32 scalefactor, l_int32 spacing, l_int32 border, l_int32 fontsize, l_uint32 textcolor );
PIX * pixaDisplayTiledByIndex ( PIXA *pixa, NUMA *na, l_int32 width, l_int32 spacing, l_int32 border, l_int32 fontsize, l_uint32 textcolor );
PIX * pixaaDisplay ( PIXAA *paa, l_int32 w, l_int32 h );
PIX * pixaaDisplayByPixa ( PIXAA *paa, l_int32 xspace, l_int32 yspace, l_int32 maxw );
PIXA * pixaaDisplayTiledAndScaled ( PIXAA *paa, l_int32 outdepth, l_int32 tilewidth, l_int32 ncols, l_int32 background, l_int32 spacing, l_int32 border );
PIXA * pixaConvertTo1 ( PIXA *pixas, l_int32 thresh );
PIXA * pixaConvertTo8 ( PIXA *pixas, l_int32 cmapflag );
PIXA * pixaConvertTo8Colormap ( PIXA *pixas, l_int32 dither );
PIXA * pixaConvertTo32 ( PIXA *pixas );
PIXA * pixaConstrainedSelect ( PIXA *pixas, l_int32 first, l_int32 last, l_int32 nmax, l_int32 use_pairs, l_int32 copyflag );
l_ok pixaSelectToPdf ( PIXA *pixas, l_int32 first, l_int32 last, l_int32 res, l_float32 scalefactor, l_int32 type, l_int32 quality, l_uint32 color, l_int32 fontsize, const char *fileout );
PIXA * pixaMakeFromTiledPixa ( PIXA *pixas, l_int32 w, l_int32 h, l_int32 nsamp );
PIXA * pixaMakeFromTiledPix ( PIX *pixs, l_int32 w, l_int32 h, l_int32 start, l_int32 num, BOXA *boxa );
l_ok pixGetTileCount ( PIX *pix, l_int32 *pn );
PIXA * pixaDisplayMultiTiled ( PIXA *pixas, l_int32 nx, l_int32 ny, l_int32 maxw, l_int32 maxh, l_float32 scalefactor, l_int32 spacing, l_int32 border );
l_ok pixaSplitIntoFiles ( PIXA *pixas, l_int32 nsplit, l_float32 scale, l_int32 outwidth, l_int32 write_pixa, l_int32 write_pix, l_int32 write_pdf );
l_ok convertToNUpFiles ( const char *dir, const char *substr, l_int32 nx, l_int32 ny, l_int32 tw, l_int32 spacing, l_int32 border, l_int32 fontsize, const char *outdir );
PIXA * convertToNUpPixa ( const char *dir, const char *substr, l_int32 nx, l_int32 ny, l_int32 tw, l_int32 spacing, l_int32 border, l_int32 fontsize );
PIXA * pixaConvertToNUpPixa ( PIXA *pixas, SARRAY *sa, l_int32 nx, l_int32 ny, l_int32 tw, l_int32 spacing, l_int32 border, l_int32 fontsize );
l_ok pixaCompareInPdf ( PIXA *pixa1, PIXA *pixa2, l_int32 nx, l_int32 ny, l_int32 tw, l_int32 spacing, l_int32 border, l_int32 fontsize, const char *fileout );
l_ok pmsCreate ( size_t minsize, size_t smallest, NUMA *numalloc, const char *logfile );
void pmsDestroy (  );
void * pmsCustomAlloc ( size_t nbytes );
void pmsCustomDealloc ( void *data );
void * pmsGetAlloc ( size_t nbytes );
l_ok pmsGetLevelForAlloc ( size_t nbytes, l_int32 *plevel );
l_ok pmsGetLevelForDealloc ( void *data, l_int32 *plevel );
void pmsLogInfo (  );
l_ok pixAddConstantGray ( PIX *pixs, l_int32 val );
l_ok pixMultConstantGray ( PIX *pixs, l_float32 val );
PIX * pixAddGray ( PIX *pixd, PIX *pixs1, PIX *pixs2 );
PIX * pixSubtractGray ( PIX *pixd, PIX *pixs1, PIX *pixs2 );
PIX * pixThresholdToValue ( PIX *pixd, PIX *pixs, l_int32 threshval, l_int32 setval );
PIX * pixInitAccumulate ( l_int32 w, l_int32 h, l_uint32 offset );
PIX * pixFinalAccumulate ( PIX *pixs, l_uint32 offset, l_int32 depth );
PIX * pixFinalAccumulateThreshold ( PIX *pixs, l_uint32 offset, l_uint32 threshold );
l_ok pixAccumulate ( PIX *pixd, PIX *pixs, l_int32 op );
l_ok pixMultConstAccumulate ( PIX *pixs, l_float32 factor, l_uint32 offset );
PIX * pixAbsDifference ( PIX *pixs1, PIX *pixs2 );
PIX * pixAddRGB ( PIX *pixs1, PIX *pixs2 );
PIX * pixMinOrMax ( PIX *pixd, PIX *pixs1, PIX *pixs2, l_int32 type );
PIX * pixMaxDynamicRange ( PIX *pixs, l_int32 type );
PIX * pixMaxDynamicRangeRGB ( PIX *pixs, l_int32 type );
l_uint32 linearScaleRGBVal ( l_uint32 sval, l_float32 factor );
l_uint32 logScaleRGBVal ( l_uint32 sval, l_float32 *tab, l_float32 factor );
l_float32 * makeLogBase2Tab ( void );
l_float32 getLogBase2 ( l_int32 val, l_float32 *logtab );
PIXC * pixcompCreateFromPix ( PIX *pix, l_int32 comptype );
PIXC * pixcompCreateFromString ( l_uint8 *data, size_t size, l_int32 copyflag );
PIXC * pixcompCreateFromFile ( const char *filename, l_int32 comptype );
void pixcompDestroy ( PIXC **ppixc );
PIXC * pixcompCopy ( PIXC *pixcs );
l_ok pixcompGetDimensions ( PIXC *pixc, l_int32 *pw, l_int32 *ph, l_int32 *pd );
l_ok pixcompGetParameters ( PIXC *pixc, l_int32 *pxres, l_int32 *pyres, l_int32 *pcomptype, l_int32 *pcmapflag );
l_ok pixcompDetermineFormat ( l_int32 comptype, l_int32 d, l_int32 cmapflag, l_int32 *pformat );
PIX * pixCreateFromPixcomp ( PIXC *pixc );
PIXAC * pixacompCreate ( l_int32 n );
PIXAC * pixacompCreateWithInit ( l_int32 n, l_int32 offset, PIX *pix, l_int32 comptype );
PIXAC * pixacompCreateFromPixa ( PIXA *pixa, l_int32 comptype, l_int32 accesstype );
PIXAC * pixacompCreateFromFiles ( const char *dirname, const char *substr, l_int32 comptype );
PIXAC * pixacompCreateFromSA ( SARRAY *sa, l_int32 comptype );
void pixacompDestroy ( PIXAC **ppixac );
l_ok pixacompAddPix ( PIXAC *pixac, PIX *pix, l_int32 comptype );
l_ok pixacompAddPixcomp ( PIXAC *pixac, PIXC *pixc, l_int32 copyflag );
l_ok pixacompReplacePix ( PIXAC *pixac, l_int32 index, PIX *pix, l_int32 comptype );
l_ok pixacompReplacePixcomp ( PIXAC *pixac, l_int32 index, PIXC *pixc );
l_ok pixacompAddBox ( PIXAC *pixac, BOX *box, l_int32 copyflag );
l_int32 pixacompGetCount ( PIXAC *pixac );
PIXC * pixacompGetPixcomp ( PIXAC *pixac, l_int32 index, l_int32 copyflag );
PIX * pixacompGetPix ( PIXAC *pixac, l_int32 index );
l_ok pixacompGetPixDimensions ( PIXAC *pixac, l_int32 index, l_int32 *pw, l_int32 *ph, l_int32 *pd );
BOXA * pixacompGetBoxa ( PIXAC *pixac, l_int32 accesstype );
l_int32 pixacompGetBoxaCount ( PIXAC *pixac );
BOX * pixacompGetBox ( PIXAC *pixac, l_int32 index, l_int32 accesstype );
l_ok pixacompGetBoxGeometry ( PIXAC *pixac, l_int32 index, l_int32 *px, l_int32 *py, l_int32 *pw, l_int32 *ph );
l_int32 pixacompGetOffset ( PIXAC *pixac );
l_ok pixacompSetOffset ( PIXAC *pixac, l_int32 offset );
PIXA * pixaCreateFromPixacomp ( PIXAC *pixac, l_int32 accesstype );
l_ok pixacompJoin ( PIXAC *pixacd, PIXAC *pixacs, l_int32 istart, l_int32 iend );
PIXAC * pixacompInterleave ( PIXAC *pixac1, PIXAC *pixac2 );
PIXAC * pixacompRead ( const char *filename );
PIXAC * pixacompReadStream ( FILE *fp );
PIXAC * pixacompReadMem ( const l_uint8 *data, size_t size );
l_ok pixacompWrite ( const char *filename, PIXAC *pixac );
l_ok pixacompWriteStream ( FILE *fp, PIXAC *pixac );
l_ok pixacompWriteMem ( l_uint8 **pdata, size_t *psize, PIXAC *pixac );
l_ok pixacompConvertToPdf ( PIXAC *pixac, l_int32 res, l_float32 scalefactor, l_int32 type, l_int32 quality, const char *title, const char *fileout );
l_ok pixacompConvertToPdfData ( PIXAC *pixac, l_int32 res, l_float32 scalefactor, l_int32 type, l_int32 quality, const char *title, l_uint8 **pdata, size_t *pnbytes );
l_ok pixacompFastConvertToPdfData ( PIXAC *pixac, const char *title, l_uint8 **pdata, size_t *pnbytes );
l_ok pixacompWriteStreamInfo ( FILE *fp, PIXAC *pixac, const char *text );
l_ok pixcompWriteStreamInfo ( FILE *fp, PIXC *pixc, const char *text );
PIX * pixacompDisplayTiledAndScaled ( PIXAC *pixac, l_int32 outdepth, l_int32 tilewidth, l_int32 ncols, l_int32 background, l_int32 spacing, l_int32 border );
l_ok pixacompWriteFiles ( PIXAC *pixac, const char *subdir );
l_ok pixcompWriteFile ( const char *rootname, PIXC *pixc );
PIX * pixThreshold8 ( PIX *pixs, l_int32 d, l_int32 nlevels, l_int32 cmapflag );
PIX * pixRemoveColormapGeneral ( PIX *pixs, l_int32 type, l_int32 ifnocmap );
PIX * pixRemoveColormap ( PIX *pixs, l_int32 type );
l_ok pixAddGrayColormap8 ( PIX *pixs );
PIX * pixAddMinimalGrayColormap8 ( PIX *pixs );
PIX * pixConvertRGBToLuminance ( PIX *pixs );
PIX * pixConvertRGBToGray ( PIX *pixs, l_float32 rwt, l_float32 gwt, l_float32 bwt );
PIX * pixConvertRGBToGrayFast ( PIX *pixs );
PIX * pixConvertRGBToGrayMinMax ( PIX *pixs, l_int32 type );
PIX * pixConvertRGBToGraySatBoost ( PIX *pixs, l_int32 refval );
PIX * pixConvertRGBToGrayArb ( PIX *pixs, l_float32 rc, l_float32 gc, l_float32 bc );
PIX * pixConvertRGBToBinaryArb ( PIX *pixs, l_float32 rc, l_float32 gc, l_float32 bc, l_int32 thresh, l_int32 relation );
PIX * pixConvertGrayToColormap ( PIX *pixs );
PIX * pixConvertGrayToColormap8 ( PIX *pixs, l_int32 mindepth );
PIX * pixColorizeGray ( PIX *pixs, l_uint32 color, l_int32 cmapflag );
PIX * pixConvertRGBToColormap ( PIX *pixs, l_int32 ditherflag );
PIX * pixConvertCmapTo1 ( PIX *pixs );
l_ok pixQuantizeIfFewColors ( PIX *pixs, l_int32 maxcolors, l_int32 mingraycolors, l_int32 octlevel, PIX **ppixd );
PIX * pixConvert16To8 ( PIX *pixs, l_int32 type );
PIX * pixConvertGrayToFalseColor ( PIX *pixs, l_float32 gamma );
PIX * pixUnpackBinary ( PIX *pixs, l_int32 depth, l_int32 invert );
PIX * pixConvert1To16 ( PIX *pixd, PIX *pixs, l_uint16 val0, l_uint16 val1 );
PIX * pixConvert1To32 ( PIX *pixd, PIX *pixs, l_uint32 val0, l_uint32 val1 );
PIX * pixConvert1To2Cmap ( PIX *pixs );
PIX * pixConvert1To2 ( PIX *pixd, PIX *pixs, l_int32 val0, l_int32 val1 );
PIX * pixConvert1To4Cmap ( PIX *pixs );
PIX * pixConvert1To4 ( PIX *pixd, PIX *pixs, l_int32 val0, l_int32 val1 );
PIX * pixConvert1To8Cmap ( PIX *pixs );
PIX * pixConvert1To8 ( PIX *pixd, PIX *pixs, l_uint8 val0, l_uint8 val1 );
PIX * pixConvert2To8 ( PIX *pixs, l_uint8 val0, l_uint8 val1, l_uint8 val2, l_uint8 val3, l_int32 cmapflag );
PIX * pixConvert4To8 ( PIX *pixs, l_int32 cmapflag );
PIX * pixConvert8To16 ( PIX *pixs, l_int32 leftshift );
PIX * pixConvertTo2 ( PIX *pixs );
PIX * pixConvert8To2 ( PIX *pix );
PIX * pixConvertTo4 ( PIX *pixs );
PIX * pixConvert8To4 ( PIX *pix );
PIX * pixConvertTo1 ( PIX *pixs, l_int32 threshold );
PIX * pixConvertTo1BySampling ( PIX *pixs, l_int32 factor, l_int32 threshold );
PIX * pixConvertTo8 ( PIX *pixs, l_int32 cmapflag );
PIX * pixConvertTo8BySampling ( PIX *pixs, l_int32 factor, l_int32 cmapflag );
PIX * pixConvertTo8Colormap ( PIX *pixs, l_int32 dither );
PIX * pixConvertTo16 ( PIX *pixs );
PIX * pixConvertTo32 ( PIX *pixs );
PIX * pixConvertTo32BySampling ( PIX *pixs, l_int32 factor );
PIX * pixConvert8To32 ( PIX *pixs );
PIX * pixConvertTo8Or32 ( PIX *pixs, l_int32 copyflag, l_int32 warnflag );
PIX * pixConvert24To32 ( PIX *pixs );
PIX * pixConvert32To24 ( PIX *pixs );
PIX * pixConvert32To16 ( PIX *pixs, l_int32 type );
PIX * pixConvert32To8 ( PIX *pixs, l_int32 type16, l_int32 type8 );
PIX * pixRemoveAlpha ( PIX *pixs );
PIX * pixAddAlphaTo1bpp ( PIX *pixd, PIX *pixs );
PIX * pixConvertLossless ( PIX *pixs, l_int32 d );
PIX * pixConvertForPSWrap ( PIX *pixs );
PIX * pixConvertToSubpixelRGB ( PIX *pixs, l_float32 scalex, l_float32 scaley, l_int32 order );
PIX * pixConvertGrayToSubpixelRGB ( PIX *pixs, l_float32 scalex, l_float32 scaley, l_int32 order );
PIX * pixConvertColorToSubpixelRGB ( PIX *pixs, l_float32 scalex, l_float32 scaley, l_int32 order );
void l_setNeutralBoostVal ( l_int32 val );
PIX * pixConnCompTransform ( PIX *pixs, l_int32 connect, l_int32 depth );
PIX * pixConnCompAreaTransform ( PIX *pixs, l_int32 connect );
l_ok pixConnCompIncrInit ( PIX *pixs, l_int32 conn, PIX **ppixd, PTAA **pptaa, l_int32 *pncc );
l_int32 pixConnCompIncrAdd ( PIX *pixs, PTAA *ptaa, l_int32 *pncc, l_float32 x, l_float32 y, l_int32 debug );
l_ok pixGetSortedNeighborValues ( PIX *pixs, l_int32 x, l_int32 y, l_int32 conn, l_int32 **pneigh, l_int32 *pnvals );
PIX * pixLocToColorTransform ( PIX *pixs );
PIXTILING * pixTilingCreate ( PIX *pixs, l_int32 nx, l_int32 ny, l_int32 w, l_int32 h, l_int32 xoverlap, l_int32 yoverlap );
void pixTilingDestroy ( PIXTILING **ppt );
l_ok pixTilingGetCount ( PIXTILING *pt, l_int32 *pnx, l_int32 *pny );
l_ok pixTilingGetSize ( PIXTILING *pt, l_int32 *pw, l_int32 *ph );
PIX * pixTilingGetTile ( PIXTILING *pt, l_int32 i, l_int32 j );
l_ok pixTilingNoStripOnPaint ( PIXTILING *pt );
l_ok pixTilingPaintTile ( PIX *pixd, l_int32 i, l_int32 j, PIX *pixs, PIXTILING *pt );
PIX * pixReadStreamPng ( FILE *fp );
l_ok readHeaderPng ( const char *filename, l_int32 *pw, l_int32 *ph, l_int32 *pbps, l_int32 *pspp, l_int32 *piscmap );
l_ok freadHeaderPng ( FILE *fp, l_int32 *pw, l_int32 *ph, l_int32 *pbps, l_int32 *pspp, l_int32 *piscmap );
l_ok readHeaderMemPng ( const l_uint8 *data, size_t size, l_int32 *pw, l_int32 *ph, l_int32 *pbps, l_int32 *pspp, l_int32 *piscmap );
l_int32 fgetPngResolution ( FILE *fp, l_int32 *pxres, l_int32 *pyres );
l_ok isPngInterlaced ( const char *filename, l_int32 *pinterlaced );
l_ok fgetPngColormapInfo ( FILE *fp, PIXCMAP **pcmap, l_int32 *ptransparency );
l_ok pixWritePng ( const char *filename, PIX *pix, l_float32 gamma );
l_ok pixWriteStreamPng ( FILE *fp, PIX *pix, l_float32 gamma );
l_ok pixSetZlibCompression ( PIX *pix, l_int32 compval );
void l_pngSetReadStrip16To8 ( l_int32 flag );
PIX * pixReadMemPng ( const l_uint8 *filedata, size_t filesize );
l_ok pixWriteMemPng ( l_uint8 **pfiledata, size_t *pfilesize, PIX *pix, l_float32 gamma );
PIX * pixReadStreamPnm ( FILE *fp );
l_ok readHeaderPnm ( const char *filename, l_int32 *pw, l_int32 *ph, l_int32 *pd, l_int32 *ptype, l_int32 *pbps, l_int32 *pspp );
l_ok freadHeaderPnm ( FILE *fp, l_int32 *pw, l_int32 *ph, l_int32 *pd, l_int32 *ptype, l_int32 *pbps, l_int32 *pspp );
l_ok pixWriteStreamPnm ( FILE *fp, PIX *pix );
l_ok pixWriteStreamAsciiPnm ( FILE *fp, PIX *pix );
l_ok pixWriteStreamPam ( FILE *fp, PIX *pix );
PIX * pixReadMemPnm ( const l_uint8 *data, size_t size );
l_ok readHeaderMemPnm ( const l_uint8 *data, size_t size, l_int32 *pw, l_int32 *ph, l_int32 *pd, l_int32 *ptype, l_int32 *pbps, l_int32 *pspp );
l_ok pixWriteMemPnm ( l_uint8 **pdata, size_t *psize, PIX *pix );
l_ok pixWriteMemPam ( l_uint8 **pdata, size_t *psize, PIX *pix );
PIX * pixProjectiveSampledPta ( PIX *pixs, PTA *ptad, PTA *ptas, l_int32 incolor );
PIX * pixProjectiveSampled ( PIX *pixs, l_float32 *vc, l_int32 incolor );
PIX * pixProjectivePta ( PIX *pixs, PTA *ptad, PTA *ptas, l_int32 incolor );
PIX * pixProjective ( PIX *pixs, l_float32 *vc, l_int32 incolor );
PIX * pixProjectivePtaColor ( PIX *pixs, PTA *ptad, PTA *ptas, l_uint32 colorval );
PIX * pixProjectiveColor ( PIX *pixs, l_float32 *vc, l_uint32 colorval );
PIX * pixProjectivePtaGray ( PIX *pixs, PTA *ptad, PTA *ptas, l_uint8 grayval );
PIX * pixProjectiveGray ( PIX *pixs, l_float32 *vc, l_uint8 grayval );
PIX * pixProjectivePtaWithAlpha ( PIX *pixs, PTA *ptad, PTA *ptas, PIX *pixg, l_float32 fract, l_int32 border );
l_ok getProjectiveXformCoeffs ( PTA *ptas, PTA *ptad, l_float32 **pvc );
l_ok projectiveXformSampledPt ( l_float32 *vc, l_int32 x, l_int32 y, l_int32 *pxp, l_int32 *pyp );
l_ok projectiveXformPt ( l_float32 *vc, l_int32 x, l_int32 y, l_float32 *pxp, l_float32 *pyp );
l_ok convertFilesToPS ( const char *dirin, const char *substr, l_int32 res, const char *fileout );
l_ok sarrayConvertFilesToPS ( SARRAY *sa, l_int32 res, const char *fileout );
l_ok convertFilesFittedToPS ( const char *dirin, const char *substr, l_float32 xpts, l_float32 ypts, const char *fileout );
l_ok sarrayConvertFilesFittedToPS ( SARRAY *sa, l_float32 xpts, l_float32 ypts, const char *fileout );
l_ok writeImageCompressedToPSFile ( const char *filein, const char *fileout, l_int32 res, l_int32 *pfirstfile, l_int32 *pindex );
l_ok convertSegmentedPagesToPS ( const char *pagedir, const char *pagestr, l_int32 page_numpre, const char *maskdir, const char *maskstr, l_int32 mask_numpre, l_int32 numpost, l_int32 maxnum, l_float32 textscale, l_float32 imagescale, l_int32 threshold, const char *fileout );
l_ok pixWriteSegmentedPageToPS ( PIX *pixs, PIX *pixm, l_float32 textscale, l_float32 imagescale, l_int32 threshold, l_int32 pageno, const char *fileout );
l_ok pixWriteMixedToPS ( PIX *pixb, PIX *pixc, l_float32 scale, l_int32 pageno, const char *fileout );
l_ok convertToPSEmbed ( const char *filein, const char *fileout, l_int32 level );
l_ok pixaWriteCompressedToPS ( PIXA *pixa, const char *fileout, l_int32 res, l_int32 level );
l_ok pixWritePSEmbed ( const char *filein, const char *fileout );
l_ok pixWriteStreamPS ( FILE *fp, PIX *pix, BOX *box, l_int32 res, l_float32 scale );
char * pixWriteStringPS ( PIX *pixs, BOX *box, l_int32 res, l_float32 scale );
char * generateUncompressedPS ( char *hexdata, l_int32 w, l_int32 h, l_int32 d, l_int32 psbpl, l_int32 bps, l_float32 xpt, l_float32 ypt, l_float32 wpt, l_float32 hpt, l_int32 boxflag );
void getScaledParametersPS ( BOX *box, l_int32 wpix, l_int32 hpix, l_int32 res, l_float32 scale, l_float32 *pxpt, l_float32 *pypt, l_float32 *pwpt, l_float32 *phpt );
void convertByteToHexAscii ( l_uint8 byteval, char *pnib1, char *pnib2 );
l_ok convertJpegToPSEmbed ( const char *filein, const char *fileout );
l_ok convertJpegToPS ( const char *filein, const char *fileout, const char *operation, l_int32 x, l_int32 y, l_int32 res, l_float32 scale, l_int32 pageno, l_int32 endpage );
l_ok convertJpegToPSString ( const char *filein, char **poutstr, l_int32 *pnbytes, l_int32 x, l_int32 y, l_int32 res, l_float32 scale, l_int32 pageno, l_int32 endpage );
char * generateJpegPS ( const char *filein, L_COMP_DATA *cid, l_float32 xpt, l_float32 ypt, l_float32 wpt, l_float32 hpt, l_int32 pageno, l_int32 endpage );
l_ok convertG4ToPSEmbed ( const char *filein, const char *fileout );
l_ok convertG4ToPS ( const char *filein, const char *fileout, const char *operation, l_int32 x, l_int32 y, l_int32 res, l_float32 scale, l_int32 pageno, l_int32 maskflag, l_int32 endpage );
l_ok convertG4ToPSString ( const char *filein, char **poutstr, l_int32 *pnbytes, l_int32 x, l_int32 y, l_int32 res, l_float32 scale, l_int32 pageno, l_int32 maskflag, l_int32 endpage );
char * generateG4PS ( const char *filein, L_COMP_DATA *cid, l_float32 xpt, l_float32 ypt, l_float32 wpt, l_float32 hpt, l_int32 maskflag, l_int32 pageno, l_int32 endpage );
l_ok convertTiffMultipageToPS ( const char *filein, const char *fileout, l_float32 fillfract );
l_ok convertFlateToPSEmbed ( const char *filein, const char *fileout );
l_ok convertFlateToPS ( const char *filein, const char *fileout, const char *operation, l_int32 x, l_int32 y, l_int32 res, l_float32 scale, l_int32 pageno, l_int32 endpage );
l_ok convertFlateToPSString ( const char *filein, char **poutstr, l_int32 *pnbytes, l_int32 x, l_int32 y, l_int32 res, l_float32 scale, l_int32 pageno, l_int32 endpage );
char * generateFlatePS ( const char *filein, L_COMP_DATA *cid, l_float32 xpt, l_float32 ypt, l_float32 wpt, l_float32 hpt, l_int32 pageno, l_int32 endpage );
l_ok pixWriteMemPS ( l_uint8 **pdata, size_t *psize, PIX *pix, BOX *box, l_int32 res, l_float32 scale );
l_int32 getResLetterPage ( l_int32 w, l_int32 h, l_float32 fillfract );
l_int32 getResA4Page ( l_int32 w, l_int32 h, l_float32 fillfract );
void l_psWriteBoundingBox ( l_int32 flag );
PTA * ptaCreate ( l_int32 n );
PTA * ptaCreateFromNuma ( NUMA *nax, NUMA *nay );
void ptaDestroy ( PTA **ppta );
PTA * ptaCopy ( PTA *pta );
PTA * ptaCopyRange ( PTA *ptas, l_int32 istart, l_int32 iend );
PTA * ptaClone ( PTA *pta );
l_ok ptaEmpty ( PTA *pta );
l_ok ptaAddPt ( PTA *pta, l_float32 x, l_float32 y );
l_ok ptaInsertPt ( PTA *pta, l_int32 index, l_int32 x, l_int32 y );
l_ok ptaRemovePt ( PTA *pta, l_int32 index );
l_int32 ptaGetRefcount ( PTA *pta );
l_int32 ptaChangeRefcount ( PTA *pta, l_int32 delta );
l_int32 ptaGetCount ( PTA *pta );
l_ok ptaGetPt ( PTA *pta, l_int32 index, l_float32 *px, l_float32 *py );
l_ok ptaGetIPt ( PTA *pta, l_int32 index, l_int32 *px, l_int32 *py );
l_ok ptaSetPt ( PTA *pta, l_int32 index, l_float32 x, l_float32 y );
l_ok ptaGetArrays ( PTA *pta, NUMA **pnax, NUMA **pnay );
PTA * ptaRead ( const char *filename );
PTA * ptaReadStream ( FILE *fp );
PTA * ptaReadMem ( const l_uint8 *data, size_t size );
l_ok ptaWriteDebug ( const char *filename, PTA *pta, l_int32 type );
l_ok ptaWrite ( const char *filename, PTA *pta, l_int32 type );
l_ok ptaWriteStream ( FILE *fp, PTA *pta, l_int32 type );
l_ok ptaWriteMem ( l_uint8 **pdata, size_t *psize, PTA *pta, l_int32 type );
PTAA * ptaaCreate ( l_int32 n );
void ptaaDestroy ( PTAA **pptaa );
l_ok ptaaAddPta ( PTAA *ptaa, PTA *pta, l_int32 copyflag );
l_int32 ptaaGetCount ( PTAA *ptaa );
PTA * ptaaGetPta ( PTAA *ptaa, l_int32 index, l_int32 accessflag );
l_ok ptaaGetPt ( PTAA *ptaa, l_int32 ipta, l_int32 jpt, l_float32 *px, l_float32 *py );
l_ok ptaaInitFull ( PTAA *ptaa, PTA *pta );
l_ok ptaaReplacePta ( PTAA *ptaa, l_int32 index, PTA *pta );
l_ok ptaaAddPt ( PTAA *ptaa, l_int32 ipta, l_float32 x, l_float32 y );
l_ok ptaaTruncate ( PTAA *ptaa );
PTAA * ptaaRead ( const char *filename );
PTAA * ptaaReadStream ( FILE *fp );
PTAA * ptaaReadMem ( const l_uint8 *data, size_t size );
l_ok ptaaWriteDebug ( const char *filename, PTAA *ptaa, l_int32 type );
l_ok ptaaWrite ( const char *filename, PTAA *ptaa, l_int32 type );
l_ok ptaaWriteStream ( FILE *fp, PTAA *ptaa, l_int32 type );
l_ok ptaaWriteMem ( l_uint8 **pdata, size_t *psize, PTAA *ptaa, l_int32 type );
PTA * ptaSubsample ( PTA *ptas, l_int32 subfactor );
l_ok ptaJoin ( PTA *ptad, PTA *ptas, l_int32 istart, l_int32 iend );
l_ok ptaaJoin ( PTAA *ptaad, PTAA *ptaas, l_int32 istart, l_int32 iend );
PTA * ptaReverse ( PTA *ptas, l_int32 type );
PTA * ptaTranspose ( PTA *ptas );
PTA * ptaCyclicPerm ( PTA *ptas, l_int32 xs, l_int32 ys );
PTA * ptaSelectRange ( PTA *ptas, l_int32 first, l_int32 last );
BOX * ptaGetBoundingRegion ( PTA *pta );
l_ok ptaGetRange ( PTA *pta, l_float32 *pminx, l_float32 *pmaxx, l_float32 *pminy, l_float32 *pmaxy );
PTA * ptaGetInsideBox ( PTA *ptas, BOX *box );
PTA * pixFindCornerPixels ( PIX *pixs );
l_int32 ptaContainsPt ( PTA *pta, l_int32 x, l_int32 y );
l_int32 ptaTestIntersection ( PTA *pta1, PTA *pta2 );
PTA * ptaTransform ( PTA *ptas, l_int32 shiftx, l_int32 shifty, l_float32 scalex, l_float32 scaley );
l_int32 ptaPtInsidePolygon ( PTA *pta, l_float32 x, l_float32 y, l_int32 *pinside );
l_float32 l_angleBetweenVectors ( l_float32 x1, l_float32 y1, l_float32 x2, l_float32 y2 );
l_ok ptaGetMinMax ( PTA *pta, l_float32 *pxmin, l_float32 *pymin, l_float32 *pxmax, l_float32 *pymax );
PTA * ptaSelectByValue ( PTA *ptas, l_float32 xth, l_float32 yth, l_int32 type, l_int32 relation );
PTA * ptaCropToMask ( PTA *ptas, PIX *pixm );
l_ok ptaGetLinearLSF ( PTA *pta, l_float32 *pa, l_float32 *pb, NUMA **pnafit );
l_ok ptaGetQuadraticLSF ( PTA *pta, l_float32 *pa, l_float32 *pb, l_float32 *pc, NUMA **pnafit );
l_ok ptaGetCubicLSF ( PTA *pta, l_float32 *pa, l_float32 *pb, l_float32 *pc, l_float32 *pd, NUMA **pnafit );
l_ok ptaGetQuarticLSF ( PTA *pta, l_float32 *pa, l_float32 *pb, l_float32 *pc, l_float32 *pd, l_float32 *pe, NUMA **pnafit );
l_ok ptaNoisyLinearLSF ( PTA *pta, l_float32 factor, PTA **pptad, l_float32 *pa, l_float32 *pb, l_float32 *pmederr, NUMA **pnafit );
l_ok ptaNoisyQuadraticLSF ( PTA *pta, l_float32 factor, PTA **pptad, l_float32 *pa, l_float32 *pb, l_float32 *pc, l_float32 *pmederr, NUMA **pnafit );
l_ok applyLinearFit ( l_float32 a, l_float32 b, l_float32 x, l_float32 *py );
l_ok applyQuadraticFit ( l_float32 a, l_float32 b, l_float32 c, l_float32 x, l_float32 *py );
l_ok applyCubicFit ( l_float32 a, l_float32 b, l_float32 c, l_float32 d, l_float32 x, l_float32 *py );
l_ok applyQuarticFit ( l_float32 a, l_float32 b, l_float32 c, l_float32 d, l_float32 e, l_float32 x, l_float32 *py );
l_ok pixPlotAlongPta ( PIX *pixs, PTA *pta, l_int32 outformat, const char *title );
PTA * ptaGetPixelsFromPix ( PIX *pixs, BOX *box );
PIX * pixGenerateFromPta ( PTA *pta, l_int32 w, l_int32 h );
PTA * ptaGetBoundaryPixels ( PIX *pixs, l_int32 type );
PTAA * ptaaGetBoundaryPixels ( PIX *pixs, l_int32 type, l_int32 connectivity, BOXA **pboxa, PIXA **ppixa );
PTAA * ptaaIndexLabeledPixels ( PIX *pixs, l_int32 *pncc );
PTA * ptaGetNeighborPixLocs ( PIX *pixs, l_int32 x, l_int32 y, l_int32 conn );
PTA * numaConvertToPta1 ( NUMA *na );
PTA * numaConvertToPta2 ( NUMA *nax, NUMA *nay );
l_ok ptaConvertToNuma ( PTA *pta, NUMA **pnax, NUMA **pnay );
PIX * pixDisplayPta ( PIX *pixd, PIX *pixs, PTA *pta );
PIX * pixDisplayPtaaPattern ( PIX *pixd, PIX *pixs, PTAA *ptaa, PIX *pixp, l_int32 cx, l_int32 cy );
PIX * pixDisplayPtaPattern ( PIX *pixd, PIX *pixs, PTA *pta, PIX *pixp, l_int32 cx, l_int32 cy, l_uint32 color );
PTA * ptaReplicatePattern ( PTA *ptas, PIX *pixp, PTA *ptap, l_int32 cx, l_int32 cy, l_int32 w, l_int32 h );
PIX * pixDisplayPtaa ( PIX *pixs, PTAA *ptaa );
PTA * ptaSort ( PTA *ptas, l_int32 sorttype, l_int32 sortorder, NUMA **pnaindex );
l_ok ptaGetSortIndex ( PTA *ptas, l_int32 sorttype, l_int32 sortorder, NUMA **pnaindex );
PTA * ptaSortByIndex ( PTA *ptas, NUMA *naindex );
PTAA * ptaaSortByIndex ( PTAA *ptaas, NUMA *naindex );
l_ok ptaGetRankValue ( PTA *pta, l_float32 fract, PTA *ptasort, l_int32 sorttype, l_float32 *pval );
PTA * ptaUnionByAset ( PTA *pta1, PTA *pta2 );
PTA * ptaRemoveDupsByAset ( PTA *ptas );
PTA * ptaIntersectionByAset ( PTA *pta1, PTA *pta2 );
L_ASET * l_asetCreateFromPta ( PTA *pta );
PTA * ptaUnionByHash ( PTA *pta1, PTA *pta2 );
l_ok ptaRemoveDupsByHash ( PTA *ptas, PTA **pptad, L_DNAHASH **pdahash );
PTA * ptaIntersectionByHash ( PTA *pta1, PTA *pta2 );
l_ok ptaFindPtByHash ( PTA *pta, L_DNAHASH *dahash, l_int32 x, l_int32 y, l_int32 *pindex );
L_DNAHASH * l_dnaHashCreateFromPta ( PTA *pta );
L_PTRA * ptraCreate ( l_int32 n );
void ptraDestroy ( L_PTRA **ppa, l_int32 freeflag, l_int32 warnflag );
l_ok ptraAdd ( L_PTRA *pa, void *item );
l_ok ptraInsert ( L_PTRA *pa, l_int32 index, void *item, l_int32 shiftflag );
void * ptraRemove ( L_PTRA *pa, l_int32 index, l_int32 flag );
void * ptraRemoveLast ( L_PTRA *pa );
void * ptraReplace ( L_PTRA *pa, l_int32 index, void *item, l_int32 freeflag );
l_ok ptraSwap ( L_PTRA *pa, l_int32 index1, l_int32 index2 );
l_ok ptraCompactArray ( L_PTRA *pa );
l_ok ptraReverse ( L_PTRA *pa );
l_ok ptraJoin ( L_PTRA *pa1, L_PTRA *pa2 );
l_ok ptraGetMaxIndex ( L_PTRA *pa, l_int32 *pmaxindex );
l_ok ptraGetActualCount ( L_PTRA *pa, l_int32 *pcount );
void * ptraGetPtrToItem ( L_PTRA *pa, l_int32 index );
L_PTRAA * ptraaCreate ( l_int32 n );
void ptraaDestroy ( L_PTRAA **ppaa, l_int32 freeflag, l_int32 warnflag );
l_ok ptraaGetSize ( L_PTRAA *paa, l_int32 *psize );
l_ok ptraaInsertPtra ( L_PTRAA *paa, l_int32 index, L_PTRA *pa );
L_PTRA * ptraaGetPtra ( L_PTRAA *paa, l_int32 index, l_int32 accessflag );
L_PTRA * ptraaFlattenToPtra ( L_PTRAA *paa );
l_ok pixQuadtreeMean ( PIX *pixs, l_int32 nlevels, PIX *pix_ma, FPIXA **pfpixa );
l_ok pixQuadtreeVariance ( PIX *pixs, l_int32 nlevels, PIX *pix_ma, DPIX *dpix_msa, FPIXA **pfpixa_v, FPIXA **pfpixa_rv );
l_ok pixMeanInRectangle ( PIX *pixs, BOX *box, PIX *pixma, l_float32 *pval );
l_ok pixVarianceInRectangle ( PIX *pixs, BOX *box, PIX *pix_ma, DPIX *dpix_msa, l_float32 *pvar, l_float32 *prvar );
BOXAA * boxaaQuadtreeRegions ( l_int32 w, l_int32 h, l_int32 nlevels );
l_ok quadtreeGetParent ( FPIXA *fpixa, l_int32 level, l_int32 x, l_int32 y, l_float32 *pval );
l_ok quadtreeGetChildren ( FPIXA *fpixa, l_int32 level, l_int32 x, l_int32 y, l_float32 *pval00, l_float32 *pval10, l_float32 *pval01, l_float32 *pval11 );
l_int32 quadtreeMaxLevels ( l_int32 w, l_int32 h );
PIX * fpixaDisplayQuadtree ( FPIXA *fpixa, l_int32 factor, l_int32 fontsize );
L_QUEUE * lqueueCreate ( l_int32 nalloc );
void lqueueDestroy ( L_QUEUE **plq, l_int32 freeflag );
l_ok lqueueAdd ( L_QUEUE *lq, void *item );
void * lqueueRemove ( L_QUEUE *lq );
l_int32 lqueueGetCount ( L_QUEUE *lq );
l_ok lqueuePrint ( FILE *fp, L_QUEUE *lq );
PIX * pixRankFilter ( PIX *pixs, l_int32 wf, l_int32 hf, l_float32 rank );
PIX * pixRankFilterRGB ( PIX *pixs, l_int32 wf, l_int32 hf, l_float32 rank );
PIX * pixRankFilterGray ( PIX *pixs, l_int32 wf, l_int32 hf, l_float32 rank );
PIX * pixMedianFilter ( PIX *pixs, l_int32 wf, l_int32 hf );
PIX * pixRankFilterWithScaling ( PIX *pixs, l_int32 wf, l_int32 hf, l_float32 rank, l_float32 scalefactor );
L_RBTREE * l_rbtreeCreate ( l_int32 keytype );
RB_TYPE * l_rbtreeLookup ( L_RBTREE *t, RB_TYPE key );
void l_rbtreeInsert ( L_RBTREE *t, RB_TYPE key, RB_TYPE value );
void l_rbtreeDelete ( L_RBTREE *t, RB_TYPE key );
void l_rbtreeDestroy ( L_RBTREE **pt );
L_RBTREE_NODE * l_rbtreeGetFirst ( L_RBTREE *t );
L_RBTREE_NODE * l_rbtreeGetNext ( L_RBTREE_NODE *n );
L_RBTREE_NODE * l_rbtreeGetLast ( L_RBTREE *t );
L_RBTREE_NODE * l_rbtreeGetPrev ( L_RBTREE_NODE *n );
l_int32 l_rbtreeGetCount ( L_RBTREE *t );
void l_rbtreePrint ( FILE *fp, L_RBTREE *t );
SARRAY * pixProcessBarcodes ( PIX *pixs, l_int32 format, l_int32 method, SARRAY **psaw, l_int32 debugflag );
PIXA * pixExtractBarcodes ( PIX *pixs, l_int32 debugflag );
SARRAY * pixReadBarcodes ( PIXA *pixa, l_int32 format, l_int32 method, SARRAY **psaw, l_int32 debugflag );
NUMA * pixReadBarcodeWidths ( PIX *pixs, l_int32 method, l_int32 debugflag );
BOXA * pixLocateBarcodes ( PIX *pixs, l_int32 thresh, PIX **ppixb, PIX **ppixm );
PIX * pixDeskewBarcode ( PIX *pixs, PIX *pixb, BOX *box, l_int32 margin, l_int32 threshold, l_float32 *pangle, l_float32 *pconf );
NUMA * pixExtractBarcodeWidths1 ( PIX *pixs, l_float32 thresh, l_float32 binfract, NUMA **pnaehist, NUMA **pnaohist, l_int32 debugflag );
NUMA * pixExtractBarcodeWidths2 ( PIX *pixs, l_float32 thresh, l_float32 *pwidth, NUMA **pnac, l_int32 debugflag );
NUMA * pixExtractBarcodeCrossings ( PIX *pixs, l_float32 thresh, l_int32 debugflag );
NUMA * numaQuantizeCrossingsByWidth ( NUMA *nas, l_float32 binfract, NUMA **pnaehist, NUMA **pnaohist, l_int32 debugflag );
NUMA * numaQuantizeCrossingsByWindow ( NUMA *nas, l_float32 ratio, l_float32 *pwidth, l_float32 *pfirstloc, NUMA **pnac, l_int32 debugflag );
PIXA * pixaReadFiles ( const char *dirname, const char *substr );
PIXA * pixaReadFilesSA ( SARRAY *sa );
PIX * pixRead ( const char *filename );
PIX * pixReadWithHint ( const char *filename, l_int32 hint );
PIX * pixReadIndexed ( SARRAY *sa, l_int32 index );
PIX * pixReadStream ( FILE *fp, l_int32 hint );
l_ok pixReadHeader ( const char *filename, l_int32 *pformat, l_int32 *pw, l_int32 *ph, l_int32 *pbps, l_int32 *pspp, l_int32 *piscmap );
l_ok findFileFormat ( const char *filename, l_int32 *pformat );
l_ok findFileFormatStream ( FILE *fp, l_int32 *pformat );
l_ok findFileFormatBuffer ( const l_uint8 *buf, l_int32 *pformat );
l_int32 fileFormatIsTiff ( FILE *fp );
PIX * pixReadMem ( const l_uint8 *data, size_t size );
l_ok pixReadHeaderMem ( const l_uint8 *data, size_t size, l_int32 *pformat, l_int32 *pw, l_int32 *ph, l_int32 *pbps, l_int32 *pspp, l_int32 *piscmap );
l_ok writeImageFileInfo ( const char *filename, FILE *fpout, l_int32 headeronly );
l_ok ioFormatTest ( const char *filename );
L_RECOG * recogCreateFromRecog ( L_RECOG *recs, l_int32 scalew, l_int32 scaleh, l_int32 linew, l_int32 threshold, l_int32 maxyshift );
L_RECOG * recogCreateFromPixa ( PIXA *pixa, l_int32 scalew, l_int32 scaleh, l_int32 linew, l_int32 threshold, l_int32 maxyshift );
L_RECOG * recogCreateFromPixaNoFinish ( PIXA *pixa, l_int32 scalew, l_int32 scaleh, l_int32 linew, l_int32 threshold, l_int32 maxyshift );
L_RECOG * recogCreate ( l_int32 scalew, l_int32 scaleh, l_int32 linew, l_int32 threshold, l_int32 maxyshift );
void recogDestroy ( L_RECOG **precog );
l_int32 recogGetCount ( L_RECOG *recog );
l_ok recogSetParams ( L_RECOG *recog, l_int32 type, l_int32 min_nopad, l_float32 max_wh_ratio, l_float32 max_ht_ratio );
l_int32 recogGetClassIndex ( L_RECOG *recog, l_int32 val, char *text, l_int32 *pindex );
l_ok recogStringToIndex ( L_RECOG *recog, char *text, l_int32 *pindex );
l_int32 recogGetClassString ( L_RECOG *recog, l_int32 index, char **pcharstr );
l_ok l_convertCharstrToInt ( const char *str, l_int32 *pval );
L_RECOG * recogRead ( const char *filename );
L_RECOG * recogReadStream ( FILE *fp );
L_RECOG * recogReadMem ( const l_uint8 *data, size_t size );
l_ok recogWrite ( const char *filename, L_RECOG *recog );
l_ok recogWriteStream ( FILE *fp, L_RECOG *recog );
l_ok recogWriteMem ( l_uint8 **pdata, size_t *psize, L_RECOG *recog );
PIXA * recogExtractPixa ( L_RECOG *recog );
BOXA * recogDecode ( L_RECOG *recog, PIX *pixs, l_int32 nlevels, PIX **ppixdb );
l_ok recogCreateDid ( L_RECOG *recog, PIX *pixs );
l_ok recogDestroyDid ( L_RECOG *recog );
l_int32 recogDidExists ( L_RECOG *recog );
L_RDID * recogGetDid ( L_RECOG *recog );
l_ok recogSetChannelParams ( L_RECOG *recog, l_int32 nlevels );
l_ok recogIdentifyMultiple ( L_RECOG *recog, PIX *pixs, l_int32 minh, l_int32 skipsplit, BOXA **pboxa, PIXA **ppixa, PIX **ppixdb, l_int32 debugsplit );
l_ok recogSplitIntoCharacters ( L_RECOG *recog, PIX *pixs, l_int32 minh, l_int32 skipsplit, BOXA **pboxa, PIXA **ppixa, l_int32 debug );
l_ok recogCorrelationBestRow ( L_RECOG *recog, PIX *pixs, BOXA **pboxa, NUMA **pnascore, NUMA **pnaindex, SARRAY **psachar, l_int32 debug );
l_ok recogCorrelationBestChar ( L_RECOG *recog, PIX *pixs, BOX **pbox, l_float32 *pscore, l_int32 *pindex, char **pcharstr, PIX **ppixdb );
l_ok recogIdentifyPixa ( L_RECOG *recog, PIXA *pixa, PIX **ppixdb );
l_ok recogIdentifyPix ( L_RECOG *recog, PIX *pixs, PIX **ppixdb );
l_ok recogSkipIdentify ( L_RECOG *recog );
void rchaDestroy ( L_RCHA **prcha );
void rchDestroy ( L_RCH **prch );
l_ok rchaExtract ( L_RCHA *rcha, NUMA **pnaindex, NUMA **pnascore, SARRAY **psatext, NUMA **pnasample, NUMA **pnaxloc, NUMA **pnayloc, NUMA **pnawidth );
l_ok rchExtract ( L_RCH *rch, l_int32 *pindex, l_float32 *pscore, char **ptext, l_int32 *psample, l_int32 *pxloc, l_int32 *pyloc, l_int32 *pwidth );
PIX * recogProcessToIdentify ( L_RECOG *recog, PIX *pixs, l_int32 pad );
SARRAY * recogExtractNumbers ( L_RECOG *recog, BOXA *boxas, l_float32 scorethresh, l_int32 spacethresh, BOXAA **pbaa, NUMAA **pnaa );
PIXA * showExtractNumbers ( PIX *pixs, SARRAY *sa, BOXAA *baa, NUMAA *naa, PIX **ppixdb );
l_ok recogTrainLabeled ( L_RECOG *recog, PIX *pixs, BOX *box, char *text, l_int32 debug );
l_ok recogProcessLabeled ( L_RECOG *recog, PIX *pixs, BOX *box, char *text, PIX **ppix );
l_ok recogAddSample ( L_RECOG *recog, PIX *pix, l_int32 debug );
PIX * recogModifyTemplate ( L_RECOG *recog, PIX *pixs );
l_int32 recogAverageSamples ( L_RECOG **precog, l_int32 debug );
l_int32 pixaAccumulateSamples ( PIXA *pixa, PTA *pta, PIX **ppixd, l_float32 *px, l_float32 *py );
l_ok recogTrainingFinished ( L_RECOG **precog, l_int32 modifyflag, l_int32 minsize, l_float32 minfract );
PIXA * recogFilterPixaBySize ( PIXA *pixas, l_int32 setsize, l_int32 maxkeep, l_float32 max_ht_ratio, NUMA **pna );
PIXAA * recogSortPixaByClass ( PIXA *pixa, l_int32 setsize );
l_ok recogRemoveOutliers1 ( L_RECOG **precog, l_float32 minscore, l_int32 mintarget, l_int32 minsize, PIX **ppixsave, PIX **ppixrem );
PIXA * pixaRemoveOutliers1 ( PIXA *pixas, l_float32 minscore, l_int32 mintarget, l_int32 minsize, PIX **ppixsave, PIX **ppixrem );
l_ok recogRemoveOutliers2 ( L_RECOG **precog, l_float32 minscore, l_int32 minsize, PIX **ppixsave, PIX **ppixrem );
PIXA * pixaRemoveOutliers2 ( PIXA *pixas, l_float32 minscore, l_int32 minsize, PIX **ppixsave, PIX **ppixrem );
PIXA * recogTrainFromBoot ( L_RECOG *recogboot, PIXA *pixas, l_float32 minscore, l_int32 threshold, l_int32 debug );
l_ok recogPadDigitTrainingSet ( L_RECOG **precog, l_int32 scaleh, l_int32 linew );
l_int32 recogIsPaddingNeeded ( L_RECOG *recog, SARRAY **psa );
PIXA * recogAddDigitPadTemplates ( L_RECOG *recog, SARRAY *sa );
L_RECOG * recogMakeBootDigitRecog ( l_int32 nsamp, l_int32 scaleh, l_int32 linew, l_int32 maxyshift, l_int32 debug );
PIXA * recogMakeBootDigitTemplates ( l_int32 nsamp, l_int32 debug );
l_ok recogShowContent ( FILE *fp, L_RECOG *recog, l_int32 index, l_int32 display );
l_ok recogDebugAverages ( L_RECOG **precog, l_int32 debug );
l_int32 recogShowAverageTemplates ( L_RECOG *recog );
l_ok recogShowMatchesInRange ( L_RECOG *recog, PIXA *pixa, l_float32 minscore, l_float32 maxscore, l_int32 display );
PIX * recogShowMatch ( L_RECOG *recog, PIX *pix1, PIX *pix2, BOX *box, l_int32 index, l_float32 score );
l_ok regTestSetup ( l_int32 argc, char **argv, L_REGPARAMS **prp );
l_ok regTestCleanup ( L_REGPARAMS *rp );
l_ok regTestCompareValues ( L_REGPARAMS *rp, l_float32 val1, l_float32 val2, l_float32 delta );
l_ok regTestCompareStrings ( L_REGPARAMS *rp, l_uint8 *string1, size_t bytes1, l_uint8 *string2, size_t bytes2 );
l_ok regTestComparePix ( L_REGPARAMS *rp, PIX *pix1, PIX *pix2 );
l_ok regTestCompareSimilarPix ( L_REGPARAMS *rp, PIX *pix1, PIX *pix2, l_int32 mindiff, l_float32 maxfract, l_int32 printstats );
l_ok regTestCheckFile ( L_REGPARAMS *rp, const char *localname );
l_ok regTestCompareFiles ( L_REGPARAMS *rp, l_int32 index1, l_int32 index2 );
l_ok regTestWritePixAndCheck ( L_REGPARAMS *rp, PIX *pix, l_int32 format );
l_ok regTestWriteDataAndCheck ( L_REGPARAMS *rp, void *data, size_t nbytes, const char *ext );
char * regTestGenLocalFilename ( L_REGPARAMS *rp, l_int32 index, l_int32 format );
l_ok pixRasterop ( PIX *pixd, l_int32 dx, l_int32 dy, l_int32 dw, l_int32 dh, l_int32 op, PIX *pixs, l_int32 sx, l_int32 sy );
l_ok pixRasteropVip ( PIX *pixd, l_int32 bx, l_int32 bw, l_int32 vshift, l_int32 incolor );
l_ok pixRasteropHip ( PIX *pixd, l_int32 by, l_int32 bh, l_int32 hshift, l_int32 incolor );
PIX * pixTranslate ( PIX *pixd, PIX *pixs, l_int32 hshift, l_int32 vshift, l_int32 incolor );
l_ok pixRasteropIP ( PIX *pixd, l_int32 hshift, l_int32 vshift, l_int32 incolor );
l_ok pixRasteropFullImage ( PIX *pixd, PIX *pixs, l_int32 op );
void rasteropUniLow ( l_uint32 *datad, l_int32 dpixw, l_int32 dpixh, l_int32 depth, l_int32 dwpl, l_int32 dx, l_int32 dy, l_int32 dw, l_int32 dh, l_int32 op );
void rasteropLow ( l_uint32 *datad, l_int32 dpixw, l_int32 dpixh, l_int32 depth, l_int32 dwpl, l_int32 dx, l_int32 dy, l_int32 dw, l_int32 dh, l_int32 op, l_uint32 *datas, l_int32 spixw, l_int32 spixh, l_int32 swpl, l_int32 sx, l_int32 sy );
void rasteropVipLow ( l_uint32 *data, l_int32 pixw, l_int32 pixh, l_int32 depth, l_int32 wpl, l_int32 x, l_int32 w, l_int32 shift );
void rasteropHipLow ( l_uint32 *data, l_int32 pixh, l_int32 depth, l_int32 wpl, l_int32 y, l_int32 h, l_int32 shift );
PIX * pixRotate ( PIX *pixs, l_float32 angle, l_int32 type, l_int32 incolor, l_int32 width, l_int32 height );
PIX * pixEmbedForRotation ( PIX *pixs, l_float32 angle, l_int32 incolor, l_int32 width, l_int32 height );
PIX * pixRotateBySampling ( PIX *pixs, l_int32 xcen, l_int32 ycen, l_float32 angle, l_int32 incolor );
PIX * pixRotateBinaryNice ( PIX *pixs, l_float32 angle, l_int32 incolor );
PIX * pixRotateWithAlpha ( PIX *pixs, l_float32 angle, PIX *pixg, l_float32 fract );
PIX * pixRotateAM ( PIX *pixs, l_float32 angle, l_int32 incolor );
PIX * pixRotateAMColor ( PIX *pixs, l_float32 angle, l_uint32 colorval );
PIX * pixRotateAMGray ( PIX *pixs, l_float32 angle, l_uint8 grayval );
PIX * pixRotateAMCorner ( PIX *pixs, l_float32 angle, l_int32 incolor );
PIX * pixRotateAMColorCorner ( PIX *pixs, l_float32 angle, l_uint32 fillval );
PIX * pixRotateAMGrayCorner ( PIX *pixs, l_float32 angle, l_uint8 grayval );
PIX * pixRotateAMColorFast ( PIX *pixs, l_float32 angle, l_uint32 colorval );
PIX * pixRotateOrth ( PIX *pixs, l_int32 quads );
PIX * pixRotate180 ( PIX *pixd, PIX *pixs );
PIX * pixRotate90 ( PIX *pixs, l_int32 direction );
PIX * pixFlipLR ( PIX *pixd, PIX *pixs );
PIX * pixFlipTB ( PIX *pixd, PIX *pixs );
PIX * pixRotateShear ( PIX *pixs, l_int32 xcen, l_int32 ycen, l_float32 angle, l_int32 incolor );
PIX * pixRotate2Shear ( PIX *pixs, l_int32 xcen, l_int32 ycen, l_float32 angle, l_int32 incolor );
PIX * pixRotate3Shear ( PIX *pixs, l_int32 xcen, l_int32 ycen, l_float32 angle, l_int32 incolor );
l_ok pixRotateShearIP ( PIX *pixs, l_int32 xcen, l_int32 ycen, l_float32 angle, l_int32 incolor );
PIX * pixRotateShearCenter ( PIX *pixs, l_float32 angle, l_int32 incolor );
l_ok pixRotateShearCenterIP ( PIX *pixs, l_float32 angle, l_int32 incolor );
PIX * pixStrokeWidthTransform ( PIX *pixs, l_int32 color, l_int32 depth, l_int32 nangles );
PIX * pixRunlengthTransform ( PIX *pixs, l_int32 color, l_int32 direction, l_int32 depth );
l_ok pixFindHorizontalRuns ( PIX *pix, l_int32 y, l_int32 *xstart, l_int32 *xend, l_int32 *pn );
l_ok pixFindVerticalRuns ( PIX *pix, l_int32 x, l_int32 *ystart, l_int32 *yend, l_int32 *pn );
NUMA * pixFindMaxRuns ( PIX *pix, l_int32 direction, NUMA **pnastart );
l_ok pixFindMaxHorizontalRunOnLine ( PIX *pix, l_int32 y, l_int32 *pxstart, l_int32 *psize );
l_ok pixFindMaxVerticalRunOnLine ( PIX *pix, l_int32 x, l_int32 *pystart, l_int32 *psize );
l_ok runlengthMembershipOnLine ( l_int32 *buffer, l_int32 size, l_int32 depth, l_int32 *start, l_int32 *end, l_int32 n );
l_int32 * makeMSBitLocTab ( l_int32 bitval );
SARRAY * sarrayCreate ( l_int32 n );
SARRAY * sarrayCreateInitialized ( l_int32 n, const char *initstr );
SARRAY * sarrayCreateWordsFromString ( const char *string );
SARRAY * sarrayCreateLinesFromString ( const char *string, l_int32 blankflag );
void sarrayDestroy ( SARRAY **psa );
SARRAY * sarrayCopy ( SARRAY *sa );
SARRAY * sarrayClone ( SARRAY *sa );
l_ok sarrayAddString ( SARRAY *sa, const char *string, l_int32 copyflag );
char * sarrayRemoveString ( SARRAY *sa, l_int32 index );
l_ok sarrayReplaceString ( SARRAY *sa, l_int32 index, char *newstr, l_int32 copyflag );
l_ok sarrayClear ( SARRAY *sa );
l_int32 sarrayGetCount ( SARRAY *sa );
char ** sarrayGetArray ( SARRAY *sa, l_int32 *pnalloc, l_int32 *pn );
char * sarrayGetString ( SARRAY *sa, l_int32 index, l_int32 copyflag );
l_int32 sarrayGetRefcount ( SARRAY *sa );
l_ok sarrayChangeRefcount ( SARRAY *sa, l_int32 delta );
char * sarrayToString ( SARRAY *sa, l_int32 addnlflag );
char * sarrayToStringRange ( SARRAY *sa, l_int32 first, l_int32 nstrings, l_int32 addnlflag );
l_ok sarrayJoin ( SARRAY *sa1, SARRAY *sa2 );
l_ok sarrayAppendRange ( SARRAY *sa1, SARRAY *sa2, l_int32 start, l_int32 end );
l_ok sarrayPadToSameSize ( SARRAY *sa1, SARRAY *sa2, const char *padstring );
SARRAY * sarrayConvertWordsToLines ( SARRAY *sa, l_int32 linesize );
l_int32 sarraySplitString ( SARRAY *sa, const char *str, const char *separators );
SARRAY * sarraySelectBySubstring ( SARRAY *sain, const char *substr );
SARRAY * sarraySelectByRange ( SARRAY *sain, l_int32 first, l_int32 last );
l_int32 sarrayParseRange ( SARRAY *sa, l_int32 start, l_int32 *pactualstart, l_int32 *pend, l_int32 *pnewstart, const char *substr, l_int32 loc );
SARRAY * sarrayRead ( const char *filename );
SARRAY * sarrayReadStream ( FILE *fp );
SARRAY * sarrayReadMem ( const l_uint8 *data, size_t size );
l_ok sarrayWrite ( const char *filename, SARRAY *sa );
l_ok sarrayWriteStream ( FILE *fp, SARRAY *sa );
l_ok sarrayWriteMem ( l_uint8 **pdata, size_t *psize, SARRAY *sa );
l_ok sarrayAppend ( const char *filename, SARRAY *sa );
SARRAY * getNumberedPathnamesInDirectory ( const char *dirname, const char *substr, l_int32 numpre, l_int32 numpost, l_int32 maxnum );
SARRAY * getSortedPathnamesInDirectory ( const char *dirname, const char *substr, l_int32 first, l_int32 nfiles );
SARRAY * convertSortedToNumberedPathnames ( SARRAY *sa, l_int32 numpre, l_int32 numpost, l_int32 maxnum );
SARRAY * getFilenamesInDirectory ( const char *dirname );
SARRAY * sarraySort ( SARRAY *saout, SARRAY *sain, l_int32 sortorder );
SARRAY * sarraySortByIndex ( SARRAY *sain, NUMA *naindex );
l_int32 stringCompareLexical ( const char *str1, const char *str2 );
SARRAY * sarrayUnionByAset ( SARRAY *sa1, SARRAY *sa2 );
SARRAY * sarrayRemoveDupsByAset ( SARRAY *sas );
SARRAY * sarrayIntersectionByAset ( SARRAY *sa1, SARRAY *sa2 );
L_ASET * l_asetCreateFromSarray ( SARRAY *sa );
l_ok sarrayRemoveDupsByHash ( SARRAY *sas, SARRAY **psad, L_DNAHASH **pdahash );
SARRAY * sarrayIntersectionByHash ( SARRAY *sa1, SARRAY *sa2 );
l_ok sarrayFindStringByHash ( SARRAY *sa, L_DNAHASH *dahash, const char *str, l_int32 *pindex );
L_DNAHASH * l_dnaHashCreateFromSarray ( SARRAY *sa );
SARRAY * sarrayGenerateIntegers ( l_int32 n );
l_ok sarrayLookupCSKV ( SARRAY *sa, const char *keystring, char **pvalstring );
PIX * pixScale ( PIX *pixs, l_float32 scalex, l_float32 scaley );
PIX * pixScaleToSizeRel ( PIX *pixs, l_int32 delw, l_int32 delh );
PIX * pixScaleToSize ( PIX *pixs, l_int32 wd, l_int32 hd );
PIX * pixScaleToResolution ( PIX *pixs, l_float32 target, l_float32 assumed, l_float32 *pscalefact );
PIX * pixScaleGeneral ( PIX *pixs, l_float32 scalex, l_float32 scaley, l_float32 sharpfract, l_int32 sharpwidth );
PIX * pixScaleLI ( PIX *pixs, l_float32 scalex, l_float32 scaley );
PIX * pixScaleColorLI ( PIX *pixs, l_float32 scalex, l_float32 scaley );
PIX * pixScaleColor2xLI ( PIX *pixs );
PIX * pixScaleColor4xLI ( PIX *pixs );
PIX * pixScaleGrayLI ( PIX *pixs, l_float32 scalex, l_float32 scaley );
PIX * pixScaleGray2xLI ( PIX *pixs );
PIX * pixScaleGray4xLI ( PIX *pixs );
PIX * pixScaleGray2xLIThresh ( PIX *pixs, l_int32 thresh );
PIX * pixScaleGray2xLIDither ( PIX *pixs );
PIX * pixScaleGray4xLIThresh ( PIX *pixs, l_int32 thresh );
PIX * pixScaleGray4xLIDither ( PIX *pixs );
PIX * pixScaleBySampling ( PIX *pixs, l_float32 scalex, l_float32 scaley );
PIX * pixScaleBySamplingToSize ( PIX *pixs, l_int32 wd, l_int32 hd );
PIX * pixScaleByIntSampling ( PIX *pixs, l_int32 factor );
PIX * pixScaleRGBToGrayFast ( PIX *pixs, l_int32 factor, l_int32 color );
PIX * pixScaleRGBToBinaryFast ( PIX *pixs, l_int32 factor, l_int32 thresh );
PIX * pixScaleGrayToBinaryFast ( PIX *pixs, l_int32 factor, l_int32 thresh );
PIX * pixScaleSmooth ( PIX *pix, l_float32 scalex, l_float32 scaley );
PIX * pixScaleSmoothToSize ( PIX *pixs, l_int32 wd, l_int32 hd );
PIX * pixScaleRGBToGray2 ( PIX *pixs, l_float32 rwt, l_float32 gwt, l_float32 bwt );
PIX * pixScaleAreaMap ( PIX *pix, l_float32 scalex, l_float32 scaley );
PIX * pixScaleAreaMap2 ( PIX *pix );
PIX * pixScaleAreaMapToSize ( PIX *pixs, l_int32 wd, l_int32 hd );
PIX * pixScaleBinary ( PIX *pixs, l_float32 scalex, l_float32 scaley );
PIX * pixScaleToGray ( PIX *pixs, l_float32 scalefactor );
PIX * pixScaleToGrayFast ( PIX *pixs, l_float32 scalefactor );
PIX * pixScaleToGray2 ( PIX *pixs );
PIX * pixScaleToGray3 ( PIX *pixs );
PIX * pixScaleToGray4 ( PIX *pixs );
PIX * pixScaleToGray6 ( PIX *pixs );
PIX * pixScaleToGray8 ( PIX *pixs );
PIX * pixScaleToGray16 ( PIX *pixs );
PIX * pixScaleToGrayMipmap ( PIX *pixs, l_float32 scalefactor );
PIX * pixScaleMipmap ( PIX *pixs1, PIX *pixs2, l_float32 scale );
PIX * pixExpandReplicate ( PIX *pixs, l_int32 factor );
PIX * pixScaleGrayMinMax ( PIX *pixs, l_int32 xfact, l_int32 yfact, l_int32 type );
PIX * pixScaleGrayMinMax2 ( PIX *pixs, l_int32 type );
PIX * pixScaleGrayRankCascade ( PIX *pixs, l_int32 level1, l_int32 level2, l_int32 level3, l_int32 level4 );
PIX * pixScaleGrayRank2 ( PIX *pixs, l_int32 rank );
l_ok pixScaleAndTransferAlpha ( PIX *pixd, PIX *pixs, l_float32 scalex, l_float32 scaley );
PIX * pixScaleWithAlpha ( PIX *pixs, l_float32 scalex, l_float32 scaley, PIX *pixg, l_float32 fract );
PIX * pixSeedfillBinary ( PIX *pixd, PIX *pixs, PIX *pixm, l_int32 connectivity );
PIX * pixSeedfillBinaryRestricted ( PIX *pixd, PIX *pixs, PIX *pixm, l_int32 connectivity, l_int32 xmax, l_int32 ymax );
PIX * pixHolesByFilling ( PIX *pixs, l_int32 connectivity );
PIX * pixFillClosedBorders ( PIX *pixs, l_int32 connectivity );
PIX * pixExtractBorderConnComps ( PIX *pixs, l_int32 connectivity );
PIX * pixRemoveBorderConnComps ( PIX *pixs, l_int32 connectivity );
PIX * pixFillBgFromBorder ( PIX *pixs, l_int32 connectivity );
PIX * pixFillHolesToBoundingRect ( PIX *pixs, l_int32 minsize, l_float32 maxhfract, l_float32 minfgfract );
l_ok pixSeedfillGray ( PIX *pixs, PIX *pixm, l_int32 connectivity );
l_ok pixSeedfillGrayInv ( PIX *pixs, PIX *pixm, l_int32 connectivity );
l_ok pixSeedfillGraySimple ( PIX *pixs, PIX *pixm, l_int32 connectivity );
l_ok pixSeedfillGrayInvSimple ( PIX *pixs, PIX *pixm, l_int32 connectivity );
PIX * pixSeedfillGrayBasin ( PIX *pixb, PIX *pixm, l_int32 delta, l_int32 connectivity );
PIX * pixDistanceFunction ( PIX *pixs, l_int32 connectivity, l_int32 outdepth, l_int32 boundcond );
PIX * pixSeedspread ( PIX *pixs, l_int32 connectivity );
l_ok pixLocalExtrema ( PIX *pixs, l_int32 maxmin, l_int32 minmax, PIX **ppixmin, PIX **ppixmax );
l_ok pixSelectedLocalExtrema ( PIX *pixs, l_int32 mindist, PIX **ppixmin, PIX **ppixmax );
PIX * pixFindEqualValues ( PIX *pixs1, PIX *pixs2 );
l_ok pixSelectMinInConnComp ( PIX *pixs, PIX *pixm, PTA **ppta, NUMA **pnav );
PIX * pixRemoveSeededComponents ( PIX *pixd, PIX *pixs, PIX *pixm, l_int32 connectivity, l_int32 bordersize );
SELA * selaCreate ( l_int32 n );
void selaDestroy ( SELA **psela );
SEL * selCreate ( l_int32 height, l_int32 width, const char *name );
void selDestroy ( SEL **psel );
SEL * selCopy ( SEL *sel );
SEL * selCreateBrick ( l_int32 h, l_int32 w, l_int32 cy, l_int32 cx, l_int32 type );
SEL * selCreateComb ( l_int32 factor1, l_int32 factor2, l_int32 direction );
l_int32 ** create2dIntArray ( l_int32 sy, l_int32 sx );
l_ok selaAddSel ( SELA *sela, SEL *sel, const char *selname, l_int32 copyflag );
l_int32 selaGetCount ( SELA *sela );
SEL * selaGetSel ( SELA *sela, l_int32 i );
char * selGetName ( SEL *sel );
l_ok selSetName ( SEL *sel, const char *name );
l_ok selaFindSelByName ( SELA *sela, const char *name, l_int32 *pindex, SEL **psel );
l_ok selGetElement ( SEL *sel, l_int32 row, l_int32 col, l_int32 *ptype );
l_ok selSetElement ( SEL *sel, l_int32 row, l_int32 col, l_int32 type );
l_ok selGetParameters ( SEL *sel, l_int32 *psy, l_int32 *psx, l_int32 *pcy, l_int32 *pcx );
l_ok selSetOrigin ( SEL *sel, l_int32 cy, l_int32 cx );
l_ok selGetTypeAtOrigin ( SEL *sel, l_int32 *ptype );
char * selaGetBrickName ( SELA *sela, l_int32 hsize, l_int32 vsize );
char * selaGetCombName ( SELA *sela, l_int32 size, l_int32 direction );
l_ok getCompositeParameters ( l_int32 size, l_int32 *psize1, l_int32 *psize2, char **pnameh1, char **pnameh2, char **pnamev1, char **pnamev2 );
SARRAY * selaGetSelnames ( SELA *sela );
l_ok selFindMaxTranslations ( SEL *sel, l_int32 *pxp, l_int32 *pyp, l_int32 *pxn, l_int32 *pyn );
SEL * selRotateOrth ( SEL *sel, l_int32 quads );
SELA * selaRead ( const char *fname );
SELA * selaReadStream ( FILE *fp );
SEL * selRead ( const char *fname );
SEL * selReadStream ( FILE *fp );
l_ok selaWrite ( const char *fname, SELA *sela );
l_ok selaWriteStream ( FILE *fp, SELA *sela );
l_ok selWrite ( const char *fname, SEL *sel );
l_ok selWriteStream ( FILE *fp, SEL *sel );
SEL * selCreateFromString ( const char *text, l_int32 h, l_int32 w, const char *name );
char * selPrintToString ( SEL *sel );
SELA * selaCreateFromFile ( const char *filename );
SEL * selCreateFromPta ( PTA *pta, l_int32 cy, l_int32 cx, const char *name );
SEL * selCreateFromPix ( PIX *pix, l_int32 cy, l_int32 cx, const char *name );
SEL * selReadFromColorImage ( const char *pathname );
SEL * selCreateFromColorPix ( PIX *pixs, const char *selname );
PIX * selDisplayInPix ( SEL *sel, l_int32 size, l_int32 gthick );
PIX * selaDisplayInPix ( SELA *sela, l_int32 size, l_int32 gthick, l_int32 spacing, l_int32 ncols );
SELA * selaAddBasic ( SELA *sela );
SELA * selaAddHitMiss ( SELA *sela );
SELA * selaAddDwaLinear ( SELA *sela );
SELA * selaAddDwaCombs ( SELA *sela );
SELA * selaAddCrossJunctions ( SELA *sela, l_float32 hlsize, l_float32 mdist, l_int32 norient, l_int32 debugflag );
SELA * selaAddTJunctions ( SELA *sela, l_float32 hlsize, l_float32 mdist, l_int32 norient, l_int32 debugflag );
SELA * sela4ccThin ( SELA *sela );
SELA * sela8ccThin ( SELA *sela );
SELA * sela4and8ccThin ( SELA *sela );
SEL * pixGenerateSelWithRuns ( PIX *pixs, l_int32 nhlines, l_int32 nvlines, l_int32 distance, l_int32 minlength, l_int32 toppix, l_int32 botpix, l_int32 leftpix, l_int32 rightpix, PIX **ppixe );
SEL * pixGenerateSelRandom ( PIX *pixs, l_float32 hitfract, l_float32 missfract, l_int32 distance, l_int32 toppix, l_int32 botpix, l_int32 leftpix, l_int32 rightpix, PIX **ppixe );
SEL * pixGenerateSelBoundary ( PIX *pixs, l_int32 hitdist, l_int32 missdist, l_int32 hitskip, l_int32 missskip, l_int32 topflag, l_int32 botflag, l_int32 leftflag, l_int32 rightflag, PIX **ppixe );
NUMA * pixGetRunCentersOnLine ( PIX *pixs, l_int32 x, l_int32 y, l_int32 minlength );
NUMA * pixGetRunsOnLine ( PIX *pixs, l_int32 x1, l_int32 y1, l_int32 x2, l_int32 y2 );
PTA * pixSubsampleBoundaryPixels ( PIX *pixs, l_int32 skip );
l_int32 adjacentOnPixelInRaster ( PIX *pixs, l_int32 x, l_int32 y, l_int32 *pxa, l_int32 *pya );
PIX * pixDisplayHitMissSel ( PIX *pixs, SEL *sel, l_int32 scalefactor, l_uint32 hitcolor, l_uint32 misscolor );
PIX * pixHShear ( PIX *pixd, PIX *pixs, l_int32 yloc, l_float32 radang, l_int32 incolor );
PIX * pixVShear ( PIX *pixd, PIX *pixs, l_int32 xloc, l_float32 radang, l_int32 incolor );
PIX * pixHShearCorner ( PIX *pixd, PIX *pixs, l_float32 radang, l_int32 incolor );
PIX * pixVShearCorner ( PIX *pixd, PIX *pixs, l_float32 radang, l_int32 incolor );
PIX * pixHShearCenter ( PIX *pixd, PIX *pixs, l_float32 radang, l_int32 incolor );
PIX * pixVShearCenter ( PIX *pixd, PIX *pixs, l_float32 radang, l_int32 incolor );
l_ok pixHShearIP ( PIX *pixs, l_int32 yloc, l_float32 radang, l_int32 incolor );
l_ok pixVShearIP ( PIX *pixs, l_int32 xloc, l_float32 radang, l_int32 incolor );
PIX * pixHShearLI ( PIX *pixs, l_int32 yloc, l_float32 radang, l_int32 incolor );
PIX * pixVShearLI ( PIX *pixs, l_int32 xloc, l_float32 radang, l_int32 incolor );
PIX * pixDeskewBoth ( PIX *pixs, l_int32 redsearch );
PIX * pixDeskew ( PIX *pixs, l_int32 redsearch );
PIX * pixFindSkewAndDeskew ( PIX *pixs, l_int32 redsearch, l_float32 *pangle, l_float32 *pconf );
PIX * pixDeskewGeneral ( PIX *pixs, l_int32 redsweep, l_float32 sweeprange, l_float32 sweepdelta, l_int32 redsearch, l_int32 thresh, l_float32 *pangle, l_float32 *pconf );
l_ok pixFindSkew ( PIX *pixs, l_float32 *pangle, l_float32 *pconf );
l_ok pixFindSkewSweep ( PIX *pixs, l_float32 *pangle, l_int32 reduction, l_float32 sweeprange, l_float32 sweepdelta );
l_ok pixFindSkewSweepAndSearch ( PIX *pixs, l_float32 *pangle, l_float32 *pconf, l_int32 redsweep, l_int32 redsearch, l_float32 sweeprange, l_float32 sweepdelta, l_float32 minbsdelta );
l_ok pixFindSkewSweepAndSearchScore ( PIX *pixs, l_float32 *pangle, l_float32 *pconf, l_float32 *pendscore, l_int32 redsweep, l_int32 redsearch, l_float32 sweepcenter, l_float32 sweeprange, l_float32 sweepdelta, l_float32 minbsdelta );
l_ok pixFindSkewSweepAndSearchScorePivot ( PIX *pixs, l_float32 *pangle, l_float32 *pconf, l_float32 *pendscore, l_int32 redsweep, l_int32 redsearch, l_float32 sweepcenter, l_float32 sweeprange, l_float32 sweepdelta, l_float32 minbsdelta, l_int32 pivot );
l_int32 pixFindSkewOrthogonalRange ( PIX *pixs, l_float32 *pangle, l_float32 *pconf, l_int32 redsweep, l_int32 redsearch, l_float32 sweeprange, l_float32 sweepdelta, l_float32 minbsdelta, l_float32 confprior );
l_ok pixFindDifferentialSquareSum ( PIX *pixs, l_float32 *psum );
l_ok pixFindNormalizedSquareSum ( PIX *pixs, l_float32 *phratio, l_float32 *pvratio, l_float32 *pfract );
PIX * pixReadStreamSpix ( FILE *fp );
l_ok readHeaderSpix ( const char *filename, l_int32 *pwidth, l_int32 *pheight, l_int32 *pbps, l_int32 *pspp, l_int32 *piscmap );
l_ok freadHeaderSpix ( FILE *fp, l_int32 *pwidth, l_int32 *pheight, l_int32 *pbps, l_int32 *pspp, l_int32 *piscmap );
l_ok sreadHeaderSpix ( const l_uint32 *data, l_int32 *pwidth, l_int32 *pheight, l_int32 *pbps, l_int32 *pspp, l_int32 *piscmap );
l_ok pixWriteStreamSpix ( FILE *fp, PIX *pix );
PIX * pixReadMemSpix ( const l_uint8 *data, size_t size );
l_ok pixWriteMemSpix ( l_uint8 **pdata, size_t *psize, PIX *pix );
l_ok pixSerializeToMemory ( PIX *pixs, l_uint32 **pdata, size_t *pnbytes );
PIX * pixDeserializeFromMemory ( const l_uint32 *data, size_t nbytes );
L_STACK * lstackCreate ( l_int32 nalloc );
void lstackDestroy ( L_STACK **plstack, l_int32 freeflag );
l_ok lstackAdd ( L_STACK *lstack, void *item );
void * lstackRemove ( L_STACK *lstack );
l_int32 lstackGetCount ( L_STACK *lstack );
l_ok lstackPrint ( FILE *fp, L_STACK *lstack );
L_STRCODE * strcodeCreate ( l_int32 fileno );
l_ok strcodeCreateFromFile ( const char *filein, l_int32 fileno, const char *outdir );
l_ok strcodeGenerate ( L_STRCODE *strcode, const char *filein, const char *type );
l_int32 strcodeFinalize ( L_STRCODE **pstrcode, const char *outdir );
l_int32 l_getStructStrFromFile ( const char *filename, l_int32 field, char **pstr );
l_ok pixFindStrokeLength ( PIX *pixs, l_int32 *tab8, l_int32 *plength );
l_ok pixFindStrokeWidth ( PIX *pixs, l_float32 thresh, l_int32 *tab8, l_float32 *pwidth, NUMA **pnahisto );
NUMA * pixaFindStrokeWidth ( PIXA *pixa, l_float32 thresh, l_int32 *tab8, l_int32 debug );
PIXA * pixaModifyStrokeWidth ( PIXA *pixas, l_float32 targetw );
PIX * pixModifyStrokeWidth ( PIX *pixs, l_float32 width, l_float32 targetw );
PIXA * pixaSetStrokeWidth ( PIXA *pixas, l_int32 width, l_int32 thinfirst, l_int32 connectivity );
PIX * pixSetStrokeWidth ( PIX *pixs, l_int32 width, l_int32 thinfirst, l_int32 connectivity );
l_int32 * sudokuReadFile ( const char *filename );
l_int32 * sudokuReadString ( const char *str );
L_SUDOKU * sudokuCreate ( l_int32 *array );
void sudokuDestroy ( L_SUDOKU **psud );
l_int32 sudokuSolve ( L_SUDOKU *sud );
l_ok sudokuTestUniqueness ( l_int32 *array, l_int32 *punique );
L_SUDOKU * sudokuGenerate ( l_int32 *array, l_int32 seed, l_int32 minelems, l_int32 maxtries );
l_int32 sudokuOutput ( L_SUDOKU *sud, l_int32 arraytype );
PIX * pixAddSingleTextblock ( PIX *pixs, L_BMF *bmf, const char *textstr, l_uint32 val, l_int32 location, l_int32 *poverflow );
PIX * pixAddTextlines ( PIX *pixs, L_BMF *bmf, const char *textstr, l_uint32 val, l_int32 location );
l_ok pixSetTextblock ( PIX *pixs, L_BMF *bmf, const char *textstr, l_uint32 val, l_int32 x0, l_int32 y0, l_int32 wtext, l_int32 firstindent, l_int32 *poverflow );
l_ok pixSetTextline ( PIX *pixs, L_BMF *bmf, const char *textstr, l_uint32 val, l_int32 x0, l_int32 y0, l_int32 *pwidth, l_int32 *poverflow );
PIXA * pixaAddTextNumber ( PIXA *pixas, L_BMF *bmf, NUMA *na, l_uint32 val, l_int32 location );
PIXA * pixaAddTextlines ( PIXA *pixas, L_BMF *bmf, SARRAY *sa, l_uint32 val, l_int32 location );
l_ok pixaAddPixWithText ( PIXA *pixa, PIX *pixs, l_int32 reduction, L_BMF *bmf, const char *textstr, l_uint32 val, l_int32 location );
SARRAY * bmfGetLineStrings ( L_BMF *bmf, const char *textstr, l_int32 maxw, l_int32 firstindent, l_int32 *ph );
NUMA * bmfGetWordWidths ( L_BMF *bmf, const char *textstr, SARRAY *sa );
l_ok bmfGetStringWidth ( L_BMF *bmf, const char *textstr, l_int32 *pw );
SARRAY * splitStringToParagraphs ( char *textstr, l_int32 splitflag );
PIX * pixReadTiff ( const char *filename, l_int32 n );
PIX * pixReadStreamTiff ( FILE *fp, l_int32 n );
l_ok pixWriteTiff ( const char *filename, PIX *pix, l_int32 comptype, const char *modestr );
l_ok pixWriteTiffCustom ( const char *filename, PIX *pix, l_int32 comptype, const char *modestr, NUMA *natags, SARRAY *savals, SARRAY *satypes, NUMA *nasizes );
l_ok pixWriteStreamTiff ( FILE *fp, PIX *pix, l_int32 comptype );
l_ok pixWriteStreamTiffWA ( FILE *fp, PIX *pix, l_int32 comptype, const char *modestr );
PIX * pixReadFromMultipageTiff ( const char *fname, size_t *poffset );
PIXA * pixaReadMultipageTiff ( const char *filename );
l_ok pixaWriteMultipageTiff ( const char *fname, PIXA *pixa );
l_ok writeMultipageTiff ( const char *dirin, const char *substr, const char *fileout );
l_ok writeMultipageTiffSA ( SARRAY *sa, const char *fileout );
l_ok fprintTiffInfo ( FILE *fpout, const char *tiffile );
l_ok tiffGetCount ( FILE *fp, l_int32 *pn );
l_ok getTiffResolution ( FILE *fp, l_int32 *pxres, l_int32 *pyres );
l_ok readHeaderTiff ( const char *filename, l_int32 n, l_int32 *pw, l_int32 *ph, l_int32 *pbps, l_int32 *pspp, l_int32 *pres, l_int32 *pcmap, l_int32 *pformat );
l_ok freadHeaderTiff ( FILE *fp, l_int32 n, l_int32 *pw, l_int32 *ph, l_int32 *pbps, l_int32 *pspp, l_int32 *pres, l_int32 *pcmap, l_int32 *pformat );
l_ok readHeaderMemTiff ( const l_uint8 *cdata, size_t size, l_int32 n, l_int32 *pw, l_int32 *ph, l_int32 *pbps, l_int32 *pspp, l_int32 *pres, l_int32 *pcmap, l_int32 *pformat );
l_ok findTiffCompression ( FILE *fp, l_int32 *pcomptype );
l_ok extractG4DataFromFile ( const char *filein, l_uint8 **pdata, size_t *pnbytes, l_int32 *pw, l_int32 *ph, l_int32 *pminisblack );
PIX * pixReadMemTiff ( const l_uint8 *cdata, size_t size, l_int32 n );
PIX * pixReadMemFromMultipageTiff ( const l_uint8 *cdata, size_t size, size_t *poffset );
PIXA * pixaReadMemMultipageTiff ( const l_uint8 *data, size_t size );
l_ok pixaWriteMemMultipageTiff ( l_uint8 **pdata, size_t *psize, PIXA *pixa );
l_ok pixWriteMemTiff ( l_uint8 **pdata, size_t *psize, PIX *pix, l_int32 comptype );
l_ok pixWriteMemTiffCustom ( l_uint8 **pdata, size_t *psize, PIX *pix, l_int32 comptype, NUMA *natags, SARRAY *savals, SARRAY *satypes, NUMA *nasizes );
l_int32 setMsgSeverity ( l_int32 newsev );
l_int32 returnErrorInt ( const char *msg, const char *procname, l_int32 ival );
l_float32 returnErrorFloat ( const char *msg, const char *procname, l_float32 fval );
void * returnErrorPtr ( const char *msg, const char *procname, void *pval );
l_ok filesAreIdentical ( const char *fname1, const char *fname2, l_int32 *psame );
l_uint16 convertOnLittleEnd16 ( l_uint16 shortin );
l_uint16 convertOnBigEnd16 ( l_uint16 shortin );
l_uint32 convertOnLittleEnd32 ( l_uint32 wordin );
l_uint32 convertOnBigEnd32 ( l_uint32 wordin );
l_ok fileCorruptByDeletion ( const char *filein, l_float32 loc, l_float32 size, const char *fileout );
l_ok fileCorruptByMutation ( const char *filein, l_float32 loc, l_float32 size, const char *fileout );
l_ok genRandomIntegerInRange ( l_int32 range, l_int32 seed, l_int32 *pval );
l_int32 lept_roundftoi ( l_float32 fval );
l_ok l_hashStringToUint64 ( const char *str, l_uint64 *phash );
l_ok l_hashPtToUint64 ( l_int32 x, l_int32 y, l_uint64 *phash );
l_ok l_hashFloat64ToUint64 ( l_int32 nbuckets, l_float64 val, l_uint64 *phash );
l_ok findNextLargerPrime ( l_int32 start, l_uint32 *pprime );
l_ok lept_isPrime ( l_uint64 n, l_int32 *pis_prime, l_uint32 *pfactor );
l_uint32 convertIntToGrayCode ( l_uint32 val );
l_uint32 convertGrayCodeToInt ( l_uint32 val );
char * getLeptonicaVersion (  );
void startTimer ( void );
l_float32 stopTimer ( void );
L_TIMER startTimerNested ( void );
l_float32 stopTimerNested ( L_TIMER rusage_start );
void l_getCurrentTime ( l_int32 *sec, l_int32 *usec );
L_WALLTIMER * startWallTimer ( void );
l_float32 stopWallTimer ( L_WALLTIMER **ptimer );
char * l_getFormattedDate (  );
char * stringNew ( const char *src );
l_ok stringCopy ( char *dest, const char *src, l_int32 n );
char * stringCopySegment ( const char *src, l_int32 start, l_int32 nbytes );
l_ok stringReplace ( char **pdest, const char *src );
l_int32 stringLength ( const char *src, size_t size );
l_int32 stringCat ( char *dest, size_t size, const char *src );
char * stringConcatNew ( const char *first, ... );
char * stringJoin ( const char *src1, const char *src2 );
l_ok stringJoinIP ( char **psrc1, const char *src2 );
char * stringReverse ( const char *src );
char * strtokSafe ( char *cstr, const char *seps, char **psaveptr );
l_ok stringSplitOnToken ( char *cstr, const char *seps, char **phead, char **ptail );
l_ok stringCheckForChars ( const char *src, const char *chars, l_int32 *pfound );
char * stringRemoveChars ( const char *src, const char *remchars );
l_int32 stringFindSubstr ( const char *src, const char *sub, l_int32 *ploc );
char * stringReplaceSubstr ( const char *src, const char *sub1, const char *sub2, l_int32 *pfound, l_int32 *ploc );
char * stringReplaceEachSubstr ( const char *src, const char *sub1, const char *sub2, l_int32 *pcount );
L_DNA * arrayFindEachSequence ( const l_uint8 *data, size_t datalen, const l_uint8 *sequence, size_t seqlen );
l_ok arrayFindSequence ( const l_uint8 *data, size_t datalen, const l_uint8 *sequence, size_t seqlen, l_int32 *poffset, l_int32 *pfound );
void * reallocNew ( void **pindata, l_int32 oldsize, l_int32 newsize );
l_uint8 * l_binaryRead ( const char *filename, size_t *pnbytes );
l_uint8 * l_binaryReadStream ( FILE *fp, size_t *pnbytes );
l_uint8 * l_binaryReadSelect ( const char *filename, size_t start, size_t nbytes, size_t *pnread );
l_uint8 * l_binaryReadSelectStream ( FILE *fp, size_t start, size_t nbytes, size_t *pnread );
l_ok l_binaryWrite ( const char *filename, const char *operation, const void *data, size_t nbytes );
size_t nbytesInFile ( const char *filename );
size_t fnbytesInFile ( FILE *fp );
l_uint8 * l_binaryCopy ( l_uint8 *datas, size_t size );
l_ok fileCopy ( const char *srcfile, const char *newfile );
l_ok fileConcatenate ( const char *srcfile, const char *destfile );
l_ok fileAppendString ( const char *filename, const char *str );
FILE * fopenReadStream ( const char *filename );
FILE * fopenWriteStream ( const char *filename, const char *modestring );
FILE * fopenReadFromMemory ( const l_uint8 *data, size_t size );
FILE * fopenWriteWinTempfile (  );
FILE * lept_fopen ( const char *filename, const char *mode );
l_ok lept_fclose ( FILE *fp );
void * lept_calloc ( size_t nmemb, size_t size );
void lept_free ( void *ptr );
l_int32 lept_mkdir ( const char *subdir );
l_int32 lept_rmdir ( const char *subdir );
void lept_direxists ( const char *dir, l_int32 *pexists );
l_int32 lept_rm_match ( const char *subdir, const char *substr );
l_int32 lept_rm ( const char *subdir, const char *tail );
l_int32 lept_rmfile ( const char *filepath );
l_int32 lept_mv ( const char *srcfile, const char *newdir, const char *newtail, char **pnewpath );
l_int32 lept_cp ( const char *srcfile, const char *newdir, const char *newtail, char **pnewpath );
void callSystemDebug ( const char *cmd );
l_ok splitPathAtDirectory ( const char *pathname, char **pdir, char **ptail );
l_ok splitPathAtExtension ( const char *pathname, char **pbasename, char **pextension );
char * pathJoin ( const char *dir, const char *fname );
char * appendSubdirs ( const char *basedir, const char *subdirs );
l_ok convertSepCharsInPath ( char *path, l_int32 type );
char * genPathname ( const char *dir, const char *fname );
l_ok makeTempDirname ( char *result, size_t nbytes, const char *subdir );
l_ok modifyTrailingSlash ( char *path, size_t nbytes, l_int32 flag );
char * l_makeTempFilename (  );
l_int32 extractNumberFromFilename ( const char *fname, l_int32 numpre, l_int32 numpost );
PIX * pixSimpleCaptcha ( PIX *pixs, l_int32 border, l_int32 nterms, l_uint32 seed, l_uint32 color, l_int32 cmapflag );
PIX * pixRandomHarmonicWarp ( PIX *pixs, l_float32 xmag, l_float32 ymag, l_float32 xfreq, l_float32 yfreq, l_int32 nx, l_int32 ny, l_uint32 seed, l_int32 grayval );
PIX * pixWarpStereoscopic ( PIX *pixs, l_int32 zbend, l_int32 zshiftt, l_int32 zshiftb, l_int32 ybendt, l_int32 ybendb, l_int32 redleft );
PIX * pixStretchHorizontal ( PIX *pixs, l_int32 dir, l_int32 type, l_int32 hmax, l_int32 operation, l_int32 incolor );
PIX * pixStretchHorizontalSampled ( PIX *pixs, l_int32 dir, l_int32 type, l_int32 hmax, l_int32 incolor );
PIX * pixStretchHorizontalLI ( PIX *pixs, l_int32 dir, l_int32 type, l_int32 hmax, l_int32 incolor );
PIX * pixQuadraticVShear ( PIX *pixs, l_int32 dir, l_int32 vmaxt, l_int32 vmaxb, l_int32 operation, l_int32 incolor );
PIX * pixQuadraticVShearSampled ( PIX *pixs, l_int32 dir, l_int32 vmaxt, l_int32 vmaxb, l_int32 incolor );
PIX * pixQuadraticVShearLI ( PIX *pixs, l_int32 dir, l_int32 vmaxt, l_int32 vmaxb, l_int32 incolor );
PIX * pixStereoFromPair ( PIX *pix1, PIX *pix2, l_float32 rwt, l_float32 gwt, l_float32 bwt );
L_WSHED * wshedCreate ( PIX *pixs, PIX *pixm, l_int32 mindepth, l_int32 debugflag );
void wshedDestroy ( L_WSHED **pwshed );
l_ok wshedApply ( L_WSHED *wshed );
l_ok wshedBasins ( L_WSHED *wshed, PIXA **ppixa, NUMA **pnalevels );
PIX * wshedRenderFill ( L_WSHED *wshed );
PIX * wshedRenderColors ( L_WSHED *wshed );
PIX * pixReadStreamWebP ( FILE *fp );
PIX * pixReadMemWebP ( const l_uint8 *filedata, size_t filesize );
l_ok readHeaderWebP ( const char *filename, l_int32 *pw, l_int32 *ph, l_int32 *pspp );
l_ok readHeaderMemWebP ( const l_uint8 *data, size_t size, l_int32 *pw, l_int32 *ph, l_int32 *pspp );
l_ok pixWriteWebP ( const char *filename, PIX *pixs, l_int32 quality, l_int32 lossless );
l_ok pixWriteStreamWebP ( FILE *fp, PIX *pixs, l_int32 quality, l_int32 lossless );
l_ok pixWriteMemWebP ( l_uint8 **pencdata, size_t *pencsize, PIX *pixs, l_int32 quality, l_int32 lossless );
l_int32 l_jpegSetQuality ( l_int32 new_quality );
void setLeptDebugOK ( l_int32 allow );
l_ok pixaWriteFiles ( const char *rootname, PIXA *pixa, l_int32 format );
l_ok pixWriteDebug ( const char *fname, PIX *pix, l_int32 format );
l_ok pixWrite ( const char *fname, PIX *pix, l_int32 format );
l_ok pixWriteAutoFormat ( const char *filename, PIX *pix );
l_ok pixWriteStream ( FILE *fp, PIX *pix, l_int32 format );
l_ok pixWriteImpliedFormat ( const char *filename, PIX *pix, l_int32 quality, l_int32 progressive );
l_int32 pixChooseOutputFormat ( PIX *pix );
l_int32 getImpliedFileFormat ( const char *filename );
l_ok pixGetAutoFormat ( PIX *pix, l_int32 *pformat );
const char * getFormatExtension ( l_int32 format );
l_ok pixWriteMem ( l_uint8 **pdata, size_t *psize, PIX *pix, l_int32 format );
l_ok l_fileDisplay ( const char *fname, l_int32 x, l_int32 y, l_float32 scale );
l_ok pixDisplay ( PIX *pixs, l_int32 x, l_int32 y );
l_ok pixDisplayWithTitle ( PIX *pixs, l_int32 x, l_int32 y, const char *title, l_int32 dispflag );
l_ok pixSaveTiled ( PIX *pixs, PIXA *pixa, l_float32 scalefactor, l_int32 newrow, l_int32 space, l_int32 dp );
l_ok pixSaveTiledOutline ( PIX *pixs, PIXA *pixa, l_float32 scalefactor, l_int32 newrow, l_int32 space, l_int32 linewidth, l_int32 dp );
l_ok pixSaveTiledWithText ( PIX *pixs, PIXA *pixa, l_int32 outwidth, l_int32 newrow, l_int32 space, l_int32 linewidth, L_BMF *bmf, const char *textstr, l_uint32 val, l_int32 location );
void l_chooseDisplayProg ( l_int32 selection );
l_ok pixDisplayWrite ( PIX *pixs, l_int32 reduction );
l_uint8 * zlibCompress ( l_uint8 *datain, size_t nin, size_t *pnout );
l_uint8 * zlibUncompress ( l_uint8 *datain, size_t nin, size_t *pnout );

"""
)


ffibuilder.set_source(
    "leptonica._leptonica",
    "#include <leptonica/allheaders.h>",
    libraries=['lept'],
    include_dirs=['/usr/local/include'],
    library_dirs=['/usr/local/lib'],
)

if __name__ == '__main__':
    ffibuilder.compile(verbose=True)
