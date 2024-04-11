# Exercise 1:	Write a Python program to find the most common elements and their counts in a specified text.
# Original string: lkseropewdssafsdfafkpwe
# Most common three characters of the said string:
# [('s', 4), ('e', 3), ('f', 3)]

def find_most_common(letters: str) -> list:
    list = [(letters.count(letter), letter) for letter in set(letters)]
    return sorted(list, reverse=True)[:3]


print(find_most_common("lkseropewdssafsdfafkpwe"))


# Exercise 2: Create a list by picking an odd-index items from the first list and even index items from the second
# Given two lists, l1 and l2, write a program to create a third list l3 by picking an odd-index element from the list l1 and even index elements from the list l2.
def merge_list(first: list, second: list) -> list:
    return [number for index, number in enumerate(first) if index % 2 != 0] + [number for index, number in
                                                                               enumerate(second) if index % 2 == 0]


def merge_list2(first: list, second: list) -> list:
    return first[1::2] + second[::2]


l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]

print((merge_list2(l1, l2)))


# Exercise 3: Create a Python set such that it shows the element from both lists in a pair
# Given:

def merge_to_set(first: list, second: list) -> set:
    return set([(i, second[index]) for index, i in enumerate(first)])


first_list = [2, 3, 4, 5, 6, 7, 8]
second_list = [4, 9, 16, 25, 36, 49, 64]

print(set(zip(first_list, second_list)))

print(merge_to_set(first_list, second_list))

"""
Exercise 4: Iterate a given list and check if a given element exists as a key’s value in a dictionary. If not, delete it from the list
Given:
"""


def delete_value(numbers: list, data: dict) -> list:
    return [number for number in data.values() if number in numbers]


roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
sample_dict = {'Jhon': 47, 'Emma': 69, 'Kelly': 76, 'Jason': 97}

print((delete_value(roll_number, sample_dict)))


# Exercise 5: Get all values from the dictionary and add them to a list but don’t add duplicates
# Given:
def unic_values(library: dict) -> list:
    return list(library.fromkeys([number for number in library.values()]))


speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54}

print(unic_values(speed))

print(list(speed.values()))
