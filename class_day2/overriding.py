class Animal:
    def __init__(self,name):
        self.name = name

    def speak(self):
        print("동물이 소리를 냅니다.")

class Dog(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def speak(self):
        super().speak()
        print("개가 짖습니다.")

my_dog = Dog("스트", "검은색")
print(my_dog.name)
print(my_dog.color)
my_dog.speak()

#자식과 부모의 함수가 겹칠 경우 자식의 함수가 우선출력
#overriding = 덮어쓰기