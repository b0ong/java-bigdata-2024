# file: p26_exceptionHandle.py
# desc: 예외 처리
# 오류(Error) = 소스코드 상에 빨간줄(노란줄)은 오류
# 예외(Exception) : 프로그램 실행 중에 생기는 오류(비정상적 종료)

# 1. 파일 읽어서

try:    
    f = open('./sanple.txt', mode= 'r', encoding='utf-8')
    # 블라블라블라블라
    res = f.readlines()
    print(res)
except:
    print('파일오픈 예외발생')
finally:
    try:
        f.close()
    except NameError as e:
        print('파일 오픈실패')
    else: # 오류가 없는 경우 수행
        f.close()

# 2. 계산결과
#  try:
#      print(5 / 0)
#  except ZeroDivisionError as e:
#      print('나누기 예외발생',e.args)

# a, b =5, 3

# if a == b:
#     print(True) 