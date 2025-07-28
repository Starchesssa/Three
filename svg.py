
import cv2
import numpy as np
import subprocess

# Load image and grayscale
image = cv2.imread("Generated Image July 26, 2025 - 2_25PM.jpeg", cv2.IMREAD_GRAYSCALE)

# Optional: Resize to reduce complexity
image = cv2.resize(image, (0, 0), fx=0.4, fy=0.4)

# Smooth to reduce noise
image = cv2.GaussianBlur(image, (5, 5), 0)

# Threshold to binary
_, binary = cv2.threshold(image, 200, 255, cv2.THRESH_BINARY)

# Save PBM
cv2.imwrite("temp.pbm", binary)

# Use Potrace with simplification options
subprocess.run([
    "potrace", "temp.pbm", "-s", "-o", "output.svg",
    "--turdsize", "50",
    "--opttolerance", "0.2",
    "--flat"
])

# (Optional) Post-process with SVGO
subprocess.run(["npx", "svgo", "output.svg", "-o", "minimal.svg"])

print("✅ Minimal SVG saved as minimal.svg")
