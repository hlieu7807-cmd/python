# Takes user input and converts it to lower case to handle 'yes', 'Yes', 'YES', etc.
user_response = input("Do you have your badge? (yes/no): ").strip().lower()

# Converts the string input into a true/false boolean
has_badge = (user_response == "yes")

if has_badge:
    print("Access granted. Welcome to the building!")
else:
    print("Access denied. The door is locked.")