class MovieTicket:
    cinema_name = "Rustaveli Cinema"
    total_tickets_sold = 0

    def __init__(self, movie_title: str, seat_number: str | int, price: float | int):
        self.movie_title = movie_title
        self.seat_number = seat_number
        self.price = price
        MovieTicket.total_tickets_sold += 1


ticket1 = MovieTicket("Dune: Part Two", "A-12", 18.0)
ticket2 = MovieTicket("Oppenheimer", "B-05", 20.0)
ticket3 = MovieTicket("Interstellar", "C-08", 15.0)

print(f"კინოთეატრი: {ticket1.cinema_name} | ფილმი: {ticket1.movie_title} | ადგილი: {ticket1.seat_number} | ფასი: {ticket1.price} GEL")
print(f"კინოთეატრი: {ticket2.cinema_name} | ფილმი: {ticket2.movie_title} | ადგილი: {ticket2.seat_number} | ფასი: {ticket2.price} GEL")
print(f"კინოთეატრი: {ticket3.cinema_name} | ფილმი: {ticket3.movie_title} | ადგილი: {ticket3.seat_number} | ფასი: {ticket3.price} GEL")

print(f"სულ გაყიდული ბილეთების რაოდენობა: {MovieTicket.total_tickets_sold}\n")

# davaleba 2

class User:
    status = "Active"

    def __init__(self, username: str, email: str, age: int):
        self.username = username
        self.email = email
        self.age = age

    def get_info(self) -> None:
        print(
            f"მომხმარებელი: {self.username} | "
            f"ელ. ფოსტა: {self.email} | "
            f"ასაკი: {self.age} | "
            f"სტატუსი: {self.status}"
        )


user1 = User("giorgi_b", "giorgi@example.com", 25)
user2 = User("nino_m", "nino@example.com", 22)

user1.get_info()
user2.get_info()

print(f"User 1 სტატუსი: {user1.status}")
print(f"User 2 სტატუსი: {user2.status}")
print(f"User კლასის საწყისი სტატუსი: {User.status}\n")

# davaleba 3

class Product:
    shop_name = "MegaShop"

    def __init__(self, name: str, price: float | int, stock: int):
        self.name = name
        self.price = price
        self.stock = stock

    def sell(self, quantity: int) -> None:
        if quantity <= self.stock:
            self.stock -= quantity
            print(f"გაიყიდა {quantity} ცალი {self.name}, დარჩა: {self.stock}")
        else:
            print(
                f"შეცდომა: მარაგში არ არის საკმარისი {self.name} "
                f"(მარაგშია: {self.stock}, მოთხოვნილია: {quantity})"
            )


laptop = Product("ლეპტოპი", 2500, 10)
print(f"მაღაზია: {laptop.shop_name} | პროდუქტი: {laptop.name} | საწყისი მარაგი: {laptop.stock}")

laptop.sell(2)
laptop.sell(5)
print(f"მიმდინარე stock ატრიბუტის მნიშვნელობა: {laptop.stock}")
laptop.sell(4) 
