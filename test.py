# -*- coding: utf-8 -*-

import time
import autopy
import pytesseract
from PIL import Image

image = Image.open('test1.jpg')
code = pytesseract.image_to_string(image)
print(code)

autopy.mouse.smooth_move(1000,870)
autopy.mouse.toggle(None,True)
autopy.mouse.toggle(None,False)

#time.sleep(2)
autopy.mouse.move(700,450)
time.sleep(3)
autopy.mouse.toggle(None,True)
autopy.mouse.toggle(None,False)

# 先把焦点定位在mumu上
time.sleep(2)
autopy.mouse.click()

print('over')