# Write a Python program that removes duplicate elements from a list, only keeping one occurrence of each element in the list.

# The original list should not be mutated (modified).

# The program must print the final version of the list.

example_list = [
    [1, 1, 2, 3, 4, 4],     # [1, 2, 3, 4]
    ["a", "a", "b", "a"],   # ['b', 'a']
    [1, 2, 3],              # [1, 2, 3]
    []                      # []
]

def remove_duplicated_items(my_list):
    new_list = list(set(my_list))
    print(new_list)

def remove_duplicated_items2(my_list):
    for elem in my_list:
        for _ in range(my_list.count(elem)-1):
            my_list.remove(elem)
    print(my_list)


for example in example_list:
    remove_duplicated_items(example)
