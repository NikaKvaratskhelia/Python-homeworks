user_input = input("Enter a string: ")
filtered_text = ""

for char in user_input:
    if char.isdigit():
        continue
    filtered_text += char

print(filtered_text)
