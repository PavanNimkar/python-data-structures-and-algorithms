# Encapsulation


# Note bad encapsule
class BadBankAccount:
    def __init__(self, balance):
        self.balance = balance


account = BadBankAccount(2000)
print(account.balance)
# NOTE we can modify or access the class artributes easily outside the class this is not encapsulation
account.balance = 3000
print(account.balance)


# Note Good Encapsulation
class BankAccount:
    def __init__(self, balance) -> None:
        self._balance = balance

    # NOTE an explict getter method to access the balance
    @property
    def balance(self):
        return self._balance

    # Note haven't used any setter method thus we can't set balance directly using object._balance = 4000 this will throw an error to deposit we used only deposit and for withdraw we use withdraw
    def deposit(self, ammount=0.0):
        # todo add logic for original behave
        self._balance += ammount

    def withdraw(self, ammount):
        # TODO add logic for original behave
        self._balance -= ammount


# Note we can't access/modify the balance outside class directly
account = BankAccount(3000)
# Note like this account.balance = 7000 as we haven't used setter method

account.deposit(89)
account.withdraw(70)
