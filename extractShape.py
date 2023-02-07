import cv2
import json

def extractShape(outputimgname):
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
            # print(approx,"triangle")
        elif len(approx) == 4 :
            # print(approx,"4 side")
            x, y , w, h = cv2.boundingRect(approx)
            shapeaxis=["RECTANGLE",x,y,w,h]
            shapelist.append(shapeaxis)
            aspectRatio = float(w)/h
            # print(aspectRatio)
            if aspectRatio >= 0.95 and aspectRatio < 1.05:
                cv2.putText(img, "square", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
            else:
                cv2.putText(img, "rectangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
        elif len(approx) == 5 :
            # print(approx,"5 side")
            x, y , w, h = cv2.boundingRect(approx)
            shapeaxis=["PENTAGON",x,y,w,h]
            shapelist.append(shapeaxis)
            cv2.putText(img, "pentagon", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
        elif len(approx) == 6 :
            # print(approx,"hexagon")
            x, y , w, h = cv2.boundingRect(approx)
            shapeaxis=["HEXAGON",x,y,w,h]
            shapelist.append(shapeaxis)
            cv2.putText(img, "hexagon", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
        elif len(approx) == 7 :
            # print(approx,"heptagon")
            x, y , w, h = cv2.boundingRect(approx)
            shapeaxis=["HEPTAGON",x,y,w,h]
            shapelist.append(shapeaxis)
            cv2.putText(img, "heptagon", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
        elif len(approx) == 8 :
            # print(approx,"octagon")
            x, y , w, h = cv2.boundingRect(approx)
            shapeaxis=["OCTAGON",x,y,w,h]
            shapelist.append(shapeaxis)
            cv2.putText(img, "octagon", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
        elif len(approx) == 10 :
            # print(approx,"10 side")
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
    return shapelist