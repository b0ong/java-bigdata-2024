# file: p54_captWeather.py
# desc: 네이버 날씨 화면 캡쳐

import pyautogui as auto
import pyperclip as clip
import time
import mss

# auto.mouseInfo() #125, 145

auto.moveTo(80, 175, duration=0.5)
time.sleep(0.2)
auto.leftClick()

clip.copy('부산 날씨')
auto.hotkey('command', 'v') # 붙여넣기
time.sleep(0.2)

auto.press('enter') # \n 가능
time.sleep(1.0)

startX, startY = 28, 300
endX, endY = 696, 944

# img = open('./images/todayWeather.png', mode='wb')
# auto.screenshot('screen.png', region=(startX, startY, endX-startX, endY-startY))만사용하면 macos에서 동작안함
im2 = auto.screenshot(region=(startX, startY, endX-startX, endY-startY))
im2.save('java-bigdata-2024/day08/screen.png')
# img.save()
# img.close()

# auto.screenshot('./day08/screen.png', region=(startX, startY, endX-startX, endY-startY))
# with mss.mss() as inst:
#     inst.shot(output='screen.png')
