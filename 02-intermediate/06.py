# Write a Python program that prints (as a list) the elements of listA that are not in listB.

# If the lists have the same elements, print an empty list.

# If listA is an empty list, print an empty list.

# Please assume that listB will be smaller or equals to listA (will have fewer elements).


example_list = [
    {"list_a": [1, 2, 3, 4], "list_b": [1, 2]},         # [3, 4]
    {"list_a": [1, 2, 3, 4], "list_b": [1, 2, 3]},      # [4]
    {"list_a": [1, 2, 3, 4], "list_b": [1, 2, 3, 4]},   # []
    {"list_a": [], "list_b": [1, 3]}                    # []
]


def find_the_difference(list_a, list_b):
    print([elem for elem in list_a if elem not in list_b])


for example in example_list:
    find_the_difference(example["list_a"], example["list_b"])
