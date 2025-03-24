# Write a Python program that prints a version of the string s with all commas replaced by dots.

example_list = ["Hello, World!", "3,456,344"]

COMMA = ","
DOT = "."

for example in example_list:
    print(example.replace(COMMA, DOT))
