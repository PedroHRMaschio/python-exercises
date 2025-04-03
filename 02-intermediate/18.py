# Write a Python program that prints the largest value in a dictionary.

# If the dictionary is empty, print None.

# You may assume that the values are numeric.


example_list = [
    {"a": 2, "b": 7, "c": 10},  # 10
    {"a": 0, "b": 7, "c": -1},  # 7
    {}                          # None
]


def get_largest_number(my_dict):
    if my_dict:
        largest_num = max(set(my_dict.values()))
        print(largest_num)
    else:
        print(None)


for example in example_list:
    get_largest_number(example)
