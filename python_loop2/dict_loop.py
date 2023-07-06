a = {"이름": "황찬혁", "나이": 25, "직업": "학생", "일일퀴즈성적": [10, 20, 30]}
b = {"이름": "이예원", "나이": 20, "직업": "멘토", "일일퀴즈성적": [11, 21, 31]}
c = {"전화번호": "010-xxxx-xxxx", "주소":"봉담"}
# for key, value in a.items():
#     print(key, value)

# for key in a.keys():
#     print(key)

# c = []
# for value in a.values():
#     c.append(value)
# print(c)

a.update(c)
print(a)
