# Write a Python program that merges two dictionaries and prints the resulting dictionary.

# "Merging" the dictionaries involves making a new dictionary with the key-value pairs in both dictionaries.


example = {
    "dict_1": {"a": 2, "b": 7, "c": 15},
    "dict_2": {"c": 4, "d": 23, "e": 1}
}                                           # {'a': 2, 'b': 7, 'c': 4, 'd': 23, 'e': 1}


def merge_dicts(dict_1, dict_2):
    merged_dict = dict_1 | dict_2
    print(merged_dict)

merge_dicts(example["dict_1"], example["dict_2"])

