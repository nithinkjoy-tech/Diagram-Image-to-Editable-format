
# Diagram Image to Editable format

This project is an Intelligent Image formated Diagram to Editable Output Conversion System. The system is designed to take an input diagram image and output an editable powerpoint file with the same diagram.

## Demo

Example 1


https://user-images.githubusercontent.com/62066971/223629911-16bfea84-cb38-45bf-bf26-19bbd3562561.mp4




Example 2


https://user-images.githubusercontent.com/62066971/223629951-ff5c6fea-3a9e-4b29-b30b-ef0d70971b53.mp4





## Screenshots
Before
![input1](https://user-images.githubusercontent.com/62066971/223630139-c891e6a8-3695-480f-a9bb-416802b6e560.png)


After
![WhatsApp Image 2023-03-08 at 10 08 33 AM](https://user-images.githubusercontent.com/62066971/223630193-d8748292-1009-4c36-8ec3-1544030ca07f.jpeg)


Before
![input2](https://user-images.githubusercontent.com/62066971/223630212-c6806ff4-b141-4da5-a49c-0c760be77ac2.png)


After
![WhatsApp Image 2023-03-08 at 10 00 28 AM](https://user-images.githubusercontent.com/62066971/223630268-ed76c3dc-2b3c-4f68-8490-778c53b26bc9.jpeg)


## Installation and Usage
Download the repository.

Make sure you have Node.js, Python and powerpoint installed in your system

Set up and activate your virtual environment. On windows, for example, type into your console:
```
python -m venv venv
.\venv\Scripts.activate.bat
```

Install the packages from the `requirements.txt` file:
```
pip install -r requirements.txt
```

Install npm packages from the `package.json` file:
```
npm install
```

Run
```
python app.py
```
## Working
This project takes input as an image and first it will erase all the text written on it using keras package. If we still keep text our model will identify it as some other random shapes that would give wrong output. Then we identiy each shapes using open-cv api and find x axis, y axis, width, height (x,y,w,h) of each shapes. using npm package (nodejs-pptx) we will draw each shapes into a ppt file. Later we use python package (python-pptx) to put borders. In the next step using easyocr package we extract text with x axis and y axis, we pass it to another node.js function and put it into the same ppt file using the generated x and y axis.
