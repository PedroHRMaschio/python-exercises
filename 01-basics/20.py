# Write a Python program that checks if a list is empty or not.

# If the list is empty, print "Empty". Else, print "Not Empty".

example_list = [
    [],         # Empty
    [1, 2, 3],  # Not Empty
    [24]        # Not Empty
]


def empty_or_not(my_list):
    if my_list:
        print("Not Empty")
    else:
        print("Empty")


for example in example_list:
    empty_or_not(example)



