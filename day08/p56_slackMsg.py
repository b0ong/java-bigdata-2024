# file: p56_slackMsg.py
# desc: 슬랙으로 스마트폰 메세지 보내기

'''
순서
1. https://api.slack.com/ 에서 your apps > Careate your first app
2. From Scratch 클릭 > 앱이름은 '영어로만!!'
3. 워크스페이스 선택
4. Incomming Webhook > On > add New Webhook to Workspace 클릭 > 채널선택 > 허용
'''

import requests
import json

slack_url = 'https://hooks.slack.com/services/***/B***/****' # 깃헙 올리기전에 지우기!

headers = { 'Content-Type': 'application/json'}
data = { 'text': 'Python에서 보내는 메세지!'}

res = requests.post(slack_url, headers=headers, data=json.dumps(data))
if res.status_code == 200:
    print('메세지 전송 성공')
else:
    print('메세지 전송 실패')