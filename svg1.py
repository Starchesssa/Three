
import cv2
import numpy as np
import subprocess
import os

# Load grayscale image
image = cv2.imread("Generated Image July 26, 2025 - 2_25PM.jpeg", cv2.IMREAD_GRAYSCALE)

# Resize (optional, for speed)
image = cv2.resize(image, (0, 0), fx=0.4, fy=0.4)

# Smooth to reduce noise
image = cv2.GaussianBlur(image, (5, 5), 0)

# Define thresholds (brightness cutoffs)
thresholds = [60, 120, 180, 240]

# Neon gradient palette (dark → bright)
colors = [
    "#0B032D",  # dark purple
    "#7B2FF7",  # violet
    "#F107A3",  # neon pink
    "#0F62FE"   # neon blue
]

# Create layers for each threshold
svg_layers = []
for i, t in enumerate(thresholds):
    _, layer = cv2.threshold(image, t, 255, cv2.THRESH_BINARY)

    pbm_file = f"temp_{i}.pbm"
    svg_file = f"layer_{i}.svg"

    # Save PBM
    cv2.imwrite(pbm_file, layer)

    # Run Potrace on each layer
    subprocess.run([
        "potrace", pbm_file, "-s", "-o", svg_file,
        "--turdsize", "50",
        "--opttolerance", "0.2",
        "--flat"
    ])

    # Read back the SVG and inject fill color
    with open(svg_file, "r") as f:
        svg_content = f.read()
    
    # Replace fill="black" with neon color
    svg_content = svg_content.replace("fill=\"black\"", f"fill=\"{colors[i]}\"")
    svg_content = svg_content.replace("fill=\"white\"", "fill=\"none\"")

    # Store layer
    svg_layers.append(svg_content)

# Merge layers into one SVG
final_svg = """<svg xmlns="http://www.w3.org/2000/svg" version="1.1">\n"""
for layer in svg_layers:
    # Remove XML header from each layer before merging
    cleaned = "\n".join(layer.splitlines()[6:])
    final_svg += cleaned + "\n"
final_svg += "</svg>"

# Save final neon UI SVG
with open("hotel_neon.svg", "w") as f:
    f.write(final_svg)

print("✅ Neon UI-style SVG saved as hotel_neon.svg")
