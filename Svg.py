
import cv2
import numpy as np
import subprocess

# Load your image (convert to grayscale)
image = cv2.imread("Generated Image July 26, 2025 - 2_25PM.jpeg", cv2.IMREAD_GRAYSCALE)

# Threshold to binary
_, binary = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

# Save as PBM (portable bitmap format)
cv2.imwrite("temp.pbm", binary)

# Use Potrace to convert PBM to SVG
subprocess.run(["potrace", "temp.pbm", "-s", "-o", "output.svg"])

print("✅ SVG saved as output.svg")
