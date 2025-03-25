# Write a Python program that prints the elements of a list on the same line.

# The elements should be separated only by a space (not by a comma).

# The output should not include the opening and closing square brackets [ ].


example_list = [
    ["a", "b", "c"],    # a b c
    [3, 4, 5, 6]        # 3 4 5 6
]


def print_list(my_list):
    print(" ".join(map(str, my_list)))


def print_list2(my_list):
    print(*my_list, sep= " ")


for example in example_list:
    print_list(example)
