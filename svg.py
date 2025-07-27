
import vtracer

# Convert image to SVG using VTracer
vtracer.convert(
    input_path="Generated Image July 26, 2025 - 2_25PM.jpeg",  # Input image
    output_path="output.svg",                                   # Output SVG file
    mode="spline",                                               # Better curves
    color_mode="grayscale",                                      # Keeps dark/light details
    filter_speckle=0,                                            # Keeps tiny shapes
    layer_difference=0.1                                         # Captures faint lines too
)

print("✅ SVG saved as output.svg")
