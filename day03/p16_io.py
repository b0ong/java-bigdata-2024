# flie: p16_io.py
# desc:입출력

# input() 함수 기본유형
res = input('인사말을 적으세요 > ')
print(res)

#num = input('곱할 수를 적으세요 > ')
#print(type(num))
# input() 받는 값은 모두 문자열
#num = int(num)
#print(num * 2)
# 숫자를 입력받아서 계산 등을 할때는 형변환이 필요함.

num = int(input('2로 곱할 숫자 입력 > '))
print(num * 2)

## 여러 값을 입력
#int(40.2) # 40
#int('50') # 50
#int('40.2') # X 
#int((10,20,30) ) # X 튜플을 바로 int로 변경할 수 있는 방법이 X

# 튜플의 () 중 할당을 받는 쪽의 ()는 생략가능
# (a1, a2, a3) = int(input('합산 3개 값을 입력(구분자는 space) >').split(' '))
(a1, a2, a3) = map(int, input('합산 3개 값을 입력(구분자는 space) >').split(' '))       # 맨앞에 () 생략가능
print(a1)
print(a2)
print(a3)
a1 = int(a1)
a2 = int(a2)
a3 = int(a3)
sum = a1 + a2 + a3
print(f'합계는 {sum}')

