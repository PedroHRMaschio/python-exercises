# Write a Python program that check if a string only contains numbers.

# If it does, print True. Else, print False.

s_list = [
    "Hello",    # False
    "4567",     # True
    "Hello59",  # False
    ""          # False
]

for s in s_list:
    print(s.isdecimal())
