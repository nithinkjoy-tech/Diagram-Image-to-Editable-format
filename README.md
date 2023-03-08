
# Diagram Image to Editable format

This project is an Intelligent Image formated Diagram to Editable Output Conversion System. The system is designed to take an input diagram image and output an editable powerpoint file with the same diagram.

## Demo

Example 1



Example 2




## Screenshots
Before


After


Before


After


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