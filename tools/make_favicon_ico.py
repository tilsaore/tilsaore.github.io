"""Downscale the rendered tab icons to their exact sizes and build favicon.ico.

Run after `node tools/make_icons.js` (tab icons are rendered at 8x for crisp edges).
"""
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
ICONS = ROOT / "icons"

for size in (16, 32, 48):
    path = ICONS / f"favicon-{size}.png"
    img = Image.open(path).convert("RGBA")
    if img.size != (size, size):
        img.resize((size, size), Image.LANCZOS).save(path, optimize=True)

# favicon.ico (16, 32, 48 px) for browsers and tools that request /favicon.ico directly.
Image.open(ICONS / "favicon-48.png").save(ROOT / "favicon.ico", sizes=[(16, 16), (32, 32), (48, 48)])
print("wrote favicon.ico and resized tab icons")
