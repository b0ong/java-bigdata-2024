def main():
    # 영어 요일과 한국어 요일을 매핑하는 딕셔너리 생성
    day_mapping = {
        'MON': '월요일',
        'TUE': '화요일',
        'WED': '수요일',
        'TUR': '목요일',
        'FRI': '금요일',
        'SAT': '토요일',
        'SUN': '일요일'
    }

    # 사용자로부터 영어 요일 입력 받기
    english_day = input("일주일의 영어 요일을 입력하세요 (예: MON, TUE, WED, TUR, FRI, SAT, SUN): ")

    # 입력된 영어 요일이 딕셔너리에 있는지 확인하고 해당하는 한국어 요일 출력
    if english_day in day_mapping:
        korean_day = day_mapping[english_day]
        print(f"오늘은 {korean_day} 입니다.")
    else:
        print("잘못된 요일을 입력하셨습니다.")

if __name__ == "__main__":
    main()
