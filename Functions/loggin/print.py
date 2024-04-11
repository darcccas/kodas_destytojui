import logging

# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')

# logging.info('This is an info message')
# logging.warning('This is a warning message')
# logging.error('This is an error message')
# logging.critical('This is a critical message')

def loging_info():
    for _ in range(9):
        logging.info("belekas")

logging.basicConfig(level=logging.DEBUG,filename='data.log', filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')


# Move all the 1s to the end of the array.
# def move_to_end(numbers=list, number=int) ->list:
#     for  num in numbers:
#         if num == number :
#             logging.info(f"Rastas skaicius {num}, perkeltas į galą")
#             numbers.append(num)
#             numbers.remove(num)
#         print(id(numbers))
#     return id(numbers)
#
# num_list = [1, 3, 2, 4, 4, 1]
#
# num = 4

# print(move_to_end(num_list, num))

"""
Sukurkite 3 funkcijas, kurios yra susijusios viena su kita (viena iškviečiama kitoje), ir išbandykite visus logging sunkumo lygius pagal savo projektą.
"""


def check_engine() -> None:
    logging.warning('Engine is not starting')

def check_temperature() -> None:
    logging.critical('Temperature is to high')
def start_car() -> None:
    check_engine()
    check_temperature()


"""
Sukurkite apskaitos programą , kuri paimtų metines pajamas, išlaidas, PVM tarifą (visos reikšmės turi būti kintamos) ir apskaičiuotų pelną, sumokėtus mokesčius 4 skirtingomis valiutomis (USD, EU, JPY, CNY). Visi skaičiavimai ir rezultatai turėtų būti spausdinami ekrane. Visi duomenys ir galimos klaidos turi būti registruojami į failą.
"""

def ernings(got=int, pvm=int, lost=int):
    pass
