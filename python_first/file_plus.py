file = open("context2.txt", "a+")
file.write("content")
file.close()

file = open("context3.txt", "a")
file.write("content")
file.close()

"""
r, r+는 파일이 없으면 에러
w, w+, a, a+는 파일이 없으면 생성
"""