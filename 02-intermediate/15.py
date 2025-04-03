# Write a Python program that adds a new key-value pair to a dictionary only if the key doesn't exist already.

# If the key-value pair exists in the dictionary, do not update the existing value.

# The dictionary should not be modified in this case.

# Store the new key in the new_key variable and the new value in the new_value variable.

# Print the final value of the dictionary.


example_list = [
    {
        "dict": {"a": 2, "b": 7},
        "data_to_insert": {"c": 5}
    },                                      # {'a': 2, 'b': 7, 'c': 5}
    {
        "dict": {"a": 2, "b": 7, "c": 5},
        "data_to_insert": {"a": 6}
    }                                       # {'a': 2, 'b': 7, 'c': 5}
]


def insert_data_on_dict(my_dict, data_to_insert):
    for key in data_to_insert:
        if key not in my_dict:
            my_dict[key] = data_to_insert[key]
    
    print(my_dict)


for example in example_list:
    insert_data_on_dict(example["dict"], example["data_to_insert"])

