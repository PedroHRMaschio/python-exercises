# Write a Python program that checks if the string s starts with the sequence of characters denoted by the variable prefix.

# If it does, print True. Else, print False.

# This test should be case sensitive. For example, "A" should not be equivalent to "a".

# If the length of the prefix is greater than the length of the string, print False.

example_list = [
    {"word": "Hello", "prefix": "He"},      # True
    {"word": "Coding", "prefix": "Con"},    # False
    {"word": "Pedro", "prefix": "Circum"}   # False
]


def check_prefix(word, prefix):
    print(word[:len(prefix)] == prefix)


def check_prefix2(word, prefix):
    starts_with_prefix = True
    for i in range(len(prefix)):
        if prefix[i] != word[i]:
            starts_with_prefix = False
            break
    print(starts_with_prefix)


def check_prefix3(word, prefix):
    print(word.startswith(prefix))


for example in example_list:
    check_prefix(example["word"], example["prefix"])
