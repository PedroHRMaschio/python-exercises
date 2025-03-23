# Write a Python program that prints the string s without the character at index n.

# If the index n is out of range, print the string s intact.

# If the string s is empty, print the string s intact.

word_list = [
    {"word": "Hello", "n": 1},  # Hllo
    {"word": "Pizza", "n": 3},  # Piza
    {"word": "Dog", "n": 15},   # Dog
    {"word": "", "n": 2}        # 
]

for example in word_list:
    print(f'Word: "{example["word"]}" | i: {example["n"]}')
    if (len(example["word"]) == 0) or (example["n"] >= len(example["word"])):
        print(example["word"])
        continue
    new_word = ""
    for i in range(len(example["word"])):
        if i != example["n"]:
            new_word += example["word"][i]
    print(new_word)
