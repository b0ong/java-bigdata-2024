# file: p21_review.py
# desc: 되새김 문제

# Q7

f = open('./day03/test1.txt','w')   #파일만들려면 w
f.write('Life is too short\n you need java')
f.close()

# body = [body[0], body[1].replace('java', 'python')] 
# f = open('./day03/test1.txt', mode='w', encoding='utf-8')
# f.write(body[0] + body[1])
# f.close()

# f = open('./day03/test.txt', 'r')
f = open('./day03/test1.txt', 'r')
body = f.read() # 단 read() 함수는 텍스트가 길면 문장이 잘려나온다.
f.close()
body = body.replace('java','python')
f = open('./day03/test1.txt', mode = 'w', encoding='utf-8') 
# 파일이 있어서 덮어쓰기느낌?
f.write(body)
f.close()