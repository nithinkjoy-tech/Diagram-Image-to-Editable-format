
def inputImage():
    inputimgname=input('\033[92m'+"Enter input img name without extension: (ex:image1)")
    inputimgname+=".png"
    outputimgname=input('\033[92m'+"Enter output img name without extension: (ex:image1)")
    outputimgname+=".png"
    return inputimgname,outputimgname