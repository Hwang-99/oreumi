educator = [{"이름": "김도언", "나이": 20, "직업": "강사", "일일퀴즈성적": [10, 20, 20]},
{"이름": "이예원", "나이": 21, "직업": "멘토", "일일퀴즈성적": [9, 19, 19]}]
educator_add_info = {"회사": "이스트소프트", "강의기수":"2기"}

for person in educator:
    person.update(educator_add_info)

print(educator)
