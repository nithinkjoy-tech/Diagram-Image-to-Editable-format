from halo import Halo
import keras_ocr
import numpy as np
import cv2
import math

def eraseText(inputimgname,outputimgname):
    def midpoint(x1, y1, x2, y2):
        x_mid = int((x1 + x2)/2)
        y_mid = int((y1 + y2)/2)
        return (x_mid, y_mid)
    spinner = Halo(text='Loading Text extracting packages...', spinner='dots')
    spinner.start()
    pipeline = keras_ocr.pipeline.Pipeline()
    spinner.stop()

    def inpaint_text(img_path, pipeline):
        # read image
        spinner = Halo(text='Extracting text from image...', spinner='dots')
        spinner.start()
        img = keras_ocr.tools.read(img_path)
        # generate (word, box) tuples 
        
        prediction_groups = pipeline.recognize([img])
        print()
        spinner.stop()
        spinner = Halo(text='Extracting shapes from image...', spinner='dots')
        spinner.start()
        print()
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
        spinner.stop()
        return(img)

    pipeline = keras_ocr.pipeline.Pipeline()

    img_text_removed = inpaint_text(inputimgname, pipeline)

    cv2.imwrite(outputimgname, cv2.cvtColor(img_text_removed, cv2.COLOR_BGR2RGB))
