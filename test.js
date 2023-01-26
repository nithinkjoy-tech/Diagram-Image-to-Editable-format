const pptxgen =require("pptxgenjs")

// Presentation 1:
let pptx = new pptxgen();

shapeslist=JSON.parse(process.argv[2])
finalshape=[]

for (shape of shapeslist){
    cx = shape[3]
    cy = shape[4]
    console.log(cx,cy)

    if(cx>7 && cy>7){
        finalshape.push(shape)
    }
}

pptx.setLayout('LAYOUT_WIDE');
 
var slide = pptx.addNewSlide();
//  slide.addText('TEXT', {OPTIONS});
// Misc Shapes
// finalshape.forEach((_,i) =>{
//     console.log(_)
//     shapename="pptx.shapes."+_[0]
//     slide.addShape(eval(shapename),{ x:_[1], y:_[2], w:_[3], h:_[4], line:'000000', line_size:1,fill:'ffffff' });
//   })
slide.addShape(pptx.shapes.LINE,      { x:4.15, y:4.40, w:5, h:0, line:'FF0000', line_size:1 });
// slide.addShape(pptx.shapes.LINE,      { x:4.15, y:4.80, w:5, h:0, line:'FF0000', line_size:2, line_head:'triangle' });
// slide.addShape(pptx.shapes.LINE,      { x:4.15, y:5.20, w:5, h:0, line:'FF0000', line_size:3, line_tail:'triangle' });
// slide.addShape(pptx.shapes.LINE,      { x:4.15, y:5.60, w:5, h:0, line:'FF0000', line_size:4, line_head:'triangle', line_tail:'triangle' });
// slide.addShape(pptx.shapes.RECTANGLE, { x:0.50, y:0.75, w:5, h:3, fill:'FF0000' });
// slide.addShape(pptx.shapes.OVAL,      { x:4.15, y:0.75, w:5, h:2, fill:{ type:'solid', color:'0088CC', alpha:25 } });
 
// Adding text to Shapes:
// slide.addText('RIGHT-TRIANGLE', { shape:pptx.shapes.RIGHT_TRIANGLE, align:'c', x:0.40, y:4.3, w:6, h:3, fill:'0088CC', line:'000000', line_size:3 });
// slide.addText('RIGHT-TRIANGLE', { shape:pptx.shapes.RIGHT_TRIANGLE, align:'c', x:7.00, y:4.3, w:6, h:3, fill:'0088CC', line:'000000', flipH:true });
// const buff = Buffer.from(pptx, "utf-8");
// console.log(buff);
// fs.writeFileSync('fef.ppt', buff);
pptx.writeFile({ fileName: "PptxGenJS-NodePres-1" });
