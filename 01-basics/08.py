# Write a Python program that prints the string s with the character curr_char replaced by the character new_char.

# curr_char and new_char are variables that contain strings with a single character.

# You may assume that new_char will not be an empty string.

# The match must be case-sensitive (do not replace lowercase letters if curr_char is uppercase).

# If no match is found, print the initial string.

example_list = [
    {"word": "Hello", "curr_char": "l", "new_char": "s"},   # Hesso
    {"word": "World", "curr_char": "W", "new_char": "A"},   # Aord
    {"word": "Python", "curr_char": "P", "new_char": "x"},  # xython
    {"word": "Python", "curr_char": "p", "new_char": "a"}   # Python
]

for example in example_list:
    print(f'Word: "{example["word"]}" | curr_char: {example["curr_char"]} | new_char: {example["new_char"]}')
    new_word = ""
    for char in example["word"]:
        if char == example["curr_char"]:
            new_word+=example["new_char"]
        else:
            new_word+=char
    print(new_word)
    # Or could just use this code:
    # print(example["word"].replace(example["curr_char"], example["new_char"]))

