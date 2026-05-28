def userinfo():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    age = int(input("Enter your age: "))
    return f"{first_name} {last_name} is {age} years old."

print(userinfo())

a = 3
b = 4
c = 5
def demo():
    y = a + b + c
    print(f"The sum of a, b, and c is: {y}")
demo()