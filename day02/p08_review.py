#file: p08_review.py
#desc: 되새김 문제

#  Q 2,3,5,6,10

# Q2
a = 13
print('a는 ', end='')
if a % 2 == 0:
    print('짝수')
else:
    print('홀수')

# Q3
pin = '881120-1068234' ## 문자열 자르기
yyyymmdd = pin.split('-')[0]
num = pin.split('-')[1]
print(yyyymmdd)
print(num)

# Q5
a = 'a:b:c:d' ## 문자열 재배치
b = a.replace(':','#')
print(b)

# Q6
a = [1, 3, 5, 4, 2] ## 내림차순
a.sort()
a.sort(reverse=True)
print(a)

#Q10
a = {'A':90, 'B':80, 'C':70}    ## pop 사용 (값꺼내기)
result = a.pop('B')
print(a)
print(result)