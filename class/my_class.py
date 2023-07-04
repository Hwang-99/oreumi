class my_health_diary:
    def __init__(self,name,weight,gym,running):
        self.name = name
        self.weight = weight
        self.gym = gym
        self.running = running
    
  
        user =  my_health_diary("황찬혁", 0, 50, 0, 10)


    def user_act(self):
        while self.gym <= 100 :
            action = input("오늘은 무엇을 할까? (1: 쇠질하기 / 2: 체육관 방문 / 3: 3키로 뛰기 / 4: 집에서 쉬기)")
        if action == "1":
            self.weight_up()
        elif action == "2":
            self.gym_visit()
        elif action =="3":
            self.running_time()
        elif action == "4":
            print("아무것도 하기 싫다...")
        else:
            print("다시 입력해보자.")
    
    def weight_up(self,weight):
        self.weight += 10
        print(f"{self.name}의 최대 중량 무게가 {self.weight}kg 만큼 늘었다!")

    def gym_visit(self,gym):
        self.gym += 1
        print(f"{self.name}의 체육관 방문수가 {self.gym}회 만큼 늘었다!")

    def running_time (self,running):
        self.running -= 1
        print(f"{self.name}의 3키로 뛰기 시간이 {self.running}분 만큼 줄었다!")