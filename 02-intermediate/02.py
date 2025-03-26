# Write a Python program that removes all occurrences of the element elem_to_remove from a list.

# The output of the program should be the new list with the element removed.

# If the element is not found in the list, print the message "Not Found".

# If the list is empty, print "Empty List".

example_list = [
    {"list": [1, 2, 3, 4], "elem_remove": 2},           # [1, 3, 4]
    {"list": [3, 3, 2, 1], "elem_remove": 3},           # [2, 1]
    {"list": ["a", "b", "c", "b"], "elem_remove": "b"}, # ["a", "c"]
    {"list": [1, 2, 3, 4], "elem_remove": 7},           # Not Found
    {"list": [], "elem_remove": 0}                      # Empty List
]


def remove_elem_from_list(my_list, elem_remove):
    if not my_list:
        print("Empty List")
        return
    elif my_list.count(elem_remove) == 0:
        print("Not Found")
        return

    for _ in range (my_list.count(elem_remove)):
        my_list.remove(elem_remove)

    print(my_list)


for example in example_list:
    remove_elem_from_list(example["list"], example["elem_remove"])
