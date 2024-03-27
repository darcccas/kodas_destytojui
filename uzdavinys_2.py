numbers = []
count = 10
while count > 0:
    count -= 1
    number = int(input("iveskite skaiciu: "))
    numbers.append(number)

print(sum(numbers) / len(numbers))
