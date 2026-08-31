class Vehicle:
    # note python only supports method overridding polymor not method overloading i.e. same method diff args of diff types
    def __int__(self, brand, model, year):
        # common attributes for all vehicles
        self.brand = brand
        self.model = model
        self.year = year

    def start(self):
        print("starting vechile")

    def stop(self):
        print("Vechile has stopped")


class Car(Vehicle):
    def __init__(self, brand, model, year):
        super().__int__(brand, model, year)

    # customized inherited start and stop method for Car class
    def start(self):
        print(f"{self.brand} has started")

    def stop(self):
        print(f"{self.brand} has stopped")


class Bike(Vehicle):
    def __init__(self, brand, model, year):
        super().__int__(brand, model, year)

    # customized inherited start and stop method for Bike class
    def start(self):
        print(f"{self.brand} has started")

    def stop(self):
        print(f"{self.brand} has stopped")


bike1 = Bike("Honda", "Splendor", 2024)
car = Car("Toyota", "Fortuner", 2026)

vehicles: list[Vehicle] = [bike1, car]

for vehilce in vehicles:
    # note python choose which method to call based on clasess of the objects
    vehilce.start()
    vehilce.stop()
