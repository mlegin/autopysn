# -*- coding: utf-8 -*-

import time
import autopy
from PIL import ImageGrab
# import pytesseract
# from PIL import Image

# image = Image.open('test1.jpg')
# code = pytesseract.image_to_string(image)
# print(code)

def where_is_the_rubbish():
    rubbish = autopy.bitmap.Bitmap.open('8.png')
    screen = autopy.bitmap.capture_screen()
    pos = screen.find_bitmap(rubbish)
    if pos:
        print ('找到了，他的位置在:%s' % str(pos))
    else:
        print ('没有找到')

def myCaputrue():
    im = ImageGrab.grab()
    im.save('path-to-save.png')
    print('已抓')

autopy.mouse.smooth_move(1000, 870)
autopy.mouse.toggle(None, True)
autopy.mouse.toggle(None, False)

# time.sleep(2)
autopy.mouse.move(700, 450)
time.sleep(3)
autopy.mouse.toggle(None, True)
autopy.mouse.toggle(None, False)

# 先把焦点定位在mumu上
time.sleep(2)
autopy.mouse.click()

myCaputrue()
# where_is_the_rubbish()

print('over')
