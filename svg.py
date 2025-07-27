
import vtracer
from PIL import Image

# Convert image to PNG first (vtracer prefers PNG or BMP)
img = Image.open("Generated Image July 26, 2025 - 2_25PM.jpeg").convert("RGBA")
img.save("input.png")

# Convert to SVG using vtracer
svg_string = vtracer.convert_image_to_svg(
    filename="input.png",
    mode="detail",             # or "polygon", "art"
    color_precision="low",     # can be "low", "medium", "high"
    filter_speckle=True,
    filter_curve=True,
)

# Save SVG
with open("output.svg", "w") as f:
    f.write(svg_string)

print("✅ SVG saved as output.svg")
