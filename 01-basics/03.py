# Write a Python Program that prints the reversed version of a string.

# The program must preserve uppercase and lowercase letters.

# If the string is empty, print it intact.

word_list = ["Hello", "Wo", ""]

for word in word_list:
    reversed_word = "".join(reversed(word)) # also could use word[::-1]
    print(f'word: {word} | reversed word: {reversed_word}') 