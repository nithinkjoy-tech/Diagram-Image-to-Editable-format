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
import math

inputimgname=input('\033[92m'+"Enter input img name without extension: (ex:image1)")
inputimgname+=".png"
outputimgname=input('\033[92m'+"Enter output img name without extension: (ex:image1)")
outputimgname+=".png"


print()
eraseText.eraseText(inputimgname, outputimgname)
spinner = Halo(text='Extracting shapes from image...', spinner='dots')
spinner.start()

shapelist=extractShape.extractShape(outputimgname)
print()
spinner.stop()

spinner = Halo(text='Drawing shape and adding text to a ppt file...', spinner='dots')
spinner.start()
print()
subprocess.run(["node", "./app.js", shapelist,inputimgname])
spinner.stop()
print('\033[92m'+"Successfully completed")
print()
subprocess.run(["node", "./openppt.js"])