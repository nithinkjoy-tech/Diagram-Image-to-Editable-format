import numpy as np
import cv2
import os
os.system('cls')
import subprocess
import json
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
import matplotlib.pyplot as plt
from halo import Halo
import eraseText
import extractShape

spinner = Halo(text='Loading Image processing packages....', spinner='dots')
spinner.start()
import keras_ocr
spinner.stop()
#os.system('cls')
import math

#remove text
inputimgname=input('\033[92m'+"Enter input img name without extension: (ex:image1)")
inputimgname+=".png"
# inputimgname+=".png"
# outputimgname=inputimgname
outputimgname=input('\033[92m'+"Enter output img name without extension: (ex:image1)")
outputimgname+=".png"


print()
#here
eraseText.eraseText(inputimgname, outputimgname)
#find shapes and points
spinner = Halo(text='Extracting shapes from image...', spinner='dots')
spinner.start()
#here

shapelist=extractShape.extractShape(outputimgname)
print()
spinner.stop()

spinner = Halo(text='Drawing shape and adding text to a ppt file...', spinner='dots')
spinner.start()
print()
# Run Node.js and return the exit code.
subprocess.run(["node", "./app.js", shapelist,inputimgname])
spinner.stop()
print('\033[92m'+"Successfully completed")
print()
subprocess.run(["node", "./openppt.js"])
# cv2.imshow('shapes', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()