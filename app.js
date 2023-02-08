const {spawn} = require("child_process");
const addShape = require("./addShape");
const addText = require("./addText");

shapeslist = JSON.parse(process.argv[2]);
inputimagename = process.argv[3];

addShape.addShape(shapeslist);
shapecount=addShape.shapeCount()

process = spawn("python", ["./addBorder.py", `${shapecount}`, inputimagename]);

process = spawn("python", ["./extractText.py", inputimagename]);

process.stdout.on("data", async data => {
  textData = eval(data.toString());
  addText.addText(textData);
});

