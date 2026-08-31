class Vehicle:
    def __init__(self, brand, model, year, color) -> None:
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color

    def move(self):
        print(f"{self.brand} is moving")


class Car(Vehicle):
    def __init__(
        self, brand, model, year, color, number_of_doors, has_sunroof, has_ac
    ) -> None:
        # calling parents class init method using super keyword
        super().__init__(brand, model, year, color)
        self.number_of_doors = number_of_doors
        self.has_sunroof = has_sunroof
        self.has_ac = has_ac


car1 = Car("Ferarri", "N32", 2026, "red", 2, True, True)
print(car1.__dict__)
car1.move()
