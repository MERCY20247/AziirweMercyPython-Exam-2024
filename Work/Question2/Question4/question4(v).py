class Car:
    def __init__(self, brand,name, color):
        self.brand = brand
        self.name = name
        self.color = color
    def start_engine(self):
        print(f"The engine of the {self.brand} car has started.")
my_car = Car("Nissan","RangeRover" "red")
my_car.start_engine()
