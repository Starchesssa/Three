import cv2
import numpy as np

# Load image
image = cv2.imread("Generated Image July 26, 2025 - 2_25PM.jpeg")
image = cv2.resize(image, (0, 0), fx=0.6, fy=0.6)

# Convert to grayscale for brightness mapping
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Normalize brightness to 0–4 (5 levels)
levels = cv2.equalizeHist(gray)
levels = np.floor_divide(levels, 51)  # 0–4

# 🎨 Define your channel colors here (BGR format in OpenCV!)
palette = [
    (20, 20, 20),      # darkest (blackish)
    (80, 50, 180),     # dark purple/blue
    (0, 180, 200),     # teal/cyan
    (0, 200, 100),     # greenish
    (255, 220, 0)      # brightest (yellow)
]

# Create an output image using the palette
art = np.zeros_like(image)
for i, color in enumerate(palette):
    art[levels == i] = color

cv2.imwrite("art_palette.jpg", art)
print("✅ Saved art image with custom channel colors (art_palette.jpg)")
