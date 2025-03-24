# Write a Python program that reverses the individual words in the string s and changes their capitalization.

# Uppercase letters should be printed in lowercase and vice versa.

# Assume that the string only contains letters and spaces are used to separate words.

example_list = [
    "Hello World",          # OLLEh DLROw
    "Python is Awesome",    # NOHTYp SI EMOSEWa
    "Hello, I am 20"        # ,OLLEh i MA 02
]


def reverse_all(s):
    new_s = ""
    word_list = s.split(" ")
    for word in word_list:
        reversed_word = "".join(reversed(word))
        swapped_case_word = reversed_word.swapcase()
        new_s += swapped_case_word + " "
    new_s.rstrip()
    print(new_s)


for example in example_list:
    reverse_all(example)
