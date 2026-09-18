from datetime import date

users_birthyear = int(input("Enter your birth year: "))

print("Your are ", date.today().year - users_birthyear, "years old.")