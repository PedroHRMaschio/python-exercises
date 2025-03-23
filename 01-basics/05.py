# Write a Python program that prints the string s without the characters located at even indices.

# If the string is empty or only has one character, print it without any changes.

word_list = [
    "Coding",   # oig
    "Pizza",    # iz
    "Python",   # yhn
    "A",        # A
    ""          # 
]

for word in word_list:
    if len(word) < 2:
        print(f"word: {word} | output: {word}")
        continue
    print(f"word: {word} | output: {word[1::2]}")
