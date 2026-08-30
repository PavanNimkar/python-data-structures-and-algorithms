class Dog:
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner


class Owner:
    def __init__(self, name, address, contact):
        self.name = name
        self.address = address
        self.contact = contact


owner = Owner("Pavan", "Subhash Nagar", "9960979677")

dog1 = Dog("Jack", "Pamelion", owner)
print(dog1.owner)
