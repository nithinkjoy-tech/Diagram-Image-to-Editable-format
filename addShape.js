const PPTX = require("nodejs-pptx");
let pptx = new PPTX.Composer();

exports.addShape = async shapeslist => {
  finalshape = [];

  for (shape of shapeslist) {
    cx = shape[3];
    cy = shape[4];

    if (cx > 15 && cy > 15) {
      finalshape.push(shape);
    }
  }

  await pptx.compose(async pres => {
    await pres.addSlide(slide => {
      finalshape.forEach((_, i) => {
        shapename = "PPTX.ShapeTypes." + _[0];
        slide.addShape(shape => {
          shape.type(eval(shapename)).x(_[1]).y(_[2]).cx(_[3]).cy(_[4]).color("ffffff");
        });
      });
    });
  });

  await pptx.save(`./shapes-test.pptx`);
};
