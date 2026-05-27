# Takes user input for age
age = int(input("Enter the person's age: "))

if age > 18:
    print("Consider them to be an adult.")
elif 13 <= age <= 18:
    print("Consider them to be a teen.")
else:
    print("Consider them to be a child.")