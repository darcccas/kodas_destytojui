import random


def generate_ran_number() -> str:
    return str(random.randint(0, 9999)).zfill(4)


def imput_time_gues():
    return int(input("Iveskite, kiek kartu norite speti: "))


def input_gues():
    return input("Iveskite savo spejima: ")


def count_bulls_cows(gen_num, try_num):
    bull, cow = 0, 0
    for index, number in enumerate(try_num):
        if number == gen_num[index]:
            bull += 1
        elif number in gen_num:
            cow += 1
    return bull, cow


print(count_bulls_cows(generate_ran_number(), input_gues()))


def main():
    gen_number = generate_ran_number()
    try_number = imput_time_gues()
    print(gen_number)
    for i in range(try_number):

        if input_gues() == gen_number:

            return "You are a WINNER"


# print(main())
