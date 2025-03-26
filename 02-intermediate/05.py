# Write a Python program that finds the intersection of two sets (set1 and set2).

# Create a new set called intersection with their intersection.

# Print the new set as the output.

# If the intersection is empty, print an empty set.

example_list = [
    {"set_1": {1, 2, 3}, "set_2": {4, 5, 6}},       # set()
    {"set_1": {1, 2, 3}, "set_2": {3, 4, 5}},       # {3}
    {"set_1": {1, 2, 3, 4}, "set_2": {3, 4, 5, 6}}, # {3, 4}
    {"set_1": {1, 2, 3, 4}, "set_2": {1, 2, 3, 4}}  # {1, 2, 3, 4}
]


def find_intersection(set_1, set_2):
    intersection = set_1.intersection(set_2)
    print(intersection)


for example in example_list:
    find_intersection(example["set_1"], example["set_2"])
