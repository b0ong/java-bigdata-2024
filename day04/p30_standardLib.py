# file: p30_standardLib.py
# desc: 표준 라이브러리(빌트인) 학습

import datetime
import time
import random

print(datetime.date(2024, 2, 26)) # 현재의 OS에 맞춰서 날짜형으로 변경

## ⭐️정말 많이 사용함
curr = datetime.datetime.now() # 현재의 년월일시분초를 알려줌
print(curr) 

print(curr.weekday()) # 0은 월요일 ~ 6 일요일
print(curr.year)
print(curr.month)
print(curr.day)
print(curr.hour)
print(curr.minute)
print(curr.second)

print(f'{curr.year}년 {curr.month:02d}월 {curr.day}일 {curr.hour}시 {curr.minute}분') 

curr2 = time.localtime() # time으로 찾는 localtime() 잘 안쓰임
print(curr2)

## 엄청 많이 사용함
for i in range(5):
    print(f'{i}출력')
    # time.sleep(2) # 2초 씩 잠시 멈춤

## 
print(random.random())  # 0  ~ 1 사이의 소수점
print(random.randint(1, 45))  # 1 ~ 45 사이

## 로또
result = []
total = []

for i in range(5):
    while True:
        val = random.randint(1, 45)
        while val not in result:
            result.append(val)
            
        if len(result) == 6: break
        
    result.sort()
    total.append(result)
    result = []

print(total)

## 내부라이버리 중 웹사이트
# import urllib
# 요청(request) > 응답(response)
# from urllib.request import Request, urlopen

# req = Request('https://www.naver.com')
# res = urlopen(req)

# print(res.status) # 응답코드 200 
# print(res.read()) #내용가져오기
import requests
from bs4 import BeautifulSoup

# res = requests.get('https://www.naver.com')
# print(res.status_code)
# print(res.content) # 내용가져오기

res = requests.get('https://www.naver.com')

if res.status_code == 200:
    html = res.text
    soup = BeautifulSoup(html, 'html.parser')
    print(soup)