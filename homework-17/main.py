class Employee:
    def __init__(self, name: str, salary: float | int):
        self.name = name
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        if value < 0:
            print("ხელფასი არ შეიძლება იყოს უარყოფითი!")
        else:
            self.__salary = value

    @salary.deleter
    def salary(self):
        del self.__salary
        print("ხელფასის მონაცემი წაიშალა.")


class Manager(Employee):
    def __init__(self, name: str, salary: float | int, department: str):
        super().__init__(name, salary)
        self.department = department

    def get_info(self):
        print(f"სახელი: {self.name}, განყოფილება: {self.department}, ხელფასი: {self.salary}")


manager = Manager("გიორგი ბერიძე", 5000, "IT")

try:
    print(manager.__salary)
except AttributeError as e:
    print(f"პირდაპირი წვდომა შეუძლებელია: {e}")

manager.get_info()

manager.salary = 5500
print(f"განახლებული ხელფასი: {manager.salary}")


# davaleba 2


class Payment:
    def process_payment(self, amount):
        print("მუშავდება გადახდა...")


class CreditCardPayment(Payment):
    def process_payment(self, amount):
        print(f"საბანკო ბარათით გადახდილია: {amount} ლარი")


class PayPalPayment(Payment):
    def process_payment(self, amount):
        print(f"PayPal-ით გადახდილია: {amount} ლარი")


card_payment = CreditCardPayment()
paypal_payment = PayPalPayment()

card_payment.process_payment(150)
paypal_payment.process_payment(80)

payments = [CreditCardPayment(), PayPalPayment()]
for payment in payments:
    payment.process_payment(250)


# davaleba 3

class SmartDevice:
    def __init__(self, brand: str):
        self.brand = brand
        self.__is_on = False

    @property
    def is_on(self):
        return self.__is_on

    def turn_on(self):
        self.__is_on = True

    def turn_off(self):
        self.__is_on = False


class SmartLight(SmartDevice):
    def __init__(self, brand: str, brightness: int = 100):
        super().__init__(brand)
        self.brightness = brightness

    def turn_on(self):
        super().turn_on()
        print(f"{self.brand}-ის ჭკვიანი სანათი ჩაირთო. სიკაშკაშე: {self.brightness}%")


light = SmartLight("Philips Hue", 80)

try:
    print(light.__is_on)
except AttributeError as e:
    print(f"პირდაპირი წვდომა შეუძლებელია: {e}")

print(f"ჩართვამდე: {light.is_on}")
light.turn_on()
print(f"ჩართვის მერე: {light.is_on}")

light.turn_off()
print(f"გამორთვის მერე: {light.is_on}")
