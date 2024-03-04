# file: p51_keyboardAuto.py
# desc: 키보드 자동화 with PyAutoGui
''' 
한글입력은 pyperclip
'''
import pyautogui as auto

# auto.mouseInfo()
# auto.click(355, 499)
auto.press('enter')
auto.write("print('Hello, Python!')",interval =0.01)
auto.write("\n",interval =0.01)
auto.typewrite("print('Life is short, You need python.')",interval =0.01) #write()와 동일

# 키보드 프레스 기능
auto.press('enter'); auto.press('A')

#키보드 단축키로 입력
# auto.hotkey('ctrl','a') # 전체 선택
# auto.hotkey('ctrl','c') # 복사
# auto.press('esc')
# auto.press('\n'); auto.press('\n'); auto.press('\n') 
# auto.hotkey('ctrl','v') # 붙여넣기

auto.write('안녕하세요, 파이썬입니다.')
print('Life is short, You need python.')
