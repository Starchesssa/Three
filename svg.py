
import cv2
import numpy as np
import subprocess

# Load your grayscale image without modifying it
image = cv2.imread("Generated Image July 26, 2025 - 2_25PM.jpeg", cv2.IMREAD_GRAYSCALE)

# Threshold the image without changing the natural look
# Try values between 80–120 until it matches what you visually see
_, binary = cv2.threshold(image, 105, 255, cv2.THRESH_BINARY)

# Save as PBM (black on white)
cv2.imwrite("temp.pbm", binary)

# Convert to SVG with Potrace, keeping small details
subprocess.run([
    "potrace", "temp.pbm",
    "-s",
    "--turdsize", "0",         # keep all details
    "--alphamax", "1",         # avoid curve simplification
    "-o", "output.svg"
])

print("✅ SVG saved as output.svg (looks like original image)")
