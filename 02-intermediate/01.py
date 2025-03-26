# Write a Python program that prints the elements of a list followed their corresponding indices.

# Each element and its index must be on the same line separated by a space.

# If the list is empty, print "Empty List".


example_list = [
    [1, 2, 3, 4],       # e: 1 i: 0, e: 2 i: 1, e:3 i:2, e:4 i:3
    ["a", "b", "c"],    # e: a i: 0, e: b i: 1, e:c i:2
    []                  # Empty List
]

def print_elem_and_index(my_list):
    if not my_list:
        print("Empty List")
        return
    for i, elem in enumerate(my_list):
        print(f"e: {elem} i: {i}")


for example in example_list:
    print_elem_and_index(example)
