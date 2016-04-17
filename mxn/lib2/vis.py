"""Visualization: plots, images, animations, color maps, annotations."""

import pylab as plt
import numpy as np
import matplotlib as mpl
import PIL


def stats_legend(text, fig=plt, fontsize=9, **kwargs):
    _text = "\n".join(text) if isinstance(text,list) else text
    fig.annotate(_text,xy=(0.04, 0.9),xytext=(0.04,0.9),
                 textcoords="axes fraction",
                 xycoords="axes fraction", fontsize=fontsize,
                 **kwargs)


def cmap_to_pil_palette(cmap):
    """convert a matplotlib colormap into a PIL palette"""
    # return (255.*np.array(
    #     map(lambda x: cmap(x)[0:3], np.linspace(0., 1.,256)))
    #         .ravel()).astype('int')
    return (255. * np.array(
        [cmap(x)[:3] for x in np.linspace(0,1,256)]).ravel().astype('int'))


def save_pil_image(img, filename, cmap="jet", mask=None, flip_vert=True):
    if mask is None:
        nimg = normscl(img)
    else:
        x = img[np.where(mask)]
        nimg = bytscl(img, np.min(x), np.max(x))/255.
    im = PIL.Image.fromarray(np.uint8(255.*plt.get_cmap(cmap)(nimg)))
    if flip_vert:
        im = im.transpose(PIL.Image.FLIP_TOP_BOTTOM)
    if mask is not None:
        alpha = PIL.Image.fromarray(np.uint8(mask)*255)
        if flip_vert:
            alpha = alpha.transpose(PIL.Image.FLIP_TOP_BOTTOM)
        im.putalpha(alpha)
    #im.show()
    im.save(filename)
    return filename, im


def save_colorbar(img=None, vmin=None, vmax=None, cmap="jet",
                  filename=None, title="Colorbar", lab=""):
    """Save a png image of a colorbar.
    One can use this code directly, or use it as an example to modify."""
    fig = plt.figure(figsize=(1.0, 4.0), facecolor=None, frameon=False)
    ax = fig.add_axes([0.0, 0.05, 0.2, 0.9])
    if vmin is None: vmin = np.min(img)
    if vmax is None: vmax = np.max(img)
    cb = mpl.colorbar.ColorbarBase(
        ax, cmap=cmap, norm=mpl.colors.Normalize(vmin=vmin, vmax=vmax))
    cb.set_label(title, rotation=-90, color='k', labelpad=20)
    if filename is None:
        filename = 'colorbar_'+lab+'.png'
    fig.savefig(filename, transparent=False, format='png')
    return filename, cb


def cmap_idl4():
    """Provides a colormap, based on IDL colortable==4.
    Got it out from IDL using:
      IDL> loadct,4
      IDL> TVLCT, R, G, B, /GET
      IDL> print, r,g,b
    """
    r="0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   7  15  22  30  37  45  52  60  67  75  82  90  97 105 112 120 125 130 135 140 145 150 155 160 165 170 175 180 185 190 195 200 200 201 201 202 202 203 203 204 204 205 205 206 206 207 207 208 208 209 209 210 210 211 211 212 212 213 213 214 214 215 215 216 216 217 217 218 218 219 219 220 220 221 221 222 222 223 223 224 224 225 225 226 226 227 227 228 228 229 229 230 230 231 231 232 232 233 233 234 234 235 235 236 236 237 237 238 238 239 239 240 240 241 241 242 242 243 243 244 244 245 245 246 246 247 247 248 248 249 249 250 250 251 251 252 252 253 253 254 254 255 255"
    g="0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   3   6   9  12  15  18  21  25  28  31  34  37  40  43  46  50  53  56  59  62  65  68  71  75  78  81  84  87  90  93  96 100 103 106 109 112 115 118 121 125 128 131 134 137 140 143 146 150 150 150 150 150 150 150 150 150 150 150 150 150 150 150 150 150 149 148 148 147 146 146 145 145 144 143 143 142 141 141 140 140 137 135 132 130 127 125 122 120 117 115 112 110 107 105 102 100  93  87  81  75  68  62  56  50  43  37  31  25  18  12   6   0   2   4   6   9  11  13  16  18  20  23  25  27  29  32  34  36  39  41  43  46  48  50  53  55  57  59  62  64  66  69  71  73  76  78  80  83  85  87  89  92  94  96  99 101 103 106 108 110 113 115 117 119 122 124 126 129 131 133 136 138 140 142 145 147 149 152 154 156 159 161 163 166 168 170 172 175 177 179 182 184 186 189 191 193 196 198 200 202 205 207 209 212 214 216 219 221 223 226 228 230 232 235 237 239 242 244 246 249 251 253 255"
    b="0   2   4   6   8  10  12  14  16  18  20  22  25  27  29  31  33  35  37  39  41  43  45  47  50  52  54  56  58  60  62  64  66  68  70  72  75  77  79  81  83  85  87  89  91  93  95  97 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100  96  93  90  87  84  81  78  75  71  68  65  62  59  56  53  50  46  43  40  37  34  31  28  25  21  18  15  12   9   6   3   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0  0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0"
    rm = [tuple([i/255,]+[int(x)/255,]*2) for i,x in enumerate(r.split())]
    gm = [tuple([i/255,]+[int(x)/255,]*2) for i,x in enumerate(g.split())]
    bm = [tuple([i/255,]+[int(x)/255,]*2) for i,x in enumerate(b.split())]
    cdict = {'red':rm, 'green':gm, 'blue':bm}
    cmap = plt.matplotlib.colors.LinearSegmentedColormap('idl4',cdict,256)
    return cmap
