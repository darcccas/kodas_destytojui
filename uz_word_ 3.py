"""
Yra stringas; ‚1asdg16asdg1wg16ewrg1er6gw1‘. Suskaiciuoti ir grazinti dicte kiek yra skaiciu ir kiek yra raidziu.
"""

res_dict = {
    "alphabetic": 0,
    "numeric": 0
}
simbol_string = "1asdg16asdg1wg16ewrg1er6gw1"
for simbol in simbol_string:
    if simbol.isalpha():
        res_dict["alphabetic"] += 1
    else:
        res_dict["numeric"] += 1

print((res_dict))
