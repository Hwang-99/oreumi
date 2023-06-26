# 파일을 출력
file_path = "title.text"

file = open(file_path, 'r', encoding='utf-8')

content = file.read()
print(content)

file.close()


# 파일에 입력
file_path = "context.text"

file = open(file_path, 'a', encoding='utf-8')

file.write("Another context.")

file.close()