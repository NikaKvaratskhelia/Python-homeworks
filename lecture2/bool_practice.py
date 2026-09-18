
users_number = int(input("Enter a number: "))


if users_number % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

if users_number > 0:
    print("The number is positive")
elif users_number < 0:
    print("The number is negative")
else: 
    print("The number is zero")