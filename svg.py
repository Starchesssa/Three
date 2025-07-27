
import subprocess

# Input and output file names
input_file = "Generated Image July 26, 2025 - 2_25PM.jpeg"
output_file = "output.svg"

# Run vtracer using subprocess
subprocess.run([
    "vtracer",
    "--input", input_file,
    "--output", output_file,
    "--mode", "spline",         # or "polygon"
    "--colormode", "binary",    # or "grayscale", "color"
])

print("✅ SVG saved as", output_file)
