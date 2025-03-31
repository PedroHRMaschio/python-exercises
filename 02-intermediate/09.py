# Write a Python program that prints the second largest value in a list.

# If the list is empty or only has one element, print None.


example_list = [
    [3, 1, 15, 10], # 10
    [1, 2, 3, 4],   # 3
    [1, 2],         # 1
    [1],            # None
    []              # None
]


def find_second_greatest(my_list):
    if len(my_list) < 2:
        print(None)
        return
    sorted_list = sorted(my_list)
    print(sorted_list[-2])


for example in example_list:
    find_second_greatest(example)
