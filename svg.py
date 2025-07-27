
import cv2
import numpy as np
import subprocess

# Load image in grayscale
image = cv2.imread("Generated Image July 26, 2025 - 2_25PM.jpeg", cv2.IMREAD_GRAYSCALE)

# Use adaptive thresholding to better detect fine details and faint lines
binary = cv2.adaptiveThreshold(
    image, 255,
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY_INV,  # Invert so black becomes white for PBM
    11, 2
)

# Optional: thicken lines slightly to ensure visibility (can remove if not needed)
kernel = np.ones((1, 1), np.uint8)  # 1x1 to preserve tiny shapes
binary = cv2.dilate(binary, kernel, iterations=1)

# Save as PBM (Portable Bitmap) for Potrace
cv2.imwrite("temp.pbm", binary)

# Convert to SVG using Potrace with detailed settings
subprocess.run([
    "potrace", "temp.pbm",
    "-s",                      # Output SVG
    "--turdsize", "0",         # Keep even the tiniest paths
    "--alphamax", "1",         # Avoid curve simplification
    "--flat",                  # Prevent smoothing into Bezier curves
    "-o", "output.svg"
])

print("✅ SVG saved as output.svg with full detail.")
