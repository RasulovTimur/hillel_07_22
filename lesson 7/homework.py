class Car:
    def __init__(self, model, year, brand, volume, color, price):
        self.model = model
        self.year = year
        self.brand = brand
        self.volume = volume
        self.color = color
        self.price = price


    def show_car(self):
        print(f"Car \n model: {self.model},\n year: {self.year},\n brand: {self.brand},\n volume: {self.volume},\n color: {self.color},\n price: {self.price}")
    def show_price(self):
        print(f"Car_price \n brand: {self.brand},\n model: {self.model},\n price: {self.price}")
car_toyota = Car(
    model="Corolla",
    year=2021,
    brand="Toyota",
    volume=1.6,
    color="Gray",
    price=19000
)
car_mazda = Car(
    model=6,
    year=2016,
    brand="Mazda",
    volume=2.0,
    color="Black",
    price=16000
)
car_toyota.show_car()
car_mazda.show_price()

class Book:
    def __init__(self, name, year, publishing_house, genre, author, price):
        self.name = name
        self.year = year
        self.publishing_house = publishing_house
        self.genre = genre
        self.author = author
        self.price = price


    def show_book(self):
        print(f"Book \n name: {self.name},\n year: {self.year},\n publishing_house: {self.publishing_house},\n genre: {self.genre},\n author: {self.author},\n price: {self.price}")
    def show_info(self):
        print(f"Book_info \n author: {self.author},\n name: {self.name},\n genre: {self.genre}")
Book_1 = Book(
    name="Кобза́рь",
    year=1840,
    publishing_house="Школа (Харьков)",
    genre="Поэзия",
    author="Тарас Шевченко",
    price=300
)
Book_2 = Book(
    name="Скотный двор",
    year=1945,
    publishing_house="АСТ",
    genre="Притча, сатира, антиутопия",
    author="Джордж Оруэлл",
    price=500
)
Book_1.show_book()
Book_2.show_info()

class Stadium:
    def __init__(self, name, opening_date, country, city, capacity):
        self.name = name
        self.opening_date = opening_date
        self.country = country
        self.city = city
        self.capacity = capacity


    def show_stadium(self):
        print(f"Stadium \n name: {self.name},\n opening_date: {self.opening_date},\n country: {self.country},\n city: {self.city},\n capacity: {self.capacity}")
    def show_info(self):
        print(f"Stadium_info \n name: {self.name},\n country: {self.country},\n capacity: {self.capacity}")
dnepr_arena = Stadium(
    name="Днепр Арена",
    opening_date=2008,
    country="Украина",
    city="Днепр",
    capacity=31000,
)
marakana = Stadium(
    name="Маракана́",
    opening_date=1950,
    country="Бразилия",
    city="Рио-де-Жанейро",
    capacity=199854,
)
dnepr_arena.show_stadium()
marakana.show_info()