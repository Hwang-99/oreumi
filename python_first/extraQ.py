'''문제1.
사용자로부터 숫자를 입력받아 해당 숫자의 자리수를
출력하는 프로그램을 작성하세요

예시입력
124

예시출력
3'''

# 정답 1.
# number = input("숫자를 입력하세요")
# length = len(number)
# print("입력하신 숫자는 %d 자리입니다." % length)

'''문제2.
사용자로부터 날짜를 입력받아 연도, 월, 일로 분리하여
출력하는 프로그램을 작성하세요.

예시입력
2023-06-26

예시출력
연도: 2023
월: 06
일: 26'''

# 정답 2.
# today = input ("날짜를 입력하세요 (- 포함)").split('-')
# print("연도:" + today[0] + "\n" + "월:" + today[1] + "\n" + "일:" + today[2])


'''문제3.
사용자로부터 정수를 입력받아 해당 정수를 2로 나눈 몫과
나머지를 출력하는 프로그램을 작성하세요.'''

# 정답 3.
# number = input("2로 나눌 값을 입력하세요.")
# result_number = int(number)
# print(number)
# print("몫은" + str((result_number // 2)) + ", 나머지는" + str((result_number % 2)))

'''문제4.
사용자로부터 섭씨 온도를 입력받아 화씨 온도로 변환하여 출력하는 프로그램을 작성하세요.
예를 들어, 20도의 섭씨 온도를 화씨 온도로 변환하려면 다음과 같은 과정을 거칩니다:
* 섭씨 온도인 20에 9를 곱합니다: 20 * 9 = 180
* 곱한 결과에 5를 나눕니다: 180 / 5 = 36
* 나눈 결과에 32를 더합니다: 36 + 32 = 68'''

# 정답 4.
# tem = input("화씨를 입력하세요.")
# result_tem = int(tem)
# print("화씨: " + str(((result_tem*9)/5)+32) + "℉")

'''문제5.
사용자로부터 파일 이름과 내용을 입력받아 텍스트파일(.txt)을 생성하고
입력한 내용을 파일에 저장하는 프로그램을 작성하세요. 
그리고, 입력한 파일 이름을 가지고 있는 동물이 파일을 열어 내용을 확인하는 장면을 가정하여 출력하는 프로그램을 작성해보세요.

예시 입출력:
파일 이름을 입력하세요: catFile.txt
파일 내용을 입력하세요: 파일내용입니다
파일 생성 및 내용 저장이 완료되었습니다.
파일을 열어 내용을 확인하는 동물이 있습니다...
고양이가 catFile.txt 파일을 열어 아래 내용을 확인합니다.
파일 내용: 파일내용입니다
'''

file_name = input("파일 이름을 입력하세요:")
file_text = input("파일 내용을 입력하세요:")

with open(file_name, "w+") as file: file.write(file_text)
print("""파일 생성 및 내용이 저장되었습니다.
파일을 열어 내용을 확인하는 동물이 있습니다...""")

# file.seek(file_name)
file_text = file.read()
print("고양이가" + file_name + "파일을 열어 아래 내용을 확인합니다.")
with open(file_name, "r") as file:
    file_content = file.read()
print(file_content)