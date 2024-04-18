class Color:
    def __init__(self):
        self.color = "brindal"


class Animal:
    legs = 4  # priejimas self.legs jei naudojame kazkurioje funcijoje, bet ne konstrukturiuje

    def __init__(self, age: int = 10, name: str = "feja", *args, **kwargs):
        self.name = name
        self.age = age
        self.age_after_ten_years = self.age + 10
        self.color = Color()

    def run(self, speed: str = "Greitai"):
        return f"{speed} bega {self.name}, jos spalva {self.color.color}, jai yra {self.age} metu"

    def barks(self, volume: str = "tyliai"):
        return f"{self.name} kartais labai {volume} loja"

    def runs_barks(self, speed: str = "Greitai", volume: str = "tyliai"):
        return self.run(speed=speed), self.barks(volume=volume)


animal = Animal()

print(Animal().name, Animal())

animal.age = 15

print(animal.name, animal.age_after_ten_years, animal.color.color)

# print(animal.run())

print(Animal().runs_barks(speed="letai", volume="triuksmingai"))
