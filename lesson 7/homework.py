class Car:
    def __init__(self, model, year, brand, volume, color, price):
        self.model = model
        self.year = year
        self.brand = brand
        self.volume = volume
        self.color = color
        self.price = price

    def show_car(self):
        print(f"Car(\n model={self.model},\n year={self.year},\n brand={self.brand},\n volume={self.volume},\n color={self.color},\n price={self.price})")

car_1 = Car(
    model="Corolla",
    year=2021,
    brand="Toyota",
    volume=1.6,
    color="Gray",
    price=19000
)
car_1.show_car()
