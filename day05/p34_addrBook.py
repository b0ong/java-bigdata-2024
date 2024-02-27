# file: p34_addrBook.py
# desc: 콘솔 주소록 프로그램

class Contact: # 주소록 클래스
    # 생성자
    def __init__(self, name, phoneNumber, eMail, addr) -> None:
        self.__name = name
        self.__phoneNumber = phoneNumber
        self.__eMail = eMail
        self.__addr = addr
        
        #  사용자가 원하는 형태로 출력
    def __str__(self) -> str:   # 원래 출력 <__main__.Contact object at 0x10f446e10>
        res = (f'이  름: {self.__name}\n'
               f'핸드폰: {self.__phoneNumber}\n'
               f'이메일: {self.__eMail}\n'
               f'주  소: {self.__addr}')
        return res
        
def run():
    first = Contact(name= '홍길동', phoneNumber= '010-9999-9999', eMail = 'hgd@naver.com', addr = '경성' )
    print(first)

if __name__ == '__main__': # main 엔트리
    print('프로그램 시작')
    run() # 메인함수 실행

print('프로그램 종료')