const {spawn} = require("child_process");
const addShape = require("./addShape");
const addText = require("./addText");

shapeslist = JSON.parse(process.argv[2]);
inputimagename = process.argv[3];


addShape.addShape(shapeslist);

process = spawn("python", ["./addBorder.py", `${finalshape.length}`, inputimagename]);

process.stdout.on("data", async data => {
  textData = eval(data.toString());
  addText.addText(textData);
});

