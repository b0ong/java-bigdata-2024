# file: p52_screenCap.py
# desc: pyautogui로 화면 캡쳐하기
''' 
> pip3 install pillow
'''
import pyautogui as auto

startX, startY = 0, 1919
startX, startY = 0, 1079

auto.screenshot('./day08/screen.png', region=(startX, startY, endX-startX,endY-startY))