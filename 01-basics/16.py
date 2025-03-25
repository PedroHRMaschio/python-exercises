# Write a Python program to convert a string s to lowercase, sort the characters of each word in alphabetical order, and print the resulting string.

# You may assume that the string only contains letters and spaces to separate the words.

# Spaces should be preserved in the final string.

example_list = [
    "Hello World",      # ehllo dlorw
    "Wonderful World"   # deflnoruw dlorw
]

def sort_words_in_alphabetical_order(phrase):
    phrase = phrase.lower()
    new_phrase = ""
    for word in phrase.split(" "):
        new_phrase += f"{''.join(sorted(word))} "
    
    new_phrase.rstrip()
    print(new_phrase)


for example in example_list:
    sort_words_in_alphabetical_order(example)
