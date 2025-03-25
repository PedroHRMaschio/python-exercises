# Write a Python program that multiplies all the items in a list by the value of the variable factor.

# The program must print the list as the output.

# The program should also allow multiplying the variable factor by a string in case the list contains strings.

# You may assume that the value of factor will be a positive integer.

example_list = [
    {"list": [3, 4, 5, 6], "factor": 2},    # [6, 8, 10, 12]
    {"list": ["a", "b", "c"], "factor": 3}  # ["aaa", "bbb", "ccc"]
]

def apply_factor_to_list(example_list, factor):
    for i in range(len(example_list)):
        example_list[i] *= factor
    print(example_list)


def apply_factor_to_list2(example_list, factor):
    new_list = example_list.copy()
    for i in range(len(example_list)):
        for _ in range(factor-1):
            new_list[i] += example_list[i]
    print(new_list)


for example in example_list:
    apply_factor_to_list(example["list"], example["factor"])
