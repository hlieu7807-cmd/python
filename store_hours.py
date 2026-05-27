# Takes user input for the current hour (using 24-hour format)
current_hour = int(input("Enter the current hour (0-23): "))

opening_hour = 9
closing_hour = 18

if opening_hour <= current_hour < closing_hour:
    print("The store is open.")
else:
    print("The store is closed.")