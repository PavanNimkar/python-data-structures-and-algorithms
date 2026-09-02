# Import all classes from bank_accounts.py.
#
# This gives us access to:
#
#     BankAccount
#     InterestRewardsAcc
#     SavingsAcc
#     BalanceException
#
from bank_accounts import *

# =========================================================
# CREATE BANK ACCOUNT OBJECTS
# =========================================================

# Creates a BankAccount object.
#
# Because an object is being created, Python automatically
# calls BankAccount.__init__().
Pavan = BankAccount(12000, "Pavan Nimkar")


# Creates another BankAccount object.
#
# This calls BankAccount.__init__() again.
Alex = BankAccount(10000, "Alex Patil")


# Creates an InterestRewardsAcc object.
#
# InterestRewardsAcc inherits from BankAccount.
#
# Its parent __init__() is called automatically through
# super().__init__() when the Savings/child class is created.
Rajesh = InterestRewardsAcc(80000, "Rajesh Choudhary")


# Creates a SavingsAcc object.
#
# SavingsAcc.__init__() is called.
#
# Inside it:
#
#     super().__init__()
#
# calls the parent BankAccount.__init__().
Sira = SavingsAcc(30000, "Sira")


# =========================================================
# INITIAL BALANCES
# =========================================================

print("\nInitial balance of each account")


# Because balance has @property:
#
#     Alex.balance
#
# automatically calls:
#
#     BankAccount.balance()
#
# It displays Alex's current balance.
Alex.balance


# Calls BankAccount.balance() for Pavan.
Pavan.balance


# Calls BankAccount.balance() for Rajesh.
#
# Rajesh inherits the balance property from BankAccount.
Rajesh.balance


# Calls BankAccount.balance() for Sira.
#
# SavingsAcc also inherits balance from BankAccount.
Sira.balance


# =========================================================
# TESTING BANKACCOUNT METHODS
# =========================================================

# Calls BankAccount.deposit().
#
# Pavan currently has ₹12,000.
#
# ₹2,000 is deposited.
#
# New balance:
#
# ₹12,000 + ₹2,000 = ₹14,000
Pavan.deposit(2000)


# Calls BankAccount.withdraw().
#
# Pavan currently has ₹14,000.
#
# ₹5,000 is withdrawn.
#
# New balance:
#
# ₹14,000 - ₹5,000 = ₹9,000
Pavan.withdraw(5000)


# Calls BankAccount.transfer().
#
# Pavan is the sender.
# Alex is the receiver.
#
# ₹1,000 is transferred.
#
# Pavan:
# ₹9,000 - ₹1,000 = ₹8,000
#
# Alex:
# ₹10,000 + ₹1,000 = ₹11,000
Pavan.transfer(1000, Alex)


# =========================================================
# TESTING INTEREST REWARDS ACCOUNT
# =========================================================

# Calls InterestRewardsAcc.deposit().
#
# IMPORTANT:
#
# InterestRewardsAcc overrides deposit().
#
# Therefore Python uses:
#
#     InterestRewardsAcc.deposit()
#
# instead of:
#
#     BankAccount.deposit()
#
# Rajesh has ₹80,000.
#
# Deposit = ₹1,000
# 5% reward = ₹50
#
# Total added = ₹1,050
#
# New balance = ₹81,050
Rajesh.deposit(1000)


# =========================================================
# TESTING SAVINGS ACCOUNT
# =========================================================

# Calls SavingsAcc.withdraw().
#
# IMPORTANT:
#
# SavingsAcc overrides withdraw().
#
# Therefore Python uses:
#
#     SavingsAcc.withdraw()
#
# instead of:
#
#     BankAccount.withdraw()
#
# Sira has ₹30,000.
#
# Withdrawal = ₹5,000
# Fee        = ₹5
#
# Total removed = ₹5,005
#
# New balance = ₹24,995
Sira.withdraw(5000)


# =========================================================
# TESTING EXCEPTIONS
# =========================================================

# Pavan currently has ₹8,000.
#
# We try to withdraw ₹600,000.
#
# viable_transaction() checks:
#
#     8000 >= 600000
#
# Result:
#
#     False
#
# Therefore:
#
#     raise BalanceException(...)
#
# is executed.
#
# The exception is caught by the except block inside
# withdraw(), so the program does NOT crash.
Pavan.withdraw(600000)


# Pavan still has only ₹8,000.
#
# We try to transfer ₹90,000.
#
# transfer() calls:
#
#     self.viable_transaction(90000)
#
# which checks:
#
#     8000 >= 90000
#
# Result = False
#
# Therefore BalanceException is raised.
#
# The exception is caught by transfer().
#
# No money is transferred.
Pavan.transfer(90000, Alex)


# =========================================================
# FINAL BALANCES
# =========================================================

print("\nBalance after transactions")


# Calls BankAccount.balance().
#
# Final Pavan balance:
# ₹12,000 + ₹2,000 - ₹5,000 - ₹1,000
# = ₹8,000
Pavan.balance


# Calls BankAccount.balance().
#
# Final Alex balance:
# ₹10,000 + ₹1,000
# = ₹11,000
Alex.balance


# Calls BankAccount.balance().
#
# Final Rajesh balance:
# ₹80,000 + ₹1,050
# = ₹81,050
Rajesh.balance


# Calls BankAccount.balance().
#
# Final Sira balance:
# ₹30,000 - ₹5,005
# = ₹24,995
Sira.balance
