import re


text = "Hello, SeongGi. This is my password 125@1"
pattern = r'\d{2,}|@'

for i in re.findall(pattern, text):
     try:
          print(int(i))
     except:
          print("숫자가 아닙니다.")