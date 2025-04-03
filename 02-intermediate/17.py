# Write a Python program that checks if all values in a dictionary are equal.

# If they are, print True. Else, print False.

# If the dictionary is empty, print "Empty".


example_list = [
    {"a": 2, "b":2, "c": 2, "d": 2, "e": 2},    # True
    {"a": 2, "b":2, "c": 2, "d": 7, "e": 2},    # False
    {"a": 2, "b":5, "c": 2, "d": 3, "e": 10},   # False
    {}                                          # Empty
]


def check_if_all_values_in_dict_are_equals(my_dict):
    num_unique_values = len(set(my_dict.values()))
    if num_unique_values == 0:
        print("Empty")
    elif num_unique_values == 1:
        print(True)
    else:
        print(False)


for example in example_list:
    check_if_all_values_in_dict_are_equals(example)
