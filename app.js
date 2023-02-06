const PPTX = require("nodejs-pptx");
let pptx = new PPTX.Composer();
const {spawn} = require("child_process");
const { execFile } = require('child_process');

shapeslist = JSON.parse(process.argv[2]);
inputimagename = process.argv[3];
// console.log(inputimagename);
finalshape = [];


for (shape of shapeslist) {
  cx = shape[3];
  cy = shape[4];
  // console.log(cx, cy);

  if (cx > 15 && cy > 15) {
    finalshape.push(shape);
  }
}

const run = async () => {
  await pptx.compose(async pres => {
    await pres.addSlide(slide => {
      finalshape.forEach((_, i) => {
        // console.log(_);
        shapename = "PPTX.ShapeTypes." + _[0];
        slide.addShape(shape => {
          shape.type(eval(shapename)).x(_[1]).y(_[2]).cx(_[3]).cy(_[4]).color("ffffff");
        });
      });
    });
  });

  await pptx.save(`./shapes-test.pptx`);
  // console.log("ober", inputimagename);
  // console.log("ober2", finalshape.length);
  process = spawn("python", ["./addBorder.py", `${finalshape.length}`, inputimagename]);
  // console.log(a)
  process.stdout.on("data", async data => {
    // console.log("final data:",eval(data.toString()));
    textData = eval(data.toString());
    // console.log(textData);
    // textData.map(data=>{
    // await pres.getSlide("slide1").addImage(image => {
    //   image.file(`./images/pizza.jpg`).x(500).y(100).cx(166).cy(100);
    // });
    // })
    // char = eval(data.toString())[0];
    // x = eval(data.toString())[1];
    // y = eval(data.toString())[2];
    await pptx.load(`./shapes-test.pptx`);
    await pptx.compose(async pres => {
      for (let i = 0; i < textData.length; i++) {
        await pres.getSlide("slide1").addText(text => {
          text
            .value(textData[i][0])
            .x(textData[i][1])
            .y(textData[i][2])
            .fontFace("Alien Encounters")
            .fontSize(20)
            .textColor("000000")
            .textWrap("none")
            .textAlign("left")
            .textVerticalAlign("center");
        });
      }
    });

    await pptx.save(`./shapes-test.pptx`);
  });
};

run();
