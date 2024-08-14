
"""Task 1: Input Length Validator Write a script that asks for and checks the length of the user's
first name and last name. Both should be at least 2 characters long. If not, print an error message."""

first_name = (input("What is your first name? "))
last_name = (input("What is your last name?"))
first_name_len = len(first_name)
last_name_len = len(last_name)

if first_name_len < 2:
    print("First name should be two characters long")
else:
    print("First name is correct")

if last_name_len < 2:
    print("Last name should be two characters long")
else:
    print("Last name is correct")

