const PptxLib = require('pptx-lib');

// Create a new PowerPoint presentation
const pptx = new PptxLib();

// Add a new slide
const slide = pptx.addSlide();

// Add a shape (e.g. a rectangle) to the slide
const shape = slide.addShape({
  type: 'rect',
  x: 1,
  y: 1,
  w: 5,
  h: 3
});

// Add a border to the shape
shape.options.border = {
  type: 'solid',
  color: '000000',
  width: 3
};

// Save the PowerPoint presentation
pptx.save('test.pptx');
