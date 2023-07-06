class Animal:
    def sound_play(self):
        pass

class Cat(Animal):
    def init(self, sound, name, legs=4):
        self.legs = legs
        self.sound = sound
        self.name = name

    def sound_play(self):
        return f"{self.name}:" +  f"{self.sound}" * 2 

class Dog(Animal):
    def init(self, sound, name, legs=4):
        self.legs = legs
        self.sound = sound
        self.name = name

    def sound_play(self):
        return f"{self.name}:" +  f"{self.sound}" * 3

animals = [Cat(name="르미", sound="Meow"), Dog(name="스트", sound="Bark")]
for animal in animals:
    print(animal.sound_play())