# Write a Python program that counts the frequency of each value in a dictionary.

# The program should create a new dictionary to map each value in the original dictionary to its frequency (how many times it occurs).

# If the dictionary is empty, print an empty dictionary.


example_list = [
    {"a": 4, "b": 4, "c": 2, "d": 7, "e": 4, "f": 2, "g": 7, "h": 7},   # {4: 3, 2: 2, 7: 3}
    {4: 3, 2: 2, 7: 3}                                                  # {3: 2, 2: 1}
]


def find_frequency_of_each_element(my_dict):
    freq_dict = dict()

    for elem in my_dict:
        if not freq_dict.get(my_dict[elem]):
            freq_dict[my_dict[elem]] = 1
        else:
            freq_dict[my_dict[elem]] += 1
    
    print(freq_dict)


for example in example_list:
    find_frequency_of_each_element(example)

