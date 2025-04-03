# Write a Python program that prints the smallest value in a dictionary.

# If the dictionary is empty, print None.

# You may assume that the values are numeric.


example_list = [
    {"a": 2, "b": 7, "c": 10},  # 2
    {"a": 0, "b": 7, "c": -1},  # -1
    {}                          # None
]


def get_smallest_number(my_dict):
    if my_dict:
        smallest_num = min(set(my_dict.values()))
        print(smallest_num)
    else:
        print(None)


for example in example_list:
    get_smallest_number(example)