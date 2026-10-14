def sum_of_digits(n):
    if n == 0:
        return 0

    return (n % 10) + sum_of_digits(n // 10)


print(sum_of_digits(12345))

# davaleba 2

scores = [45, 82, 67, 38, 90, 55, 72]

passing_scores = list(filter(lambda x: x >= 50, scores))

final_scores = list(map(lambda x: min(x + 5, 100), passing_scores))

print("Passing scores:", passing_scores)
print("Final scores with bonus:", final_scores)

# davaleba 3

names = ["Laptop", "Phone", "Headphones", "Monitor"]
prices = [1200, 800, 150, 300]
ratings = [4.8, 4.5, 4.2, 4.9]


zipped = list(zip(names, prices, ratings))

sorted_by_price = sorted(zipped, key=lambda x: x[1], reverse=True)

print("Sorted by price (highest to lowest):")

for item in sorted_by_price:
    print(f"Product: {item[0]}, Price: {item[1]}, Rating: {item[2]}")

sorted_by_rating = sorted(zipped, key=lambda x: x[2])

print("Sorted by rating (lowest to highest):")
for item in sorted_by_rating:
    print(f"Product: {item[0]}, Price: {item[1]}, Rating: {item[2]}")
