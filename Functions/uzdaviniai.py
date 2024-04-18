import math


def caldict(data=dict, necessary_key=list, deleted_keys=list) -> dict:
    res = {}
    new_data = data.copy()
    for key in data:
        if key in necessary_key:
            res[key] = data[key]
        if key in deleted_keys:
            del new_data[key]
    return res, new_data


Data = {1: "vienas", 2: "du", 3: "trys", 4: "keturi"}

nece = [1, 2]
delet = [3]

print(caldict(Data, nece, delet))


def sliced_list(numbers=list, number=int) -> list:
    return [
        numbers[i * number : i * number + number]
        for i in range(math.ceil(len(numbers) / number))
    ]


num_list = [1, 2, 3, 4, 5, 45, 7, 6, 78, 54, 654, 45]
num = 5

print(sliced_list(numbers=num_list, number=num))
