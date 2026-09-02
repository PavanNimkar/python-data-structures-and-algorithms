class Transaction:
    def __init__(self, title, amount, type, note="") -> None:
        self.title = title
        self.amount = amount
        self.type = type
        self.note = note

    def display_info(self):
        return f"\nTransaction: {self.title} | Amount (₹): {self.amount} | Type: {self.type} | Note: {self.note}"


class Bank:
    def __init__(self) -> None:
        self.wallet = []

    def add_transaction(self, transaction):
        self.wallet.append(transaction)

    def remove_transaction(self, title):
        for trans in self.wallet:
            if trans.title == title:
                self.wallet.remove(trans)
                return f"{title} removed"
        return f"{title} not found..."

    def display_transaction_info(self):
        if not self.wallet:
            return "No transactions present in wallet"
        return "\n".join([transaction.display_info() for transaction in self.wallet])

    def search_transaction(self, query):
        clean_query = query.lower()
        found = [
            trans
            for trans in self.wallet
            if clean_query in trans.title.lower()
            or clean_query in trans.type.lower()
            or clean_query in trans.note.lower()
        ]

        return found


def main():

    bankManager = Bank()

    while True:
        print("\n" + "═" * 58)
        print("           📦 BANK  MANAGER")
        print("═" * 58)
        print(" 1. ➕ Add Transaction")
        print(" 2. 📋 View Transactions")
        print(" 3. 🔍 Search Transactions")
        print(" 4. 🗑 Delete Transaction")
        print(" 5. 🚪 Exit")
        print("─" * 58)

        try:
            choice = int(input("Enter your choice (1-5): "))
        except ValueError:
            print("\n❌ Please enter a valid number.")
            continue

        match choice:

            case 1:
                # Add transactions
                print("\n" + "─" * 58)
                print("               ➕ ADD NEW TRANSACTION")
                print("─" * 58)

                title = input("Title : ")
                amount = float(input("Amount (₹): "))
                type = input("Type    : ")
                note = input("Note     : ")

                transaction = Transaction(title, amount, type, note)
                bankManager.add_transaction(transaction)
                print("\n✅ Transaction added successfully!")

            case 2:
                # Display transactions
                print("Your Transactions: ")
                result = bankManager.display_transaction_info()
                print(result)

            case 3:
                # Search transactions
                print("\n" + "─" * 58)
                print("              🔍 SEARCH TRANSACTIONS")
                print("─" * 58)

                query = input("Search for transaction title or note or type : ")
                result = bankManager.search_transaction(query)

                if not result:
                    print(f"No transactions found with query '{query}'")
                print(f"\nDisplaying transactions with query '{query}':")
                for trans in result:
                    print(trans.display_info())

            case 4:
                # Remove transactions
                result = bankManager.display_transaction_info()
                print(result)
                if result:
                    title = input("Enter the title of transaction to delete: ")
                    result = bankManager.remove_transaction(title)
                    print(result)

            case 5:
                # Exit
                print("\n" + "═" * 58)
                print("        Thank you for using our Bank System")
                print("═" * 58)
                break

            case _:
                print("\n❌ Please choose a number between 1 and 5.")


if __name__ == "__main__":
    main()
