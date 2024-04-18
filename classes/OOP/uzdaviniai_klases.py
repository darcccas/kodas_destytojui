# Sukurkite Calculator klasę su pagrindinėmis funkcijomis: sudėti, dalyti, dauginti, atimti ir t. t.. Inicijuokite klasę ir parodykite keletą skaičiavimų.
class Calculiator:
    def __init__(self, x: int = 1, y: int = 1):
        self.x = x
        self.y = y

    def sum(self):
        return self.x + self.y

    def dev(self):
        return self.x / self.y

    def multi(self):
        return self.x * self.y

    def minus(self):
        return self.x - self.y


calc = Calculiator(4, 2)

print(calc.dev())
print(calc.sum())
print(calc.multi())
print(calc.minus())

"""
Darbuotojo klasėje sukurkite egzempliorių atributus fullname (vardas, pavardė) ir email (el. paštas). Turint asmens vardą ir pavardę:

Vardą ir pavardę suformuokite paprasčiausiai sujungdami vardą ir pavardę, atskiriamus tarpeliu.

Elektroninį paštą suformuokite sujungdami vardą ir pavardę, tarp jų įterpdami simbolį . Pabaigoje įrašydami @company.com. Įsitikinkite, kad visas el. laiškas būtų** rašomas mažosiomis raidėmis**.
"""


class Labor:
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname
        self.fullname = f"{name} {surname}"
        self.email = f"{name.lower()}.{surname.lower()}@company.com"


labor = Labor("Darius", "Kom")

print(labor.fullname)


# Sukurkite knygos klasę Book, kuri turi du atributus:


class Book:
    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author

    def get_title(self):
        return f"Title {self.name}"

    def get_author(self):
        return f"Author {self.author}"


PP = Book("Pride and Prejudice", "Jane Austen")
H = Book("Hamlet", "William" "Shakespears")
WP = Book("War and Peace", "Lew Tolstoj")
HP = Book("Harry Potter", "J.K. Roling")

print(HP.name)
print(HP.author)
print(HP.get_title())
print(HP.get_author())


# uzdavinys


class Country:
    def __init__(self, name: str, population: int, area: int):
        self.name = name
        self.pop = population
        self.area = area
        self.is_big = population > 20000000 or area > 30000000

    def compare(self, other_country):
        if self.pop / self.area > other_country.pop / other_country.area:
            size = "larger"
        else:
            size = "smaller"
        return f"{self.name} has {size} population density than {other_country.name}"


australia = Country("Australia", 23545500, 7692024)
andorra = Country("Andorra", 76098, 468)

print(andorra.compare(australia))
print(australia.is_big)
print(andorra.is_big)
