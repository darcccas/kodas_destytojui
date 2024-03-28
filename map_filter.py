import random

import math

"""
DRY - Don't repeat yourself :D
"""


def print_word(word):
    print(f"labas {word}")


def return_word(word):
    return f"labas {word}"


# Raskite visus skaičius nuo 1 iki 1000, kurie dalijasi iš 6.


def find_number_devided(devide):
    return [num for num in range(1, 1001) if num % devide == 0]


# Raskite visus skaičius iš 1-1000, kuriuose yra 9

def find_number_with_number_in(number):
    return [num for num in range(1, 1001) if str(number) in str(num)]


print(find_number_with_number_in(2))


# Sukurkite string iš daugybės žodžių: Apskaičiuokite, kiek žodžių turi raidę e.

def find_word_with_letter(string, letter):
    return [word for word in string.split() if letter in word]


lond_string = "Sukurkite string iš daugybės žodžių: Apskaičiuokite, kiek žodžių turi raidę e."

letter_to_find = "e"

print(find_word_with_letter(lond_string, letter_to_find))

'''
Naudodami tą patį string, kaip ir ankstesniame pratime: apskaičiuokite raidžių, kurios turi daugiau nei 5 simbolius, skaičių.
'''


def find_word_with_len_more_5(string):
    return len([word for word in string.split() if len(word) > 4])


print(find_word_with_len_more_5(lond_string))


# Parašykite programą, kuri patikrintų, ar duotas skaičius yra tobulasis kvadratas.


def find_number_squer_root(number):
    return number == math.isqrt(number) * math.isqrt(number)


print(find_number_squer_root(25))

'''
Lentynoje sudeti batai:
[8.90, 4,90, 13,20, 8,80, 14,00, 12,00]
a) Paskaičiuokite kiek eurų liks žmogui, jei jis šiuo metu pirks dvejus pigiausius batus;
'''

def count_money_left(prices, pcs_to_buy_cheapest, money_have):
    return round(money_have - sum(sorted(prices)[:pcs_to_buy_cheapest]), 2)

price_list = [8.90, 4.90, 13.20, 8.80, 14.00, 12.00]
money = 20
psc_to_buy = 2


print(count_money_left(price_list, psc_to_buy, money))

#b) kokius dvejus batus jam nupirkti, jei jis turi 20 eurų ir nori, kad jam liktų kuo mažiau eurų;

def max_can_buy(prices, have_money):
    pass

# planas savaitgaliui pabaigti, kai galva atsinaujins






shoes_prices = [8.90, 4,90, 13,20, 8,80, 14,00, 12,00]

