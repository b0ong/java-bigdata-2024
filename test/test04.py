# result.txt 파일을 쓰기 모드로 열어줍니다.
with open('result.txt', 'w') as f:
  # 1부터 1000까지 반복합니다.
  num = 1
  while num <= 1000:
    # 3과 5의 배수인지 확인합니다.
    if num % 3 == 0 and num % 5 == 0:
      # 3과 5의 배수라면 result.txt 파일에 저장합니다.
      f.write(str(num) + '\n')
    # 다음 숫자로 넘어갑니다.
    num += 1