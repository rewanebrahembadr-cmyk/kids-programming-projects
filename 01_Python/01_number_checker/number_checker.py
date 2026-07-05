# Number Checker Project
# This project helps beginners practice input, conditions, and comparison operators.

number = int(input("Enter a number: "))

if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")
