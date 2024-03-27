import random

new_dict = {}

for key in range(10):
    new_dict[key + 1] = random.randint(1, 100)

print(new_dict)
