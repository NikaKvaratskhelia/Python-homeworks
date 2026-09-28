inventory = ["apple", "banana", "orange", "apple", "kiwi", "apple"]
new_items = ["mango", "grape"]

apple_count = inventory.count("apple")
print(f"Number of 'apple' in inventory: {apple_count}")

orange_index = inventory.index("orange")
print(f"Index of first 'orange': {orange_index}")

inventory.extend(new_items)
print(f"Inventory after extend: {inventory}")

print(f"Reversed inventory: {inventory[::-1]}")
