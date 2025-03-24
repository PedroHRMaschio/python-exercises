# Write a Python program that checks if the string s contains all the letters in the alphabet (case-insensitive, so "A" should be equivalent to "a").

# If it does, print True. Else, print False.

# Before comparing the characters, you should convert the string to lowercase.

# If the string contains spaces, ignore them before finding the result.

# You may assume that the string doesn't contain numbers or any other symbols, only spaces (possibly).

# Consider these letters as part of the alphabet: 'abcdefghijklmnopqrstuvwxyz'
from string import ascii_lowercase

example_list = [
    "abcdefghijklmnopqrstuvwxyz",                   # True
    "The quick brown fox jumps over the lazy dog",  # True
    "Hello"                                         # False
]

SPACE = " "

for example in example_list:
    set_example = set(example.lower())
    if SPACE in set_example:
        set_example.remove(SPACE)
    print(set(ascii_lowercase).issubset(set_example))

# Also could do this exarcise this way:

# for example in example_list:
#     is_pangram = True
#     for char in ascii_lowercase:
#         if char not in example.lower():
#             is_pangram = False
#             break
#     print(is_pangram)

