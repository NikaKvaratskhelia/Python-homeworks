import csv


def add_favorite_quote(filename: str = "quotes.txt") -> None:
    author = input("შეიყვანეთ თქვენი საყვარელი მწერალი: ").strip()
    quote = input("შეიყვანეთ ციტატა: ").strip()

    with open(filename, mode="a", encoding="utf-8") as file:
        file.write(f"ავტორი: {author}\nციტატა: {quote}\n\n")

    print(f"ინფორმაცია წარმატებით ჩაიწერა ფაილში: {filename}")


def read_quotes(filename: str = "quotes.txt") -> str:
    try:
        with open(filename, mode="r", encoding="utf-8") as file:
            content = file.read()
            print(content)
            return content
    except FileNotFoundError:
        print(f"ფაილი '{filename}' ვერ მოიძებნა.")
        return ""


add_favorite_quote()
read_quotes()


# davaleba 2


def get_survived_passengers(input_file: str = "titanic.csv") -> list[dict]:
    survived_passengers = []
    with open(input_file, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row.get("Survived") == "1":
                survived_passengers.append(row)

    return survived_passengers


def save_survived_passengers(
    passengers: list[dict] | None = None,
    output_file: str = "survived.csv",
    input_file: str = "titanic.csv",
) -> None:
    if passengers is None:
        passengers = get_survived_passengers(input_file)

    if not passengers:
        print("გადარჩენილი მგზავრების მონაცემები არ არის.")
        return

    fieldnames = list(passengers[0].keys())
    with open(output_file, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(passengers)

    print(f"გადარჩენილი მგზავრების ინფორმაცია წარმატებით ჩაიწერა '{output_file}'-ში.")


survived_passengers = get_survived_passengers()
save_survived_passengers(survived_passengers)
print(f"გადარჩენილი მგზავრების რაოდენობა: {len(survived_passengers)}")

# davaleba 3


def get_large_companies(
    input_file: str = "ssl_companies.csv", min_employees: int = 1000
) -> list[dict]:
    large_companies = []
    with open(input_file, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                emp_count = int(row.get("Number of employees", 0))
            except ValueError:
                emp_count = 0

            if emp_count > min_employees:
                large_companies.append(
                    {
                        "Name": row.get("Name"),
                        "Industry": row.get("Industry"),
                        "Number of employees": row.get("Number of employees"),
                    }
                )

    return large_companies


def save_sorted_companies(
    companies: list[dict] = None,
    output_file: str = "sorted_companies.csv",
    input_file: str = "ssl_companies.csv",
) -> None:
    if companies is None:
        companies = get_large_companies(input_file)

    if not companies:
        print("ჩასაწერი კომპანიების სია ცარიელია.")
        return

    fieldnames = ["Name", "Industry", "Number of employees"]
    with open(output_file, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(companies)

    print(f"კომპანიების ინფორმაცია წარმატებით ჩაიწერა '{output_file}'-ში.")


large_companies = get_large_companies()
save_sorted_companies(large_companies)
print(f"გადარჩეული კომპანიების რაოდენობა (>1000): {len(large_companies)}")
