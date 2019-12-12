# -*- coding: utf-8 -*-
import time
import autopy
from PIL import ImageGrab
import win32api, win32gui, win32con
import win32gui, win32con, win32com.client
from time import sleep
import aircv as ac
import datetime
from PIL import Image
import cv2
import numpy as np
import pyautogui
import pyperclip
from pandas import DataFrame
import pandas as pd

def getCount():
    im = Image.open("screen.png")
    pix = im.load()
    r1, g, b = pix[300, 700]
    r2, g, b = pix[385, 700]
    r3, g, b = pix[455, 700]
    r4, g, b = pix[535, 700]
    r5, g, b = pix[615, 700]
    source =[r1, r2, r3, r4, r5]
    return len([i for i in source if i > 60])

def judgeColor(x, y, r, g, b, screen = 'screen.png'):
    im = Image.open(screen)
    pix = im.load()
    r1, g1, b1 = pix[x, y]
    if r1 == r and g1 == g and b1 == b:
        return True
    else:
        return False

lastClick = 'default'
# 宝藏
BZ = False

# 起始， 终止 下面，用于黄星
pickArr = [
    [263, 527, 500, 937],
    [554, 568, 782, 972],
    [852, 548, 1066, 937],
    [1141, 572, 1335, 978],
    [1425, 543, 1628, 942],
]

# 起始终止，上面，用于计算定身
pickArr2 =[
    [486, 171, 559, 217],
    [665, 173, 737, 216],
    [877, 82, 942, 134],
    [1110, 174, 1178, 217],
    [1289, 172, 1353, 218],
]

def calcStar(coordinate, pix):
    area = 0
    for i in range(coordinate[0], coordinate[2]):
        for j in range(coordinate[1], coordinate[3]):
            if pix[i, j] == 255:
                area += 1
    return area

def qq_message_chuang(x, y, strs):
    sleep(2)
    fullScreen()
    sleep(1)
    time_str = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    mouse_click(x, y)
    # mouse_click(515, 1057)
    # mouse_click(859, 1060)
    sleep(4)
    pyperclip.copy(strs + '： ' + time_str)  # 先复制
    pyautogui.hotkey('ctrl', 'v')  # 再粘贴
    sleep(3)
    mouse_click(1045, 742)  # 发送消息
    sleep(2)
    mouse_click(1267, 290)  # 关闭qq窗口
    sleep(4)
    fullScreen()
    sleep(2)

def myCaputrue(screen = 'screen.png'):
    im = ImageGrab.grab()
    im.save(screen)

def mouse_drop(startX, startY, endX, endY):
    autopy.mouse.move(startX, startY)
    sleep(1)
    autopy.mouse.toggle(None, True)
    autopy.mouse.smooth_move(endX, endY)
    autopy.mouse.toggle(None, False)

def matchImg(imgsrc, imgobj, confidence=0.5, mark='default'):  # imgsrc=原始图像，imgobj=待查找的图片
    imsrc = ac.imread(imgsrc)
    imobj = ac.imread(imgobj)

    match_result = ac.find_template(imsrc, imobj, confidence)
    # {'confidence': 0.5435812473297119, 'rectangle': ((394, 384), (394, 416), (450, 384), (450, 416)), 'result': (422.0, 400.0)}
    if match_result is not None:
        match_result['shape'] = (imsrc.shape[1], imsrc.shape[0])  # 0为高，1为宽
        match_result['mark'] = mark
    print('ceshi' + str(match_result))
    return match_result


win32api.ShellExecute(0, 'open', r'D:\Program Files\Nox\bin\Nox.exe', '', '', 1)
time.sleep(2)
hwnd_title = {}

def where_is_the_rubbish():
    rubbish = autopy.bitmap.Bitmap.open('auto.png')
    screen = autopy.bitmap.capture_screen()
    pos = screen.find_bitmap(rubbish)
    if pos:
        print ('找到了，他的位置在:%s' % str(pos))
    else:
        print ('没有找到')

clickD = {
    'shangji': {'click': (1517, 980)},  # 只有这个识别
    'chuji': {'click': (1200, 673)},
}

slowClick = {
    'tianshi': {'click': (1160, 800), 'click2': (1538, 925)},
    'baoxiang': {'click': (1160, 800), 'click2': (1538, 925)},
    'kulou': {'click': (1160, 800), 'click2': (1538, 925)},
    'monv': {'click': (1160, 800), 'click2': (1538, 925)},
    'boss': {'click': (1160, 800), 'click2': (1538, 925)}
}
#['tianshi', 'baoxiang', 'kulou', 'monv', 'boss'

def mouse_click(x, y,flag= False, j = 0, describe = 'default', mark= 'default'):
    print('kaishi '+ str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S %f')))
    global lastClick
    global clickD
    x = int(x)
    y = int(y)
    ff = True
    if lastClick in clickD and 'nextButton' in clickD[lastClick]:
        ff = True if mark == clickD[lastClick]['nextButton'] else False
        print('进入mouse_click中绑定字典 ' + ' ff:' + str(ff) + ' lastClick:' + str(lastClick) + ' mark: ' + str(mark) + ' 说明-' + describe)
    if ff:
        win32api.SetCursorPos([x, y])
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
        time1 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S %f')
        print('click ' + str(x) + ' ' + str(y) + ' 循环量-' +
              str(j) + ' 说明-' + describe + ' pMark-' + mark + ' 点击时间-' + time1)
        if mark in clickD and 'click' in clickD[mark]:
            sleep(0.8)
            print('click生效')
            mouse_click(int(clickD[mark]['click'][0]), int(clickD[mark]['click'][1]))
            if 'click3' in clickD[mark]:
                sleep(2)
                mouse_click(int(clickD[mark]['click2'][0]), int(clickD[mark]['click2'][1]))
                sleep(0.6)
        if lastClick in slowClick:
            sleep(2)
        lastClick = mark
    else:
        print('跳过点击')
    print('jieshu '+ str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S %f')))

def huangxing():
    position_temp = matchImg('./screen.png', './huangxing.png', 0.7, 'huangxing')
    if position_temp and 254 < position_temp['result'][0] < 1638 and 554 < position_temp['result'][1] < 850:
        return position_temp
    else:
        return None

def get_all_hwnd(hwnd, mouse):
    if (win32gui.IsWindow(hwnd)
            and win32gui.IsWindowEnabled(hwnd)
            and win32gui.IsWindowVisible(hwnd)):
        hwnd_title.update({hwnd: win32gui.GetWindowText(hwnd)})

def fullScreen():
    win32api.keybd_event(17, 0, 0, 0)  # 按下enter，第一个元素13为enter的键位码
    win32api.keybd_event(100, 0, 0, 0)  # 按下enter，第一个元素13为enter的键位码
    time.sleep(1)
    win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)  # 松开enter
    win32api.keybd_event(100, 0, win32con.KEYEVENTF_KEYUP, 0)  # 松开enter

def findhwnd():
    win32gui.EnumWindows(get_all_hwnd, 0)
    for h, t in hwnd_title.items():
        if t:
            print(h, t)
            if t == "夜神模拟器":
                # win32api.keybd_event(13, 0, 0, 0)
                win32gui.SetForegroundWindow(h)
                sleep(1)
                fullScreen()

# win32api.SetCursorPos([599, 599])    #鼠标移动到
# win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)    #左键按下
# time.sleep(1)
# mw = int(300)
# mh = int(300)
# win32api.mouse_event(win32con.MOUSEEVENTF_ABSOLUTE + win32con.MOUSEEVENTF_MOVE, 0, mh, 0, 0)
# time.sleep(1)
# win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

# # 打开游戏
# mouse_click(954, 530)
# sleep(15)  # 进主界面点开始
# mouse_click(690, 848)
# sleep(25)  # 进主城界面，耗时长
# mouse_click(1836, 1000)  # 打开右下角
# sleep(1)
# mouse_click(1200, 945)  # 点击战斗
# sleep(3)
# mouse_click(1400, 700)  # 进入魔女界面
# 【函数】
def zhandou(position, j):
    if matchImg('./screen.png', './sfiona.png', 0.9, 'sfiona') is not None:
        position = zhandouPick()
        posFadong = matchImg('./screen.png', './fadong.png', 0.7, 'fadong')
        posFadongJiNeng = matchImg('./screen.png', './fadongjineng.png', 0.7, 'fadongjineng')
        posQueRen = matchImg('./screen.png', './queren.png', 0.7, 'queren')
        if posQueRen:
            mouse_click(posQueRen['result'][0], posQueRen['result'][1], False, j, '点击确认【zhandou】', posQueRen['mark'])
        if position is None and posFadong is None:  # 没亮星
            mouse_click(1830, 933, False, j, '没亮星，点自动【zhandou】', 'wu')
        elif posFadong is not None:
            mouse_click(posFadong['result'][0], posFadong['result'][1], False, j, '点击发动【zhandou】', posFadong['mark'])
        elif posFadongJiNeng is not None:
            mouse_click(posFadongJiNeng['result'][0], posFadongJiNeng['result'][1], False, j, '点击发动【zhandou】', posFadongJiNeng['mark'])
        else: # 亮星了
            mouse_click(position['result'][0], position['result'][1], False, j, '亮星了【zhandou】', position['mark'])
            sleep(0.3)
            # myCaputrue()
            # position = matchImg('./screen.png', './fadong.png', 0.7, 'fadong')
            mouse_click(1150, 677)
            sleep(0.3)
            mouse_click(1400, 555)
            sleep(0.3)
        return
            # if position is not None:
            #     mouse_click(position['result'][0], position['result'][1], False, j, '亮星点击发动【zhandou】', position['mark'])
    if position is not None and float(position['confidence']) > 0.932:
        mouse_click(position['result'][0], position['result'][1], False, j, '不在战斗中【zhandou】', position['mark'])
    else:
        mouse_click(300, 180, True, j, '点击300【zhandou】', 'default') # 不延迟

def xiulianchangDrop():
    mouse_drop(599, 599, 1499, 599)
    sleep(2)
    mouse_click(416, 774)
    sleep(1)
    mouse_click(915, 760)
    sleep(3)

# 刷魔女
def shuaMoNv():
    print('进入刷魔女')
    sleep(2)
    mouse_click(1818, 990)
    sleep(2)
    mouse_click(1200, 950)
    sleep(4)
    # mouse_click(1400, 865)
    mouse_click(1400, 660)
    sleep(4)
    flag = True
    monv_zero = False
    j = 0
    k = 0
    while (flag):
        j += 1
        sleep(0.2)
        myCaputrue()
        position = matchImg('./screen.png', './tiaozhan0.png', 0.99, 'tiaozhan0')
        if position is not None:
            if k > -1:
                flag = False
                mouse_click(1585, 129)
                monv_zero = True
                print('monvOver')
                break
            # mouse_click(1300, 450)
            # sleep(0.6)
            # mouse_click(1200, 628)
            k += 1
        if matchImg('./screen.png', './xiulianchang.png') is not None and matchImg('./screen.png', './tips.png', 0.7) is not None:
            mouse_click(129, 436)  # 先点一下出现中
            sleep(1)
            xiulianchangDrop()
            mouse_click(1505, 524)  # 出现中的保险
            continue
        position = matchImg('./screen.png', './auto.png')
        if position is not None:
            mouse_click(position['result'][0], position['result'][1])
            continue

        posNameListnv = ['zhandou', 'zhandoukaishi', 'ok', 'x', 'zidong', 'chuang', 'fanhui']
        resultPos = {'confidence': 0}
        for item in posNameListnv:
            pos = matchImg('./screen.png', './' + item +'.png', 0.7, item)
            if pos and float(pos['confidence']) > 0.97:
                if item == 'chuang':
                    resultPos = pos
                    break
                resultPos = pos if float(pos['confidence'] > float(resultPos['confidence'])) else resultPos
            elif pos and float(pos['confidence']) > float(resultPos['confidence']):
                resultPos = pos
        print('resultPos:' + str(resultPos))
        if resultPos and 'mark' in resultPos and resultPos['mark'] == 'chuang':
            qq_message_chuang(515, 1057, '来创了老铁，时间')
            print('chuanglaile')
        zhandou(resultPos, j)
    shuaMoJie(monv_zero)

# mojiebaji = True
mojiebaji = False
# 魔界
def shuaMoJie(monv_zero = False):
    global mojiebaji
    global BZ
    if '18:22:15.1' > str(datetime.datetime.now().time()) > '18:16:15.1':
        BZ = False
    print('进入刷魔界')
    sleep(2)
    mouse_click(1818, 990)
    sleep(0.3)
    mouse_click(1200, 950)
    sleep(3)
    mouse_click(1400, 170)
    sleep(4)
    flag = True
    j = 0
    while (flag):
        if mojiebaji:
            break
        j += 1
        sleep(0.6)
        myCaputrue()
        posNameList = ['tianshi', 'baoxiang', 'kulou', 'monv', 'boss', 'shangji', 'lvse', 'okkkk', 'okmn', 'chuji', 'zhandoukaishi_mojie', 'bx']
        resultPos = {'confidence': 0}
        for item in posNameList:
            pos = matchImg('./screen.png', './' + item +'.png', 0.7, item)
            if pos and float(pos['confidence']) > 0.97:
                resultPos = pos if float(pos['confidence'] > float(resultPos['confidence'])) else resultPos
                if posNameList.index(item) > 4:
                    break
                else: # <4
                    resultPos = pos if int(pos['result'][0]) > int(resultPos['result'][0]) else resultPos
            elif pos and float(pos['confidence']) > float(resultPos['confidence']):
                if posNameList.index(item) < 4 and 'result' in resultPos:
                    resultPos = pos if int(pos['result'][0]) > int(resultPos['result'][0]) else resultPos
                else:
                    resultPos = pos
        print('resultPos:' + str(resultPos))
        if resultPos and 'mark' in resultPos and resultPos['mark'] == 'shangji':
            for l in range(4):
                mouse_click(300, 180)
                print('过场动画')
                sleep(3)
            myCaputrue('screen_mojie.png')
            if not judgeColor(1700, 400, 41, 28, 32, 'screen_mojie.png') and judgeColor(600, 318, 131, 108, 142, 'screen_mojie.png'):
                # 进入秘境了
                print('进入秘境')
                sleep(4)
                qq_message_chuang(569, 1057, '魔界秘境！@mlegin')
                sleep(4)
                mouse_click(323, 574)
                sleep(5)
                mouse_click(1508, 985)
                mouse_drop(995, 650, 995, 492)
                sleep(1)
                mouse_click(1200, 900)  # 五次霸级
                sleep(1)
                mouse_click(1300, 450)
                sleep(0.6)
                mouse_click(1200, 628)
                mojiebaji = True  # 从while跳出，进入魔女，并且一直不进魔界了
                print('jieshu')
                sleep(10)
                continue
            if '11:15:15.1' > str(datetime.datetime.now().time()) > '10:05:15.1' and not BZ:
                flag = False
                BZ = True
                shuaBaoZang()
                break
            if '19:30:15.1' > str(datetime.datetime.now().time()) > '18:23:15.1' and not BZ:
                flag = False
                BZ = True
                shuaBaoZang()
                break
            if getCount() < 1:  # 只打5个魔界
                flag = False
                break
        zhandou(resultPos, j)
    if monv_zero:
        # print('休息一个半小时') #不休息了，让他扫描创去
        # sleep(5400)
        shuaMoNv()
    else:
        shuaMoNv()

def kaiBaoZang():
    mouse_click(1217, 935)
    sleep(6)
    mouse_click(955, 669)
    sleep(6)
    mouse_click(1443, 927)
    sleep(6)
    mouse_click(1219, 906)
    sleep(6)
    mouse_click(955, 669)
    sleep(3)
    # myCaputrue()
    # position = matchImg('./screen.png', './tanhao.png', 0.7, 'tanhao')
    # if position is not None:
    #     mouse_click(position['result'][0], position['result'][1])

# 进主城刷宝藏
def shuaBaoZang():
    global BZ
    BZ = True
    sleep(2)
    mouse_click(1818, 990)
    sleep(1)
    mouse_click(1500, 990)
    sleep(4)
    mouse_click(1215, 697)  # 点击叹号
    sleep(2)
    mouse_click(1385, 980)
    sleep(12)
    for i in range(5):
        kaiBaoZang()
        sleep(4)
        mouse_click(1544, 77)
        sleep(4)
    sleep(5)
    #  选宝藏
    for i in range(4):
        mouse_click(462, 205)
        sleep(0.3)
        mouse_drop(996, 965, 996, 340)
        sleep(0.2)
        mouse_drop(996, 965, 996, 340)
        sleep(1)
        mouse_click(1540, 540)
        sleep(1)
        mouse_click(1167, 672)  # 点击是
        sleep(3)
        mouse_click(1544, 77)
        sleep(4)
    shuaMoNv()

# 颜色识别出数组opencv
def screenToArr(low, high, targetPng, cPixCount, pickAr):
    countStar = [0, 0, 0, 0, 0]
    img_original = cv2.imread('screen.png')
    # 转变为HSV颜色空间
    img_hsv = cv2.cvtColor(img_original, cv2.COLOR_BGR2HSV)
    # 返回黄色区域的二值图像
    img_yellow = cv2.inRange(img_original, low, high)
    cv2.imwrite(targetPng, img_yellow)
    cv2.waitKey()
    cv2.destroyAllWindows()
    im = Image.open(targetPng)
    pix = im.load()
    position_temp = None
    # 循环查找星星
    for i in range(5):
        cPix = calcStar(pickAr[i], pix)
        if cPix > cPixCount:
            position_temp = {
                'confidence': 0.999,
                'result': (pickAr[i][0] + 100, pickAr[i][1] + 150),
                'mark': 'huangxing'
            } #budui
        countStar[i] += cPix
    result = {'countStar': countStar, 'position_temp': position_temp}
    return result

def zhandouPick():
    print('111 '+ str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S %f')))
    acc = 1
    for k in range(2): # 控制精度
        print('333 ' + str(k) + str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S %f')))
        if k == 0:
            myCaputrue('screen.png')
        # 黄色星星
        result = screenToArr((60, 200, 215), (140, 255, 255), 'whitePix.png', 2000, pickArr)
        count_star = result['countStar']
        position_temp = result['position_temp']
        print('ww' + str(count_star))
        print(np.array(count_star)/acc)

        # result = screenToArr((151, 240, 110), (159, 248, 118), 'greenPix.png', 15, pickArr)
        # count_star = result['countStar']
        # position_temp = result['position_temp']
        # print('gg' + str(count_star))
        # print(np.array(count_star) / acc)
        # #
        # result = screenToArr((176, 36, 152), (185, 44, 160), 'purplePix.png', 15, pickArr)
        # count_star = result['countStar']
        # position_temp = result['position_temp']
        # print('ss' + str(count_star))
        # print(np.array(count_star) / acc)
        #
        # result = screenToArr((155, 102, 29), (164, 110, 37), 'blue.png', 15, pickArr)
        # count_star = result['countStar']
        # position_temp = result['position_temp']
        # print('bb' + str(count_star))
        # print(np.array(count_star) / acc)
        #
        # result = screenToArr((45, 1, 240), (190, 100, 255), 'dingshen.png', 15, pickArr2)
        # count_star = result['countStar']
        # position_temp = result['position_temp']
        # print('dd' + str(count_star))
        # print(np.array(count_star) / acc)
        #
        # result = screenToArr((0, 0, 170), (5, 5, 200), 'kejuebao.png', 15, pickArr)
        # count_star = result['countStar']
        # position_temp = result['position_temp']
        # print('kk' + str(count_star))
        # print(np.array(count_star) / acc)
    print('222 ' + str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S %f')))
    return position_temp

def zhandou_baji():
    print(1)

findhwnd()
# sleep(5)
# zhandouPick()
# shuaBaoZang()
shuaMoNv()
# shuaMoJie()

# now = datetime.datetime.now()
# tt = now + datetime.timedelta(hours= 2, minutes= 30)
# print(tt.strftime('%Y-%m-%d %H:%M:%S %f'))
#
#
# def csv_deal(name = 'caibao'):
#     data = {"name": ['caibao', 'ziyuan'], "time": [datetime.datetime.now(), datetime.datetime.now()], "jiange": [9, 3]}
#     f1 = DataFrame(data, columns=['name', 'time', 'jiange'])
#     print(f1)
#     df = pd.DataFrame(data)
#     df.to_csv('pandas.csv', header=False, index=False)
#
# csv_deal()