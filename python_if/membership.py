
mom_fruits =["멜론", "수박", "배", "딸기"]

favorite_fruits = ["사과", "수박", "배"]

eat_list = []

for fruit in mom_fruits:
    if fruit not in favorite_fruits:
        print("먹는다!")
        eat_list.append(fruit)
    else:
        print("안먹는다!")
print(eat_list)

# if fruit in fruits:
#     print("내가 좋아하는 과일이다!")
# else:
#     print("별로 좋아하지는 않는다.")