"""
Deletes all even-numbered occurrences of a given list its indices.
"""

import random


def populate(lst):
    "Populates a given list with random numbers"
    for _ in range(random.randint(5, 10)*2):
        lst.append(random.randint(5, 10))
    print(lst, "< Populated list")


def count_occurrences(lst):
    "Counts the amount of time each number appears in the list"
    dictionary = {}
    for i in range(len(lst)):
        if lst[i] in dictionary:
            dictionary[lst[i]] += 1
        else:
            dictionary[lst[i]] = 1
    return dictionary


def delete_occurrences(lst):
    "Deletes even occurrences from a given list"
    dictionary = count_occurrences(lst)
    print(dictionary, "< Occurences")

    evens = [i for i in dictionary if dictionary[i] % 2 == 0]
    print(evens, "< To remove from list")

    index = 0
    end = len(lst)

    while index < end:
        if lst[index] in evens:
            del lst[index]
            end -= 1
        else:
            index += 1

    return lst


some_list = []
populate(some_list)
delete_occurrences(some_list)

print(some_list, "< New list")
