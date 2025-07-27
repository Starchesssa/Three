
import cv2
import numpy as np
import subprocess

# Load image in grayscale
image = cv2.imread("Generated Image July 26, 2025 - 2_25PM.jpeg", cv2.IMREAD_GRAYSCALE)

# Invert the image logic: anything that is not white (255) becomes black
# This turns all non-white into black (for Potrace to trace)
binary = np.where(image < 250, 0, 255).astype(np.uint8)

# Save binary as PBM
cv2.imwrite("temp.pbm", binary)

# Use Potrace to convert PBM to SVG, keeping all details
subprocess.run([
    "potrace", "temp.pbm",
    "-s",
    "--turdsize", "0",       # Keep even the smallest details
    "--alphamax", "1",       # Preserve shape accuracy
    "-o", "output.svg"
])

print("✅ SVG saved as output.svg (everything not white is now traced)")
