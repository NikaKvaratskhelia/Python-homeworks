try:
    age_input = input("Enter your age: ")
    age = int(age_input)
    if age < 0:
        raise ValueError("Age cannot be negative!")
    if age < 18:
        raise ValueError("User must be at least 18 years old to register.")
except ValueError as e:
    print(e)
finally:
    print("Registration process completed.")
