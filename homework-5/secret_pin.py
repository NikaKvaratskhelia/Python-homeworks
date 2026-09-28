CORRECT_PIN = "1234"
MAX_ATTEMPTS = 3

attempts = MAX_ATTEMPTS

while attempts > 0:
    user_pin = input("Enter 4-digit PIN: ")
    
    if user_pin == CORRECT_PIN:
        print("Access granted!")
        break
    
    attempts -= 1
    if attempts > 0:
        print(f"Incorrect PIN. Remaining attempts: {attempts}")
    else:
        print("Card blocked!")
