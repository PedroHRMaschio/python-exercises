# Write a Python program that prints the largest and smallest values in a list

# Print the two values on the same line, separated by a space.

# The largest value should appear first and the smallest value should appear second.

# You may assume that the list only contains numeric values.

# If the list is empty, print None.

example_List = [
    [3, 4, 5, 6],       # 6 3
    [-1, -2, -3, -4],   # -1 -4
    [0, 0, 0, 0],       # 0 0
    []                  # []
]


def print_max_and_min(my_list):
    if my_list:
        print(max(my_list), min(my_list))
    else:
        print(my_list)


for exmaple in example_List:
    print_max_and_min(exmaple)

