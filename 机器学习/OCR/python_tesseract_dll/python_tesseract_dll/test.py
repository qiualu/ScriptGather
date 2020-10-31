import os ,sys

TESSDATA_PREFIX = os.getenv('tessdata', None)


if sys.platform[:3] == "win":
    libnames = [
        # Jflesch> Don't they have the equivalent of LD_LIBRARY_PATH on
        # Windows ?
        "../vs2010/DLL_Release/libtesseract304.dll",
        "libtesseract304.dll", #libtesseract302.dll
    ]
else:
    libnames = [
        "libtesseract.so.3",
    ]

tessdir = os.getenv('tessdata', None)
print("tessdir -> ",tessdir)
if tessdir is None  :
    tessdir = os.path.split(os.path.realpath(__file__))[0]
    print("tessdir22 -> ", tessdir)
    os.environ['tessdata'] = tessdir
if tessdir not in os.environ['PATH']:
    os.environ['PATH']= tessdir+';' +os.environ['PATH']
    #sys.path.append(tessdir)

# print("1  ",os.environ['PATH'])
# print("2  ",os.environ['tessdata'])
# print("3  ",TESSDATA_PREFIX)
# print("4  ",libnames)
# print("5  ",tessdir)
# print("6  ",libnames)
# print("7  ",libnames)

from pyocr import libtesseract
from pyocr.builders import TextBuilder
from PIL import Image

# filename ='test.png'

filename ='img/screen16.png'


img = Image.open(filename)
#不设置成单行模式,没有输出
bu = TextBuilder(tesseract_layout=7)
#lang为语言,默认使用eng
print(libtesseract.image_to_string(img,lang='eng',builder=bu))












