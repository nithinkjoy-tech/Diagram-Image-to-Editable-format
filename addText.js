const PPTX = require("nodejs-pptx");
let pptx = new PPTX.Composer();

char = process.argv[2];
x = process.argv[3];
y = process.argv[4];
// console.log(char, x, y);

async function addText() {
  await pptx.load(`./new.pptx`);

  await pres.addSlide(slide => {
    // declarative way of adding an object
    for (let i = 0; i < char.length; i++) {
      slide.addText(text => {
        text
          .value(char[i])
          .x(x[i])
          .y(y[i])
          .fontFace("Alien Encounters")
          .fontSize(12)
          .textColor("CC0000")
          .textWrap("none")
          .textAlign("left")
          .textVerticalAlign("center");
      });
    }
  });

  await pptx.save(`./hello-world.pptx`);
  
}

addText();
