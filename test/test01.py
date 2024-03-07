def check_gender(id_number):
    # 주민등록번호에서 7번째 숫자를 확인하여 성별을 판별합니다.
    gender_digit = int(id_number[6])
    if gender_digit in [1, 3, 5]:
        return "남성"
    elif gender_digit in [2, 4, 6]:
        return "여성"
    else:
        return "알 수 없음"

def main():
    while True:
        id_number = input("주민등록번호를 입력하세요 (예: 123456-1234567): ")
        # 입력된 주민등록번호에서 '-'를 제거합니다.
        id_number = id_number.replace('-', '')
        # 입력된 주민등록번호가 유효한지 확인합니다.
        if len(id_number) != 13 or not id_number.isdigit():
            print("올바른 주민등록번호를 입력하세요.")
            continue
        gender = check_gender(id_number)
        print(f"입력하신 주민등록번호는 {gender}입니다.")

        choice = input("다른 주민등록번호를 확인하시겠습니까? (예/아니오): ")
        if choice.lower() != '예':
            break

if __name__ == "__main__":
    main()
