import numpy as np
import cv2
import subprocess
import json
import matplotlib.pyplot as plt
import keras_ocr
import math

#remove text
inputimgname=input("Enter input img name without extension")
inputimgname+=".png"
# inputimgname+=".png"
# outputimgname=inputimgname
outputimgname=input("Enter output img name without extension")
outputimgname+=".png"

def midpoint(x1, y1, x2, y2):
    x_mid = int((x1 + x2)/2)
    y_mid = int((y1 + y2)/2)
    return (x_mid, y_mid)
pipeline = keras_ocr.pipeline.Pipeline()
def inpaint_text(img_path, pipeline):
    # read image
    img = keras_ocr.tools.read(img_path)
    # generate (word, box) tuples 
    prediction_groups = pipeline.recognize([img])
    mask = np.zeros(img.shape[:2], dtype="uint8")
    for box in prediction_groups[0]:
        x0, y0 = box[1][0]
        x1, y1 = box[1][1] 
        x2, y2 = box[1][2]
        x3, y3 = box[1][3] 
        
        x_mid0, y_mid0 = midpoint(x1, y1, x2, y2)
        x_mid1, y_mi1 = midpoint(x0, y0, x3, y3)
        
        thickness = int(math.sqrt( (x2 - x1)**2 + (y2 - y1)**2 ))
        
        cv2.line(mask, (x_mid0, y_mid0), (x_mid1, y_mi1), 255,    
        thickness)
        img = cv2.inpaint(img, mask, 7, cv2.INPAINT_NS)
                 
    return(img)

pipeline = keras_ocr.pipeline.Pipeline()

img_text_removed = inpaint_text(inputimgname, pipeline)

plt.imshow(img_text_removed)

cv2.imwrite(outputimgname, cv2.cvtColor(img_text_removed, cv2.COLOR_BGR2RGB))



#find shapes and points
img = cv2.imread(outputimgname)
imgGry = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret , thrash = cv2.threshold(imgGry, 240 , 255, cv2.CHAIN_APPROX_NONE)
contours , hierarchy = cv2.findContours(thrash, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

shapelist=[]
for contour in contours:
    approx = cv2.approxPolyDP(contour, 0.01* cv2.arcLength(contour, True), True)
    # print(approx,"ap")
    cv2.drawContours(img, [approx], 0, (0, 0, 0), 5)
    x = approx.ravel()[0]
    y = approx.ravel()[1] - 5
    # print("x",x)
    # print("\ny",y)
    if len(approx) == 3:
        x, y , w, h = cv2.boundingRect(approx)
        shapeaxis=["TRIANGLE",x,y,w,h]
        shapelist.append(shapeaxis)
        cv2.putText( img, "Triangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0) )
        print(approx,"triangle")
    elif len(approx) == 4 :
        print(approx,"4 side")
        x, y , w, h = cv2.boundingRect(approx)
        shapeaxis=["RECTANGLE",x,y,w,h]
        shapelist.append(shapeaxis)
        aspectRatio = float(w)/h
        print(aspectRatio)
        if aspectRatio >= 0.95 and aspectRatio < 1.05:
            cv2.putText(img, "square", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
        else:
            cv2.putText(img, "rectangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
    elif len(approx) == 5 :
        print(approx,"5 side")
        x, y , w, h = cv2.boundingRect(approx)
        shapeaxis=["PENTAGON",x,y,w,h]
        shapelist.append(shapeaxis)
        cv2.putText(img, "pentagon", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
    elif len(approx) == 6 :
        print(approx,"hexagon")
        x, y , w, h = cv2.boundingRect(approx)
        shapeaxis=["HEXAGON",x,y,w,h]
        shapelist.append(shapeaxis)
        cv2.putText(img, "hexagon", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
    elif len(approx) == 7 :
        print(approx,"heptagon")
        x, y , w, h = cv2.boundingRect(approx)
        shapeaxis=["HEPTAGON",x,y,w,h]
        shapelist.append(shapeaxis)
        cv2.putText(img, "heptagon", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
    elif len(approx) == 8 :
        print(approx,"octagon")
        x, y , w, h = cv2.boundingRect(approx)
        shapeaxis=["OCTAGON",x,y,w,h]
        shapelist.append(shapeaxis)
        cv2.putText(img, "octagon", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
    elif len(approx) == 10 :
        print(approx,"10 side")
        x, y , w, h = cv2.boundingRect(approx)
        shapeaxis=["STAR_5_POINT",x,y,w,h]
        shapelist.append(shapeaxis)
        cv2.putText(img, "star", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
    else:
        pass
        # print(approx,"circle side")
        # x, y , w, h = cv2.boundingRect(approx)
        # shapeaxis=["OVAL",x,y,w,h]
        # shapelist.append(shapeaxis)
        # cv2.putText(img, "circle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))

shapelist = json.dumps(shapelist)
# Run Node.js and return the exit code.
subprocess.run(["node", "./app.js", shapelist,inputimgname])
# cv2.imshow('shapes', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()