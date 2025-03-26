# Write a Python program that counts the number of elements in a list with value greater than 3.

# You may assume that the list only contains numbers.

# Print the final count.

example_list = [
    [1, -1, 0, 2, 2, 3],    # 0
    [1, 2, 3, 4],           # 1
    [7, 8, 9, 10],          # 4
    []                      # 0
]

GT_NUMBER = 3


def verify_gt_number(my_list):
    number_counter = 0

    for elem in my_list:
        if elem > GT_NUMBER:
            number_counter += 1
    
    print(number_counter)


def verify_gt_number2(my_list):
    number_counter = sum(1 for elem in my_list if elem > 3)

    print(number_counter)


for example in example_list:
    verify_gt_number(example)
