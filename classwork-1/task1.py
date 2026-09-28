try:
    birth_year = int(input("Enter your birth year: "))
    age = 2026 - birth_year
    print(f"Your age: {age}")
except ValueError:
    print("Please enter only digits!")
