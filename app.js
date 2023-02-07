const {spawn} = require("child_process");
const addShape = require("./addShape");
const addText = require("./addText");

shapeslist = JSON.parse(process.argv[2]);
inputimagename = process.argv[3];
finalshape = [];

for (shape of shapeslist) {
  cx = shape[3];
  cy = shape[4];

  if (cx > 15 && cy > 15) {
    finalshape.push(shape);
  }
}

addShape.addShape(finalshape);

process = spawn("python", ["./addBorder.py", `${finalshape.length}`, inputimagename]);

process.stdout.on("data", async data => {
  textData = eval(data.toString());
  addText.addText(textData);
});

