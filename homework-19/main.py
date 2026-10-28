cart = []

cart.append("რძე")
cart.append("პური")
cart.append("ყველი")
cart.append("ვაშლი")

print(f"კალათა პროდუქტების დამატების შემდეგ: {cart}")

removed_product = cart.pop()
print(f"ამოღებული პროდუქტი (LIFO): {removed_product}")

print(f"კალათის მიმდინარე მდგომარეობა: {cart}\n")


# davaleba 2

visitors = ["gio", "ნინო", "gio", "ანა", "ნიკა", "ანა"]
print(f"ვიზიტორების საწყისი სია: {visitors}")

unique_visitors = set(visitors)
print(f"უნიკალური ვიზიტორები (set): {unique_visitors}")

total_unique = len(unique_visitors)
print(f"სულ ეწვია {total_unique} უნიკალური მომხმარებელი.\n")


# davaleba 3

phonebook = {
    "გიორგი": "599-11-22-33",
    "ანა": "598-22-33-44",
    "ნიკა": "577-33-44-55",
    "მარიამი": "591-44-55-66",
}

print(f"ტელეფონის წიგნაკი: {phonebook}")

search_name = input("შეიყვანეთ სახელი ნომრის მოსაძებნად: ").strip()
result = phonebook.get(search_name, "ვერ მოიძებნა")
print(f"ძებნის შედეგი ({search_name}): {result}")
