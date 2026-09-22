age = int(input("Enter your age: "))

if age < 0:
    print("Invalid age entered.")
elif age < 5:
    print("Your ticket price is $0.")
elif 5 <= age <= 12:
    print("Your ticket price is $8.")
elif 13 <= age <= 64:
    print("Your ticket price is $15.")
else:
    print("Your ticket price is $10.")
