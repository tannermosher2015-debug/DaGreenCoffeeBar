"""Optimize Da Green real photos into web-ready assets.
Source originals live in images/source/ (archived, gitignored).
Outputs go to images/. Re-runnable."""
from PIL import Image, ImageOps
from pathlib import Path

ROOT = Path(__file__).parent
SRC = ROOT / "images" / "source"
OUT = ROOT / "images"
OUT.mkdir(parents=True, exist_ok=True)


def load(name):
    im = Image.open(SRC / name)
    im = ImageOps.exif_transpose(im)  # respect camera orientation
    return im.convert("RGB")


def save(im, name, w=None, q=82):
    if w and im.width > w:
        h = round(im.height * w / im.width)
        im = im.resize((w, h), Image.LANCZOS)
    im.save(OUT / name, "JPEG", quality=q, optimize=True, progressive=True)
    print(f"  {name:28s} {im.width}x{im.height}  {(OUT/name).stat().st_size//1024} KB")


def crop_ratio(im, ratio, anchor=0.5):
    """Center-ish crop to target w/h ratio. anchor=vertical focus 0..1."""
    w, h = im.size
    target = ratio
    cur = w / h
    if cur > target:  # too wide -> crop width
        nw = round(h * target)
        x = (w - nw) // 2
        return im.crop((x, 0, x + nw, h))
    else:  # too tall -> crop height
        nh = round(w / target)
        y = round((h - nh) * anchor)
        return im.crop((0, y, w, y + nh))


print("Exterior:")
ext = load("exterior_IMG6167.jpg")
print(f"  original {ext.width}x{ext.height}")
save(ext, "exterior.jpg", w=1200, q=80)                        # full portrait, hero (LCP — keep lean)
save(crop_ratio(ext, 16/10, anchor=0.42), "exterior-wide.jpg", w=1600)  # landscape hero crop

print("Garden:")
gar = load("garden_DSC06123.jpg")
print(f"  original {gar.width}x{gar.height}")
save(gar, "garden.jpg", w=1600)                                # landscape feature
save(crop_ratio(gar, 1/1, anchor=0.5), "garden-square.jpg", w=1000)     # square detail

print("Neon sign detail (cropped from exterior):")
neon = ext.crop((900, 640, 1980, 1240))                        # iconic "DA GREEN COFFEE BAR" neon
save(neon, "neon-sign.jpg", w=1080, q=84)                      # no upscale; ~560px display

print("done")
