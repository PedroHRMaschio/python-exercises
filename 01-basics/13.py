# Write a Python program that checks if the string s ends with a specific sequence of characters denoted by the variable suffix.

# If it does, print True. Else, print False.

# This test should be case sensitive. Therefore, "A" should not be equivalent to "a".

# If the length of the suffix is greater than the length of the string, print False.

example_list = [
    {"word": "Hello", "suffix": "ello"},    # True
    {"word": "Coding", "suffix": "eng"},    # False
    {"word": "Pedro", "suffix": "rowing"}   # False
]


def check_suffix(word, suffix):
    print(word.endswith(suffix))


for example in example_list:
    check_suffix(example["word"], example["suffix"])
