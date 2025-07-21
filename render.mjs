
import {renderVideo} from '@revideo/renderer';

await renderVideo({
  projectFile: './main.ts', 
  settings: {
    outFile: 'out/video.mp4',
    logProgress: true,
    puppeteer: {
      args: ['--no-sandbox'] // required for GitHub Actions
    }
  }
});
