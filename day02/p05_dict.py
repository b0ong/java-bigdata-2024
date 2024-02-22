# file: p05_dict.py
# desc: 딕셔너리 자료형, 집합 학습

## key와 value가 둘다 있어야한다. 단, key는 되도록이면 문자열로 작성
## 딕셔너리 구성
spiderMan = { 'name':'Peter Parker', 'age':'18', 'weapon':'Web shooter', 'friends':['ironMan','Thor','Captain America']}
##출력
print(spiderMan)
print(spiderMan['name'])

## 값추가
spiderMan['job'] = 'CameraMan' 
print(spiderMan)

## 값삭제
del spiderMan['friends']        ## del 사용
print(spiderMan)

## 딕셔너리 함수
print(spiderMan.keys()) # 딕셔너리에 현재 존재하는 키 목록 출력
print(list(spiderMan.keys())) # 키목록을 리스트형태로 형변환
print(spiderMan.items())    #딕셔너리 모든 아이템 출력
print(spiderMan.get('job'))  # 딕셔너리의 값 가져오기

print('friends' in spiderMan) # 딕셔너리안에 키가 있는 지 확인
print(spiderMan.values())

res = spiderMan.pop('job') # 값을 꺼내기 
print(res)
print(spiderMan.pop('age'))
print(spiderMan)

## 데이터 삭제
spiderMan.clear()
print(spiderMan)

del spiderMan # 완전삭제
print(spiderMan)

## 집합(실무에 거의 사용안함): 중복된 값은 하나로 합침 (중복 허용X), 순서 X 
#set([1,2,3,4,3,4,2,1]) = {1,2,3,4} or {2,3,1,4} 등등(순서가 없기 때문)