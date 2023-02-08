
def inputImage():
    location="./images/"
    imgname=input('\033[92m'+"Enter input img name without extension: (ex:image1)")
    imgnamewext=imgname+".png"
    inputimgname=location+imgnamewext
    
    imgnamewext=imgname+"out"+".png"
    outputimgname=location+imgnamewext
    return inputimgname,outputimgname