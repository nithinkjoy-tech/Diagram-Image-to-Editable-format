import os
import cv2
import math
import json
import openppt
import subprocess
import numpy as np
from halo import Halo
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 

spinner = Halo(text='Loading Image processing packages....', spinner='dots')
spinner.start()
import keras_ocr
print()
spinner.stop()

import eraseText
import extractShape
import inputImage


inputimgname,outputimgname =inputImage.inputImage()
eraseText.eraseText(inputimgname, outputimgname)
shapelist=extractShape.extractShape(outputimgname)

spinner = Halo(text='Drawing shape and adding text to a ppt file...', spinner='dots')
spinner.start()
print()
subprocess.run(["node", "./app.js", shapelist,inputimgname])
spinner.stop()

print('\033[92m'+"Successfully completed")

openppt.openppt()