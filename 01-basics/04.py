# Write a Python program that prints the first and last three characters of the string s as a single string.

# If the string has less than six characters, print an empty string (blank output).

word_list = [
    "Blue",         # 
    "Wonderful",    # Wonful
    "Amazing"       # Amaing
]
num_chars = 3

for word in word_list:
    if len(word) < (num_chars * 2):
        print(f"word: {word} | output: ")
        continue
    print(f"word: {word} | output: {word[:num_chars] + word[len(word)-num_chars:]}")
