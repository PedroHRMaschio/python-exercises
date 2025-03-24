# Write a Python program that prints a copy of the string s without any spaces.

# Words should be connected in the final string.

# If the string doesn't contain spaces, print it intact.

s_list = [
    "Hello, World!",    # Hello,World!
    "Have a great day", # Haveagreatday
    "Python"            # Python
]

for s in s_list:
    print(s.replace(" ", ""))
