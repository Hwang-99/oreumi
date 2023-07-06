import re

# pattern = r"b.t"
# string = "bat, bet, bit, but, autt"

#pattern = r"ab+c" #b가 1개 이상
#string = "abcabc"

# pattern = r"ab*c" #b가 0개 이상
# string ="ac, abc, abbc, abbbc, abdc"

# pattern = r"(ab)+c"
# string = "abc, ababc, abababc, ab, aabb"

# pattern = r"[aeiou]"
# string = "apple, orange, banana"

# pattern = r"[0-9]"
# string = "1234567890"

# pattern = r"\d+"
# string = "I have 10 apples and 5 bananas"

# pattern = r"\w+"
# string = "Hello, World! 123"

# pattern = r"^Hello" #시작점부터
# pattern = r"Python!$" #끝점부터
# string = "Hello, World! Hello, Python!"

# pattern = r"a{1,3}"
# string = "ab, abc, aabc, aaabc"

# pattern = r"a|b"
# string = "ab, abc, aabc, aaabc"

# pattern = r"\d{2,3}\-\d{3,4}\-\d{4}"
# string = "안녕하세요. 저의 전화번호는 !-010-1234-5678-!입니다. 다른 전화번호는 !-02-987-6543-!입니다. 125!22%13. 지역번호가 155542-10-1"

# result = re.findall(pattern, string)
# print(result)

# pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
# string = "안녕하세요. 이메일 주소는 abc@example.com입니다. 다른 이메일은 ab_TE@hcu.co.kr이고, x_yz@hotmail.net도 있습니다."

# result = re.findall(pattern, string)
# print(result)

string = "문장 속에는 다양한 URL이 있습니다. https://www.example.com/, http://subdomain.example.co.kr/, www.google.com, ftp://fileserver.example.org, 이렇게 다양한 형식의 URL이 있습니다."
pattern = r"[\w/]+\.[\w/.]+\.[a-z/]"
# result = re.findall(pattern, string)
result = re.sub(pattern,"", string)
print(result)