class Animal:
    def __init__(self, age: int = 10, color: str = "pink"):
        self.color = color
        self.age = age

    def eat(self):
        print("eat")

    def make_sound(self):
        print("loud")


class Bird(Animal):
    # def __init__(self, age, color, type: str = "Water bird"):
    #     super().__init__(age, color)
    #     self.type = type

    def fly(self):
        print("fly")


class Mamel(Animal):
    pass


class Mammoth(Mamel):
    def __init__(self, age, color):
        super().__init__(age, color)

    def walk(self):
        return print("walk")


class Hybrid(Mammoth, Bird):
    pass


bird = Bird()
mammoth = Mammoth(15, "grey")
hybrid_animl = Hybrid(10, "black")
print(bird.color)
print(mammoth.age)
print(hybrid_animl.make_sound())
