# Write a Python program that prints the character at index i in the string s.

# If the index is out of range, the program should print "i out of range"

# If the string is empty, the program should print "Empty String"

word_list = [
    {"word": "Hello", "i": 2},
    {"word": "Pizza", "i": 4},
    {"word": "", "i": 3},
    {"word": "World", "i": 15}
]

for example in word_list:
    print(f'Word: "{example["word"]}" | i: {example["i"]}')
    if len(example["word"]) == 0:
        print("This is an empty string.")
    elif example["i"] > len(example["word"]):
        print("i out of range")
    else:
        print(example["word"][example["i"]])
