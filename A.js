
// install: npm install jimp

const Jimp = require("jimp");

// Define your brand palette (dark to light)
const palette = [
  [20, 20, 20],     // darkest black
  [80, 50, 180],    // purple
  [0, 180, 200],    // teal
  [255, 220, 0]     // yellow
];

// Map brightness to nearest palette color
function mapToPalette(r, g, b) {
  let brightness = (r + g + b) / 3;
  let index = Math.floor((brightness / 255) * (palette.length - 1));
  return palette[index];
}

async function processImage(inputPath, outputPath) {
  const image = await Jimp.read(inputPath);

  image.scan(0, 0, image.bitmap.width, image.bitmap.height, (x, y, idx) => {
    let r = image.bitmap.data[idx + 0];
    let g = image.bitmap.data[idx + 1];
    let b = image.bitmap.data[idx + 2];

    let [nr, ng, nb] = mapToPalette(r, g, b);

    image.bitmap.data[idx + 0] = nr;
    image.bitmap.data[idx + 1] = ng;
    image.bitmap.data[idx + 2] = nb;
  });

  await image.writeAsync(outputPath);
  console.log(`✅ Processed: ${outputPath}`);
}

// Example: batch process all images in /input and save to /output
const fs = require("fs");
const path = require("path");

const inputDir = "input_images";
const outputDir = "output_images";

fs.readdirSync(inputDir).forEach(file => {
  if (/\.(jpg|jpeg|png)$/i.test(file)) {
    let inputPath = path.join(inputDir, file);
    let outputPath = path.join(outputDir, "BRANDED_" + file);
    processImage(inputPath, outputPath);
  }
});
