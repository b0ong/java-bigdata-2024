# file: p25_review.py
# desc: 되새김문제(p185)

## Q1
def is_odd(number):
    if number %2 == 1:
        return True
    else:
        return False
    
print(is_odd(3))
print(is_odd(4))

## Q2

def avg_numbers(*args):
    result = 0
    for i in args:
        result += i
    return result / len(args)

print(avg_numbers(1,2))
print(avg_numbers(1,2,3,4,5))

## Q3
#(input1, input2) = map(int, input())
# input1 = input('첫 번째 숫자를 입력하세요: ')
# input2 = input('두 번째 숫자를 입력하세요: ')
# input1 = int(input1)
# input2 = int(input2)
# total = input1 + input2
# print(f'두수의 합은{total}입니다.')
    
## Q4

print('you' 'need' 'python')
print('you'+'need'+'python')
print('you', 'need', 'python')
print(''.join(['you', 'need', 'python']))


## Q5

f1 = open('./day03/test1.txt', mode='w', encoding='utf-8')
f1.write('Life is too short')
f1.close()

f2 = open('./day03/test1.txt', mode='r', encoding='utf-8')
print(f2.read())
f2.close()

## Q6

# user_input = input('저장할 내용을 입력하세요')
# f = open('./day03/test1.txt', mode='a', encoding='utf-8')
# f.write(user_input)
# f.write('\n')
# f.close()

## Q8

import sys

args = sys.argv[1:]
for i in args:
    print(i)

