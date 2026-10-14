def even_numbers():
    num = 0
    while True:
        yield num
        num += 2


count = 0
for number in even_numbers():
    print(number)
    count += 1
    if count == 10:
        break


# davaleba 2

words = ["python", "generator", "yield", "code", "ai", "developer"]

filtered_words = (word.upper() for word in words if len(word) > 4)

for word in filtered_words:
    print(word)


# davaleba 3


def greeter_bot():
    response = "Enter your name"
    while True:
        name = yield response
        response = f"Hello, {name}!"


bot = greeter_bot()
print(next(bot))
print(bot.send("Alice"))
print(bot.send("Bob"))
