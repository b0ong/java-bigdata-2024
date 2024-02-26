# file: p31_externalLib.py
# desc: 외부 라이브러리 사용법

# > pip install LibName
# Successfully installed / Requirement already satisfied 가 나와야함
# pip uninstall LibName
# Successfully uninstalled 나와야함

from faker import Faker

fake = Faker('ko-KR') # 한국어 설정
print(fake.name())
print(fake.address())
# print(fake.phone_number())
# print(fake.profile())

dummyData = [fake.profile() for i in range(10)]
print(dummyData)