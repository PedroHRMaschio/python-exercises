# Write a Python program that checks if a key exists in a dictionary or not.

# If the key exists in the dictionary, print True. Else, print False.

# The key should be stored in the variable key.


example_list = [
    {"dict": {"a": 4, "b": 6}, "key": "a"}, # True
    {"dict": {"a": 4, "b": 6}, "key": "p"}, # False
    {"dict": {}, "key": "d"}                # False
]


def find_key_on_dict(my_dict, key):
    print(key in my_dict)


for example in example_list:
    find_key_on_dict(example["dict"], example["key"])
