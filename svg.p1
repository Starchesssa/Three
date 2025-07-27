
import cv2
import numpy as np
import subprocess

# Load image in grayscale
image = cv2.imread("Generated Image July 26, 2025 - 2_25PM.jpeg", cv2.IMREAD_GRAYSCALE)

# Slight contrast stretch to make light lines more distinct but still natural
image = cv2.normalize(image, None, 0, 255, cv2.NORM_MINMAX)

# Threshold to binary (slightly lower value to catch faint lines)
_, binary = cv2.threshold(image, 100, 255, cv2.THRESH_BINARY)

# Optional: very light dilation to ensure thin lines remain visible
kernel = np.ones((1, 1), np.uint8)
binary = cv2.dilate(binary, kernel, iterations=1)

# Save as PBM (white background, black shapes)
cv2.imwrite("temp.pbm", binary)

# Use Potrace to convert PBM to SVG, preserving small details
subprocess.run([
    "potrace", "temp.pbm",
    "-s",
    "--turdsize", "0",         # Keep very small parts
    "--alphamax", "1",         # No simplification
    "-o", "output.svg"
])

print("✅ SVG saved as output.svg (clean and detail-preserved)")
