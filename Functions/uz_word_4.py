"""
Yra duotas listas su domenimis:

[3, 2, ‚‘m‘, ‚lele‘, (1, 2, 3), [1, 2, 3], {‚vienas‘: 1,‘du‘: 2})

Reikai gražinti diktą, kuriame raktas butu reiksme duota reiksme, o rezultatas:

Jei stringas – simboliu skaicius

Jei integeris – kvadratas

Jei listas = suma

Jei dictas – value suma.

Jei tuple = sudauginti visus skaicius
"""

data_list = [3, 2, "m", "lele", (3, 2, 3), [1, 2, 3], {"vienas": 1, "du": 2}]

res_dict = {}

for data in data_list:
    if type(data) == str:
        res_dict[data] = len(data)
    elif type(data) == int:
        res_dict[data] = data**2
    elif type(data) == list:
        res_dict[str(data)] = sum(data)
    elif type(data) == dict:
        num = 0
        for value in data.values():
            num += value
        res_dict[str(data)] = num
    elif type(data) == tuple:
        num = 1
        for value in data:
            num *= value
        res_dict[data] = num

print(res_dict)
