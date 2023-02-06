console.log(__dirname)


let str = "This \is\ a\ string with\ a backslash:.";
let newStr = str.replace(/\\/g, "\\\\");
console.log(newStr);

const { execFile } = require('child_process');

const filePath = 'C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\POWERPNT.EXE';
dirname=__dirname.replace(/\\/g, "\\\\");
const fileToOpen = `${dirname}\\new.pptx`;

execFile(filePath, [fileToOpen], (error, stdout, stderr) => {
  if (error) {
    console.error(`execFile error: ${error}`);
    return;
  }
});
