# file: p18_flieRead.py
# desc: 텍스트 파일 읽기

f = open('./day03/sample.txt',mode='r', encoding='utf-8')
f2 = open('./day03/dest.txt', mode='w', encoding='utf-8')
###
read = f.readlines()
print('파일에서 읽은 내용> ', read)
for line in read:
    print(line.replace('\n',''))
    f2.write(line)

f.close()
f2.close()