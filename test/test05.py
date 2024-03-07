from datetime import datetime

def main():
    # 현재 날짜와 시간을 가져옵니다.
    now = datetime.now()

    # 날짜와 시간을 지정된 형식에 맞게 문자열로 변환합니다.
    formatted_datetime = now.strftime("%Y\\%m%%%d %H**%M//%S")

    # 출력합니다.
    print(formatted_datetime)

if __name__ == "__main__":
    main()
