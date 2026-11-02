import requests

BASE_URL = "https://crudcrud.com/api/d76075a31c5041c48a7cf5b05381f508/products"

TIMEOUT = 15000

product_data = {"name": "Laptop", "price": 2500, "in_stock": True}

created_product_id = None

try:
    response = requests.post(BASE_URL, json=product_data, timeout=TIMEOUT)
    response.raise_for_status()
    created_product = response.json()
    created_product_id = created_product.get("_id")

    print("პროდუქტი წარმატებით დაემატა!")
    print(f"სერვერის პასუხი: {created_product}\n")
except requests.exceptions.RequestException as e:
    print(f"TASK 1 შეცდომა: {e}\n")


# დავალება 2

try:
    response = requests.get(BASE_URL, timeout=TIMEOUT)
    response.raise_for_status()
    products_list = response.json()

    print(f"სულ მოიძებნა {len(products_list)} პროდუქტი:")
    for idx, prod in enumerate(products_list, start=1):
        p_id = prod.get("_id")
        name = prod.get("name")
        price = prod.get("price")
        in_stock = prod.get("in_stock")
        print(f"  {idx}. [ID: {p_id}] {name} - {price} GEL (მარაგშია: {in_stock})")
    print()
except requests.exceptions.RequestException as e:
    print(f"TASK 2 შეცდომა: {e}\n")


# დავალება 3

try:
    if created_product_id:
        single_url = f"{BASE_URL}/{created_product_id}"
        response = requests.get(single_url, timeout=TIMEOUT)
        response.raise_for_status()
        single_product = response.json()

        print("მიღებულია კონკრეტული პროდუქტის მონაცემები:")
        print(f"  _id: {single_product.get('_id')}")
        print(f"  სახელი: {single_product.get('name')}")
        print(f"  ფასი: {single_product.get('price')}")
        print(f"  მარაგშია: {single_product.get('in_stock')}\n")
    else:
        print("TASK 3 გაუქმდა: _id ვერ მოიძებნა (წინა ეტაპზე პროდუქტი ვერ დაემატა).\n")
except requests.exceptions.RequestException as e:
    print(f"TASK 3 შეცდომა: {e}\n")


# დავალება 4

updated_data = {"name": "Gaming Laptop", "price": 3200, "in_stock": True}

try:
    if created_product_id:
        update_url = f"{BASE_URL}/{created_product_id}"
        response = requests.put(update_url, json=updated_data, timeout=TIMEOUT)
        response.raise_for_status()
        print(
            f"PUT მოთხოვნის სტატუს კოდი: {response.status_code} (წარმატებით განახლდა)"
        )

        verify_response = requests.get(update_url, timeout=TIMEOUT)
        verify_response.raise_for_status()
        print("განახლებული შედეგი სერვერიდან:")
        print(f"  {verify_response.json()}\n")
    else:
        print("TASK 4 გაუქმდა: _id ვერ მოიძებნა.\n")
except requests.exceptions.RequestException as e:
    print(f"TASK 4 შეცდომა: {e}\n")


# დავალება 5

try:
    if created_product_id:
        delete_url = f"{BASE_URL}/{created_product_id}"
        response = requests.delete(delete_url, timeout=TIMEOUT)
        response.raise_for_status()
        print(f"DELETE მოთხოვნის სტატუს კოდი: {response.status_code}")
        print(f"პროდუქტი ID-ით '{created_product_id}' წარმატებით წაიშალა სერვერიდან!\n")
    else:
        print("TASK 5 გაუქმდა: _id ვერ მოიძებნა.\n")
except requests.exceptions.RequestException as e:
    print(f"TASK 5 შეცდომა: {e}\n")
