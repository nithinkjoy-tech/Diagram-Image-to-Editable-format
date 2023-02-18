const PPTX = require("nodejs-pptx");
let pptx = new PPTX.Composer();

exports.addText = async (textData) => {
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
};
