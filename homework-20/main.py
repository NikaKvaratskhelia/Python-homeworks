from dataclasses import dataclass, asdict
import json


# davaleba 1


@dataclass
class Product:
    name: str
    price: float
    in_stock: bool


product1 = Product("Laptop", 2500.0, True)
product2 = Product("Mouse", 50.0, True)
product3 = Product("Keyboard", 120.0, False)

products = [product1, product2, product3]

for product in products:
    print(product)

print()


# davaleba 2

products_dict = [asdict(p) for p in products]

json_string = json.dumps(products_dict, indent=4)
print("სერიალიზებული JSON მონაცემები:")
print(json_string)

print()


# davaleba 3

json_data = '{"name": "Laptop", "price": 2500, "in_stock": true}'

parsed_data = json.loads(json_data)

restored_product = Product(**parsed_data)

print(f"ობიექტის ტიპი: {type(restored_product)}")
print(f"ობიექტი: {restored_product}")
print(f"name: {restored_product.name}")
print(f"price: {restored_product.price}")
print(f"in_stock: {restored_product.in_stock}")
