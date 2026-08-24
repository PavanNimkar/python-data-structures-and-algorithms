all_expenses = []

total_expense = 0


def view_history(all_expenses):
    print("\n" + "=" * 50)
    print("             EXPENSE HISTORY")
    print("=" * 50)

    if len(all_expenses) == 0:
        print("\nNo expenses found.\n")
        return

    for expense in range(len(all_expenses)):
        print("\n" + "*" * 40)
        print(f"         EXPENSE ID : {expense}")
        print("*" * 40)
        print(f" Amount   : ₹{all_expenses[expense]['amount']}")
        print(f" Date     : {all_expenses[expense]['date']}")
        print(f" Category : {all_expenses[expense]['category']}")
        print(f" Details  : {all_expenses[expense]['details']}")
        print("*" * 40)


try:
    while True:

        print("\n" + "=" * 50)
        print("         EXPENSE TRACKER")
        print("=" * 50)
        print("1. Add Expense")
        print("2. Delete Expense")
        print("3. View History")
        print("4. View Total Expense")
        print("5. Exit")
        print("-" * 50)

        user_choice = int(input("Choose your task (1-5): "))

        if user_choice == 1:
            print("\n" + "-" * 40)
            print("        ADD NEW EXPENSE")
            print("-" * 40)

            ex_amount = float(input("Enter amount    : ₹"))
            ex_date = input("Enter date      : ")
            ex_category = input("Enter category  : ")
            ex_details = input("Enter details   : ")

            expense = {
                "date": ex_date,
                "amount": ex_amount,
                "category": ex_category,
                "details": ex_details,
            }

            all_expenses.insert(0, expense)

            print("\nExpense added successfully!")
            print("-" * 40)

        elif user_choice == 2:
            view_history(all_expenses)

            ex_index = int(input("\nEnter Expense ID to delete: "))
            del all_expenses[ex_index]

            print("\nExpense deleted successfully!")

        elif user_choice == 3:
            view_history(all_expenses)

        elif user_choice == 4:
            for expense in all_expenses:
                total_expense = total_expense + expense["amount"]

            print("\n" + "=" * 50)
            print(f"   TOTAL EXPENSE : ₹{total_expense}")
            print("=" * 50)

        elif user_choice == 5:
            print("\n" + "=" * 50)
            print("   Thank you for using Expense Tracker!")
            print("=" * 50)
            break

        else:
            print("\nInvalid choice! Please enter 1 to 5.")

except KeyboardInterrupt:
    print("\n\n" + "=" * 50)
    print(" Program interrupted by user.")
    print(" Thank you for using Expense Tracker!")
    print("=" * 50)
