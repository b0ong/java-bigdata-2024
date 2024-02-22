# file: p09_ifCondition.py
# desc: if 제어문

money = 2700

if money >= 5000:
    # indentation (들여쓰기) 기본값: tab == space * 
    print('택시타고가') # tab 잘 맞추기 아니면 에러남.
    print('부럽농')
elif money < 5000 and money >= 2500:
    print('기사님 일광역까지만 가주세여')
    print('걸어가농..')
    
else:
    print('걸어가라')
    print('그지농..')
    
a,b,c,d = 10,5,7,9
    
print(a >= b) # True
print(c > d) # False

print(a >= b and c > d) # False 1 and 1 == 1 / 1 and 0 == 0 / 0 and 1 == 0 / 0 and 0 == 0
print(a >= b or c > d) # True 1 or 1 == 1 / 1 or 0 == 1 / 0 or 1 == 0 / 0 or 0 == 0
## and 80% 사용 / or 20% 사용

print(not (a >= b)) #False
## prin() end 옵션(정말 많이 사용), sep옵션
print(1 in [1,3,5,7,9], end = ',') # True
print(6 in [1,3,5,7,9]) #False

print('13579', '246810', sep='|')

score = 60

# 파이썬에서는 조건 연산자를 잘 안씀
# (score >= 60) ? "sucess" : "failure" )
print( 'success' if score >= 60 else 'falure')

