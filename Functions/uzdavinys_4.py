pin = "0045"

for number in range(10000):

    if str(number).zfill(4) == pin:
        print(f"Jusu PIN nulauztas ir yra {str(number).zfill(4)}")
        break
