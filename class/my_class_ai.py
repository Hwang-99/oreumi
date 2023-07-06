class MyHealthDiary:
    def __init__(self, name, weight, gym, running):
        self.name = name
        self.weight = weight
        self.gym = gym
        self.running = running
    
    def user_act(self):
        while self.weight <= 490:
            action = input("오늘은 무엇을 할까? (1: 쇠질하기 / 2: 체육관 방문 / 3: 3키로 뛰기 / 4: 집에서 쉬기): ")
            if action == "1":
                self.weight_up()
            elif action == "2":
                self.gym_visit()
            elif action == "3":
                self.running_time()
            elif action == "4":
                print("아무것도 하기 싫다...")
            else:
                print("다시 입력해보자.")
        
        print("목표하던 중량인 3대 500을 달성했다!")
    
    def weight_up(self):
        self.weight += 10
        print(f"{self.name}의 3대 중량 무게가 {self.weight}kg 으로 늘었다!")

    def gym_visit(self):
        self.gym += 1
        print(f"{self.name}의 체육관 방문수가 {self.gym}회 만큼 늘었다!")

    def running_time(self):
        self.running -= 1
        print(f"{self.name}의 3키로 뛰기 시간이 {self.running}분 만큼 줄었다!")

user = MyHealthDiary("황찬혁", 100, 0, 10)
user.user_act()