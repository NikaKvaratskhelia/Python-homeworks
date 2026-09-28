fruits = ["apple", "banana", "cherry", "orange"]

try:
    index_input = input("Enter index: ")
    index = int(index_input)
    print(f"Selected fruit: {fruits[index]}")
except ValueError:
    print("Invalid input! Please enter a whole number.")
except IndexError:
    print(f"Index out of bounds! Choose an index between 0 and {len(fruits)-1}.")
else:
    print("Successfully retrieved item!")
