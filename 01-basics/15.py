# Write a Python program to count the number of repeated characters in the string s.

# The program must print the total number of repeated characters and a message on the next line displaying the repeated characters separated by a space and sorted alphabetically.

# If there are no repeated characters in the string, print 0 as the total count and None on the next line.

example_list = [
    "Hello",        # 1 l
    "Corporation",  # 2 o r
    "Python"        # 0 None
]


def count_repeted_chars(word):
    repeated_count = 0
    repeated_chars = []

    for char in word:
        if (word.count(char) > 1) and (char not in repeated_chars):
            repeated_count += 1
            repeated_chars.append(char)

    if repeated_chars:
        print(repeated_count, *sorted(repeated_chars), sep=" ")
    else:
        print(0, None)


for example in example_list:
    count_repeted_chars(example)
