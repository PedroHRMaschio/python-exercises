# Write a Python program that creates and print a dictionary

# that maps each element in a list to its corresponding frequency (how many times it occurs in the list).

# The test should be case-sensitive. Therefore, "A" should not be considered the same element as "a".


example_list = [
    ["a", "a", "b", "c", "a", "b"], # {'a': 3, 'b': 2, 'c': 1}
    [1, 2, 3, 4, 3, 2, 1, 2]        # {1: 2, 2: 3, 3: 2, 4: 1}
]


def find_how_many_reps(my_list):
    rep_dict = dict()
    for elem in my_list:
        if elem in rep_dict:
            rep_dict[elem] += 1
        else:
            rep_dict[elem] = 1
    print(rep_dict)


for example in example_list:
    find_how_many_reps(example)

