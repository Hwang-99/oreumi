class Car:

    window = 2

    # __ __ = 매직 메서드 or 언더 메서드
    # __init__ = class가 실행됐을 때 이부분을 먼저 실행
    def __init__(self, people):
        self.people = people
        self.window = 2
        self.wheel = 4

    def brake(self): #self는
        print(f"{self.people}(이)가 brake!")
        # pass #아무것도 받지 않고 싶을 때 pass

    def accelerate(self):
        print("accelerate!")
        

my_car = Car("김도언")
my_car.brake()
