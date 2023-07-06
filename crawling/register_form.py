import re
import sys
from datetime import datetime

def validate_password(password):
    if len(password) < 8:
        return False

    if re.search(r'(.)\1{1,}', password) is not None:
        return False

    if not any(c.islower() for c in password):
        return False

    if not any(c.isupper() for c in password):
        return False

    if not any(c.isdigit() for c in password):
        return False

    if not any(not c.isalnum() for c in password):
        return False

    if ' ' in password:
        return False

    return True

def validate_resident(resident):
    if len(resident) != 14:
        return False

    if not resident[:6].isdigit() or not resident[7:].isdigit():
        return False

    return True

def get_gender(resident):
    gender_digit = int(resident[7])
    return '여성' if gender_digit % 2 == 0 or gender_digit % 4 == 0 else '남성'

def get_current_date():
    now = datetime.now()
    return now.strftime("%Y년 %m월 %d일")

def main():
    password = input("비밀번호를 입력하세요: ")
    while not validate_password(password):
        print("비밀번호가 조건에 맞지 않습니다. 다시 입력해주세요.")
        print("(8자리 이상,영문 대,소문자/숫자/특수문자 포함, 2자리 연속 같은 문자 사용 금지)")
        password = input("비밀번호를 입력하세요: ")

    print("강력한 비밀번호입니다.")

    password_confirm = input("비밀번호를 한번 더 입력하세요: ")
    attempt = 1
    while password_confirm != password:
        if attempt >= 3:
            sys.exit("비밀번호 확인이 3회 이상 실패하였습니다. 프로그램을 종료합니다.")
        print("비밀번호가 일치하지 않습니다. 다시 입력해주세요.")
        password_confirm = input("비밀번호를 한번 더 입력하세요: ")
        attempt += 1

    print("비밀번호 확인이 완료되었습니다.")

    resident = input("주민등록번호를 입력하세요(-포함): ")
    while not validate_resident(resident):
        print("주민등록번호 형식이 올바르지 않습니다. 다시 입력해주세요.")
        resident = input("주민등록번호를 입력하세요(-포함): ")

    gender = get_gender(resident)
    print(f"회원성별은 {gender}입니다.")

    join_date = get_current_date()
    print(f"가입일은 {join_date} 입니다.")

if __name__ == "__main__":
    main()