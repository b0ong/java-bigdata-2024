# file: p50_mouseAuto.py
# desc: PyAygoGui로 마우스 조작
'''
    파이썬 모듈 설치시 터미널보다 Vscode내 터미널에서 설치를 추천
    PyAutoGui 모듈설치
    > pip3 install PyAutoGui
'''
 
import pyautogui as auto

print(auto.size()) # 현재 모니터 해상도 정보 Size(width=1920, height=1080)
print(auto.position()) # 현재 마우스의 위치

# pyautogui 마우스 설정 창
# pilow 모듈이 같이 설치되어야 색상 표시가능
auto.mouseInfo()

## 마우스 이동 (절대좌표)
auto.moveTo(100,51) # (0, 0) 이후 이동이 안됨
auto.moveTo(678,51, duration=1.0) # x축 500, y축 500으로 1.0초 동안 이동

## 마우스 이동 (상대좌표)
# auto.move(505,505, duration=0.5) # 현재위치에서 x축 500, y축 500으로 1.5초 동안 이동

## 마우스 클릭
auto.leftClick()