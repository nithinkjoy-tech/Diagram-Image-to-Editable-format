const PPTX = require("nodejs-pptx");
let pptx = new PPTX.Composer();
const {spawn} = require("child_process");

shapeslist = JSON.parse(process.argv[2]);
inputimagename = process.argv[3];
console.log(inputimagename);
finalshape = [];

for (shape of shapeslist) {
  cx = shape[3];
  cy = shape[4];
  console.log(cx, cy);

  if (cx > 8 && cy > 8) {
    finalshape.push(shape);
  }
}

const run = async () => {
  await pptx.compose(async pres => {
    await pres.addSlide(slide => {
      finalshape.forEach((_, i) => {
        console.log(_);
        shapename = "PPTX.ShapeTypes." + _[0];
        slide.addShape(shape => {
          shape.type(eval(shapename)).x(_[1]).y(_[2]).cx(_[3]).cy(_[4]).color("ffffff");
        });
      });

      //Creating a shape using the object-only syntax.
      //   slide.addShape({ type: PPTX.ShapeTypes.OVAL, x: 150, y: 50, cx: 300, cy: 300, color: '0000FF' });

      // Adding a hyperlink to the shape.
      //   slide.addShape({ type: PPTX.ShapeTypes.UP_ARROW, x: 500, y: 140, cx: 100, cy: 50, color: '0000FF'});
    });
  });

  await pptx.save(`./shapes-test.pptx`);
  console.log("ober", inputimagename);
  process = spawn("python", ["./addBorder.py", `${finalshape.length}`, inputimagename]);
  // console.log(a)
  process.stdout.on("data", async data => {
    // char = eval(data.toString())[0];
    // x = eval(data.toString())[1];
    // y = eval(data.toString())[2];
    // await pptx.load(`./new.pptx`);

    // await pptx.compose(async pres => {
    //   await pres.addSlide(slide => {
    //     // declarative way of adding an object
    //     for (let i = 0; i < char.length; i++) {
    //       slide.addText(text => {
    //         text
    //           .value(char[i])
    //           .x(x[i])
    //           .y(y[i])
    //           .fontFace("Alien Encounters")
    //           .fontSize(16)
    //           .textColor("CC0000")
    //           .textWrap("none")
    //           .textAlign("left")
    //           .textVerticalAlign("center");
    //       });
    //     }
    //   });

    //   await pptx.save(`./new.pptx`);
    // });
  });
};

run();
