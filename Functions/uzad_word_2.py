"""
Duotas listas skaiciu – [1, 2, 3, 4, 5, 6, 18, 90, 118, 991,  196151]. Grazinti dicta, kuris butu suskaiciuota kiek is siu skaiciu yra lyginiu, kiek nelyginiu:
"""

num_list = [1, 2, 3, 4, 5, 6, 18, 90, 118, 991, 196151]

res_dict = {}
num_even = []
num_odd = []
for num in num_list:
    if num % 2 == 0:
        num_even.append(num)
    else:
        num_odd.append(num)

res_dict[sum(num_even)] = len(num_even)
res_dict[sum(num_odd)] = len(num_odd)

print(res_dict)
