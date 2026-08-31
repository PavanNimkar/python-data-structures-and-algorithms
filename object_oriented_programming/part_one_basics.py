"""
Python OOP - Day 01 + Day 02
Author: Pavan Nimkar

Concepts covered:
1. Classes & Objects
2. Constructors
3. Instance Attributes
4. Object Composition
5. Class (Static) Attributes
6. Static Methods
7. Encapsulation
8. Protected & Private Members
9. Getters and Setters
10. Property Decorator
"""

# ==========================================================
# 1. CLASS & OBJECT COMPOSITION
# ==========================================================


class Owner:
    """
    Owner class represents the dog's owner.
    """

    def __init__(self, name, address, contact):
        self.name = name
        self.address = address
        self.contact = contact


class Dog:
    """
    Dog class contains another object (Owner).
    This is called Object Composition (HAS-A relationship).
    """

    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner

    def display_info(self):
        print(f"Dog Name: {self.name}")
        print(f"Breed: {self.breed}")
        print(f"Owner     : {self.owner.name}")
        print(f"Address   : {self.owner.address}")
        print(f"Contact   : {self.owner.contact}")


# Create Owner object
owner1 = Owner(name="Pavan", address="Subhash Nagar", contact="9960979677")

# Pass owner object into Dog
dog1 = Dog("Jack", "Pomeranian", owner1)

print("=" * 50)
print("OBJECT COMPOSITION EXAMPLE")
print("=" * 50)
dog1.display_info()


# ==========================================================
# 2. ENCAPSULATION
# ==========================================================


class User:

    # ------------------------------------------------------
    # Class Attribute (Shared by all objects)
    # ------------------------------------------------------
    user_count = 0

    # ------------------------------------------------------
    # Static Method
    # Can be called without creating an object.
    # ------------------------------------------------------
    @staticmethod
    def get_user_count():
        return User.user_count

    # ------------------------------------------------------
    # Constructor
    # ------------------------------------------------------
    def __init__(self, username, email, password):

        # Public Instance Attribute
        self.username = username

        # Protected Attribute
        self._password = password

        # Email validation
        if "@" in email and ".com" in email:
            self._email = email
            print("\nEmail set successfully.")
        else:
            self._email = None
            print("\nInvalid Email!")

        # Private Attribute (Name Mangling)
        self.__confirm_email = email

        # Increase total users
        User.user_count += 1

    # ------------------------------------------------------
    # Getter Method
    # Used to access protected/private data safely.
    # ------------------------------------------------------
    def get_email(self):
        return self._email

    # ------------------------------------------------------
    # Setter Method
    # Used to update data with validation.
    # ------------------------------------------------------
    def set_email(self, new_email):
        if "@" in new_email and ".com" in new_email:
            self._email = new_email
            print("Email updated successfully.")
        else:
            print("Invalid Email!")

    # ------------------------------------------------------
    # Private Method
    # Can only be used inside the class.
    # ------------------------------------------------------
    def __log_user_data(self):
        print("\n--- Private User Data ---")
        print(f"Username : {self.username}")
        print(f"Password : {self._password}")
        print(f"Email    : {self._email}")

    # Public method to access private method
    def show_user_data(self):
        self.__log_user_data()

    # ------------------------------------------------------
    # Protected Method
    # Intended for subclasses.
    # ------------------------------------------------------
    def _get_confirm_email(self):
        return self.__confirm_email

    # ------------------------------------------------------
    # Property Decorator
    # Makes a method behave like an attribute.
    # ------------------------------------------------------
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, new_email):
        if "@" in new_email and ".com" in new_email:
            self._email = new_email
        else:
            print("Invalid Email!")


# ==========================================================
# 3. OBJECT CREATION
# ==========================================================

user1 = User(username="pavannimkar", email="pavan@gmail.com", password="pavan@123")

print("\n" + "=" * 50)
print("ENCAPSULATION EXAMPLE")
print("=" * 50)

# Public attribute
print("Username :", user1.username)

# Getter
print("Email (Getter):", user1.get_email())

# Setter
user1.set_email("newpavan@gmail.com")
print("Updated Email:", user1.get_email())

# Property Getter
print("Property Email:", user1.email)

# Property Setter
user1.email = "property@gmail.com"
print("After Property Setter:", user1.email)

# Protected method
print("Confirm Email:", user1._get_confirm_email())

# Private method cannot be called directly
# user1.__log_user_data()   ❌ AttributeError

# Correct way
user1.show_user_data()

# Static Method
print("\nTotal Users:", User.get_user_count())
