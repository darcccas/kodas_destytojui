# def find_two_best(price_list: list, amount):
#     actual_shoes = [price for price in price_list if price < amount]
#     print(actual_shoes)
#     lowest_price = max(actual_shoes) * 2
#     for index, price in enumerate(actual_shoes[:-1]):
#         print(index, price)   # rekia imti iki priespaskutines poros
#         for second_price in actual_shoes[index+1:]:
#             shoes_price = price + second_price
#
#             if shoes_price < lowest_price:
#                 lowest_price = shoes_price
#                 print(lowest_price)
#
# money = 20
# prices = [2.45, 1.45, 8.98, 10.45, 18.40, 20]
#
# find_two_best(prices, money)

def add_srting(value: list, end_string="string") -> list:
    return [f"{x}_{end_string}" for x in value]


data = ["asda", "sd", 5]
end_string = "nx"
print(add_srting(value=data, end_string=end_string))


# Sukurkite mini python programą, kuri kaip įvestį paimtų du skaičius ir grąžintų jų sumą, atimtį, dalybą, daugybą.

def number_math(num1: int, num2: int) -> tuple:
    return num1 - num2, num1 / num2, num1 * num2, num1 + num2


number1 = 10
number2 = 5

print(number_math(num1=number1, num2=number2))


# Sukurkite funkciją, kuri grąžintų tik unikalius simbolius turinčias string reikšmes.

def unic_string(text: str) -> list:
    return [word for word in text.split() if len(set(word)) == len(word)]


'''
Parašykite programą, apibrėžiančią funkciją extract_email_addresses(), kuri priima tekstą kaip įvestį ir iš teksto ištraukia visus el. pašto adresus.
'''


def extract_email_addresses(text: str) -> list:
    return [data for data in text.split() if "@" in data]


long_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam at elit nec nisi lobortis luctus. Ut faucibus, lorem@example.com quis hendrerit lacinia, ipsum odio tristique purus, at suscipit quam felis eu purus. Quisque ac lorem vel ante scelerisque suscipit. Nam eu mauris at leo tristique fermentum. Sed varius libero at eros malesuada, sed venenatis justo mattis. Vestibulum@example.net eu dolor non leo lacinia tincidunt. Fusce tristique lacus nec mauris fermentum, at placerat sapien feugiat. Phasellus@example.org finibus vulputate tellus, nec consectetur risus. Curabitur et ligula et ligula pulvinar varius eget eu arcu. Integer at ligula vitae libero facilisis fermentum. Sed@example.co.uk dapibus malesuada orci, id eleifend purus aliquam eu. Donec condimentum, libero eget interdum consequat, odio justo convallis sem, ut ultricies velit velit@example.io eget lacus. In hac habitasse platea dictumst. Maecenas ac libero in velit consequat interdum. Sed eget nisl vel ipsum hendrerit interdum. Fusce id fermentum lacus, ut pulvinar felis. Sed efficitur aliquam nulla, eget convallis neque@example.biz."

print(extract_email_addresses(long_text))

print(unic_string(long_text))


#antros dalies uzdaviniai: ar sarasu elementu suma sudaro vienodus elementus

def sum_list_values(a=list, b=list) ->bool:
    print(list(zip(a, b)))
    if len(a) == len(b):
        res_list = [sum(ab) for ab in zip(a, b)]
        return len(set(res_list)) == 1
    return False


print(sum_list_values(a=[1, 8, 5, 0, -1, 7], b=[0, -7, -4, 1, 2, -6]))

#lyginiu nelyginiu skaiciu sumu skirtumas

def war_of_numbers(a=list) ->int:
    return abs(sum([num for num in a if num % 2 == 0]) - sum([num for num in a if num % 2 != 0]))

print(war_of_numbers([2, 47, 8, 7 ,9]))

'''
Jums duotas bigramų masyvas ir žodžių masyvas. Parašykite funkciją, kuri grąžintų True, jei iš šio masyvo galima rasti kiekvieną bigramą bent vieną kartą žodžių masyve.
'''

def can_find(bigrams=list, words=list) ->bool:
    for bigram in bigrams:
        if bigram not in " ".join(words):
            return False
    return True

#
print(can_find(["at", "be", "th", "au"], ["beautiful", "the", "hat"]) )
print(can_find(["ay", "be", "ta", "cu"], ["maybe", "beta", "abet", "course"]))
print(can_find(["th", "fo", "ma", "or"], ["the", "many", "for", "forest"]))
print(can_find(["oo", "mi", "ki", "la"], ["milk", "chocolate", "cooks", "cooks"]))
# # "cu" nėra nė viename iš žodžių.
# can_find(["th", "fo", "ma", "or"], ["the", "many", "for", "forest"]) ➞ True
#can_find(["oo", "mi", "ki", "la"], ["milk", "chocolate", "cooks", "cooks"]) ➞ False