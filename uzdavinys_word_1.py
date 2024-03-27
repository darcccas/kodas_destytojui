word_name = ["asdfrwe", "sdfukas", "fghstis"]

result = ""
for name in word_name:
    for index in range(len(name)):

        if name[index] == word_name[1][index] and name[index] == word_name[2][index]:
            result += name[index]

    print(result)
    break
