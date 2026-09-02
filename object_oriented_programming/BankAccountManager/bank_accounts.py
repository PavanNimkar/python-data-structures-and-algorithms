class BalanceException(Exception):
    """Raised when an account does not have enough funds."""


class BankAccount:
    def __init__(self, initial_amount, account_name) -> None:
        self._funds = initial_amount
        self.name = account_name

        print(f"\nAccount '{self.name}' created." f"\nAccount Balance: ₹{self._funds}")

    @property
    def balance(self):
        """Return the current account balance."""
        print(f"\nAccount '{self.name}' has \nAccount Balance of ₹{self._funds}")

    def deposit(self, amount):
        self._funds += amount
        print(f"₹{amount} deposited into {self.name}'s account.")

    def viable_transaction(self, amount):
        """Check whether the account has enough money."""
        if self._funds >= amount:
            return

        raise BalanceException("Sorry, account has insufficient balance.")

    def withdraw(self, amount):
        try:
            self.viable_transaction(amount)
            self._funds -= amount

            print(f"₹{amount} withdrawn from {self.name}'s account.")

        except BalanceException as e:
            print(f"Withdrawal interrupted: {e}")

    def transfer(self, amount, account):
        try:
            self.viable_transaction(amount)

            self._funds -= amount
            account.deposit(amount)

            print(f"₹{amount} transferred from " f"{self.name} to {account.name}.")

        except BalanceException as e:
            print(f"Transfer failed: {e}")


class InterestRewardsAcc(BankAccount):

    def deposit(self, amount):
        self._funds += amount * 1.05

        print(f"₹{amount} deposited with 5% reward.")


class SavingsAcc(InterestRewardsAcc):

    def __init__(self, initial_amount, account_name) -> None:
        super().__init__(initial_amount, account_name)
        self.fee = 5

    def withdraw(self, amount):
        try:
            self.viable_transaction(amount + self.fee)

            self._funds -= amount + self.fee

            print(
                f"₹{amount} withdrawn from {self.name}."
                f" ₹{self.fee} transaction fee charged."
            )

        except BalanceException as e:
            print(f"Withdrawal stopped: {e}")
