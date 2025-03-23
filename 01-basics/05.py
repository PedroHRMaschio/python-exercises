# Write a Python program that prints the string s without the characters located at even indices.

# If the string is empty or only has one character, print it without any changes.

# "Coding" should return "oig"
# "Pizza" should return "iz"
# "Python" should return "yhn"

word_list = ["Coding", "Pizza", "Python", "A", ""]

for word in word_list:
    if len(word) < 2:
        print(f"word: {word} | output: {word}")
        continue
    print(f"word: {word} | output: {word[1::2]}")
