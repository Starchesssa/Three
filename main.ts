
import {makeScene2D} from '@revideo/2d';
import {Rect, Txt} from '@revideo/2d';
import {createVideo} from '@revideo/core';

createVideo({
  width: 1280,
  height: 720,
  fps: 30,
  durationInFrames: 150, // 5 seconds
  scenes: [
    makeScene2D(function* (view) {
      // Create a rectangle background
      const rect = new Rect({width: 1280, height: 720, fill: 'black'});
      view.add(rect);

      // Create a text element
      const text = new Txt('Hello Revideo!', {
        fontSize: 80,
        fill: 'white',
      });
      view.add(text);

      // Animate text
      yield* text.opacity(1, 1); // Fade in over 1 second
    }),
  ],
});
