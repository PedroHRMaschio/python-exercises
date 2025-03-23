# Write a Python program that check if a string only contains numbers.

# If it does, print True. Else, print False.

s_list = ["Hello", "4567", "Hello59", ""]

for s in s_list:
    print(s.isdecimal())
