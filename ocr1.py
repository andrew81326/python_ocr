import cv2
import pytesseract
import numpy as np
import  matplotlib.pyplot as plt
import sys

import pyocr
import pyocr.builders

#loading image
img= cv2.imread('camera_ocr.jpg',0)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
img = cv2.resize(img, (428, 270), interpolation=cv2.INTER_CUBIC)
img1 = cv2.imread('English.jpg',0)
img = cv2.resize(img1, (428, 270), interpolation=cv2.INTER_CUBIC)
code = pytesseract.image_to_string(img1,lang='eng')
#print("檢驗過程 :" + code)
#gray image
#cv2.imshow('image',img1)
k= cv2.waitKey(0)
if k== 27:
    cv2.destroyAllWindows()
elif k== ord ('s'):
    cv2.imwrite('image_ocr.png',img)
    cv2.destroyAllWindows()

tools = pyocr.get_available_tools()
# The tools are returned in the recommended order of usage
tool = tools[0]

langs = tool.get_available_languages()
lang = langs[0]

txt = tool.image_to_string(
    img.open('camera_ocr.jpg'),
    lang=lang,
    builder=pyocr.builders.TextBuilder()
)
# txt is a Python string

word_boxes = tool.image_to_string(
   img.open('camera_ocr.jpg'),
    lang="chi_tra",
    builder=pyocr.builders.WordBoxBuilder()
)
# list of box objects. For each box object:
#   box.content is the word in the box
#   box.position is its position on the page (in pixels)
#
# Beware that some OCR tools (Tesseract for instance)
# may return empty boxes

line_and_word_boxes = tool.image_to_string(
   img.open('camera_ocr.jpg'), lang="chi_tra",
    builder=pyocr.builders.LineBoxBuilder()
)
# list of line objects. For each line object:
#   line.word_boxes is a list of word boxes (the individual words in the line)
#   line.content is the whole text of the line
#   line.position is the position of the whole line on the page (in pixels)
#
# Beware that some OCR tools (Tesseract for instance)
# may return empty boxes

# Digits - Only Tesseract (not 'libtesseract' yet !)
digits = tool.image_to_string(
    img.open('camera_ocr.jpg'),
    lang=lang,
    builder=pyocr.tesseract.DigitBuilder()
)
# digits is a python string
