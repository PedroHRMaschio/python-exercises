# Write a Python program that prints a list with the elements that listA and listB have in common.

# If they don't have any elements in common, print an empty list.

# The program should not assume that the lists have the same length.

# You may assume that each element will only appear once in each list.


example_list = [
    {"list_a": [1, 2, 3], "list_b": [1, 2, 3]}, # [1, 2, 3]
    {"list_a": [4, 5, 6], "list_b": [1, 4, 5]}, # [4, 5]
    {"list_a": [3, 4, 5], "list_b": [1, 2, 3]}, # [3]
    {"list_a": [4, 5, 6], "list_b": [1, 2, 3]}  # []
]


def find_common_elements(list_a, list_b):
    set_a = set(list_a)
    set_b = set(list_b)

    common_elements = set_a.intersection(set_b)
    print(list(common_elements))


for example in example_list:
    find_common_elements(example["list_a"], example["list_b"])

