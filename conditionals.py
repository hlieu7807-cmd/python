# 1. Create a variable to hold the number of bananas (Instruction 4)
# We use int(input()) so the user can type the number in the console
bananas = int(input("How many bananas do you have? "))

# 2. Set up the conditionals using if, elif, and else (Instruction 2 & 3)
if bananas >= 5:
    print("I have a bunch of bananas.")

elif 1 <= bananas <= 4:
    print("I have a small bunch of bananas.")

else:
    print("I have no bananas.")