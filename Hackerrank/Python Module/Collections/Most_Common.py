from collections import *

lowercase_letters_counter = Counter(input())

three_most_common_characters = []
def find_ith_most_common_character():
    most_common_character = ()
    for key, value in lowercase_letters_counter.items():
        if value == max(lowercase_letters_counter.values()):

            if len(most_common_character) == 0:
                most_common_character = (key, value)

            elif key < most_common_character[0]:
                most_common_character = (key, value)
    three_most_common_characters.append(most_common_character)
    del lowercase_letters_counter[most_common_character[0]]

for _ in range(3):
    find_ith_most_common_character()

for key, value in three_most_common_characters:
    print(key + " " + str(value))
