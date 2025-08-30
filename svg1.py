import cv2
import numpy as np

# Load image
image = cv2.imread("Generated Image July 26, 2025 - 2_25PM.jpeg")
image = cv2.resize(image, (0, 0), fx=0.6, fy=0.6)

# Reshape image into list of pixels
Z = image.reshape((-1, 3))
Z = np.float32(Z)

# KMeans to reduce to 5 colors
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 20, 1.0)
K = 5
_, labels, centers = cv2.kmeans(Z, K, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

# Convert centers to uint8
centers = np.uint8(centers)
quantized = centers[labels.flatten()]
quantized = quantized.reshape(image.shape)

# 🎨 Define your custom palette (OpenCV uses BGR order!)
palette = np.array([
    [20, 20, 20],       # dark (blackish)
    [80, 50, 180],      # purple
    [0, 180, 200],      # teal
    [0, 200, 100],      # green
    [255, 220, 0]       # bright yellow
], dtype=np.uint8)

# Map each KMeans cluster color to nearest palette color
def closest_color(color, palette):
    diffs = np.linalg.norm(palette - color, axis=1)
    return palette[np.argmin(diffs)]

out = np.zeros_like(quantized)
for i in range(quantized.shape[0]):
    for j in range(quantized.shape[1]):
        out[i, j] = closest_color(quantized[i, j], palette)

cv2.imwrite("art_colored.jpg", out)
print("✅ Saved colorful art image as art_colored.jpg")
