# Write a Python program that prints the second smallest value in a list.

# If the list is empty or only has one element, print None.


example_list = [
    [3, 1, 15, 10], # 3
    [1, 2, 3, 4],   # 2
    [1, 2],         # 2
    [1],            # None
    []              # None
]


def find_second_smallest(my_list):
    if len(my_list) < 2:
        print(None)
        return
    my_list.sort()
    print(my_list[1])


for example in example_list:
    find_second_smallest(example)
