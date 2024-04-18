import pyjokes

# print(uzdavinys_karves_buliai.generate_ran_number())


def joke():
    return pyjokes.get_joke()


if __name__ == "__main__":
    print(joke())
