import csv
import uuid


class InventoryItem:
    def __init__(self, item_id, name, quantity, price, sku=None):
        self.item_id = item_id
        self.name = name
        self.quantity = quantity
        self.price = price
        self.sku = sku if sku else str(uuid.uuid4())

    def display_info(self):
        print("┌──────────────────────────────────────────────┐")
        print(f"│ 🆔 ID       : {self.item_id:<28}│")
        print(f"│ 📦 Product  : {self.name:<28}│")
        print(f"│ 📊 Quantity : {self.quantity!s:<28}│")
        print(f"│ 💰 Price    : ₹{self.price:<27.2f}│")
        print(f"│ 🏷 SKU      : {self.sku[:8]:<28}│")
        print("└──────────────────────────────────────────────┘")


class InventoryManager:
    next_item_id = 1

    def __init__(self, file):
        self.file = file
        self.inventory = []
        self.load_inventory()

    def load_inventory(self):
        try:
            with open(self.file, "r", newline="") as csv_file:
                reader = csv.DictReader(csv_file)

                self.inventory = [
                    InventoryItem(
                        int(row["ItemID"]),
                        row["Name"],
                        int(row["Quantity"]),
                        float(row["Price"]),
                        row["SKU"],
                    )
                    for row in reader
                ]

                if self.inventory:
                    InventoryManager.next_item_id = (
                        max(item.item_id for item in self.inventory) + 1
                    )

        except FileNotFoundError:
            pass

    def save_inventory(self):
        with open(self.file, "w", newline="") as csv_file:
            fieldnames = ["ItemID", "Name", "Quantity", "Price", "SKU"]

            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()

            for item in self.inventory:
                writer.writerow(
                    {
                        "ItemID": item.item_id,
                        "Name": item.name,
                        "Quantity": item.quantity,
                        "Price": item.price,
                        "SKU": item.sku,
                    }
                )

    def add_item(self, name, quantity, price):
        item = InventoryItem(
            InventoryManager.next_item_id,
            name,
            quantity,
            price,
        )

        self.inventory.append(item)
        InventoryManager.next_item_id += 1
        self.save_inventory()

    def display_inventory(self):
        if not self.inventory:
            print("\n❌ Inventory is empty.")
            return

        print("\n" + "═" * 58)
        print("                    INVENTORY")
        print("═" * 58)
        print(f"{'ID':<5}{'PRODUCT':<22}{'QTY':<10}{'PRICE'}")
        print("─" * 58)

        for item in self.inventory:
            print(
                f"{item.item_id:<5}"
                f"{item.name:<22}"
                f"{item.quantity:<10}"
                f"₹{item.price:.2f}"
            )

        print("─" * 58)
        print(f"Total Items : {len(self.inventory)}")

    def delete_item_by_id(self, item_id):
        original = len(self.inventory)

        self.inventory = [item for item in self.inventory if item.item_id != item_id]

        self.save_inventory()
        return len(self.inventory) != original

    def filter_items(self, max_price):
        return [item for item in self.inventory if item.price <= max_price]


def main():
    store = InventoryManager("inventory.csv")

    while True:
        print("\n" + "═" * 58)
        print("           📦 E-COMMERCE INVENTORY MANAGER")
        print("═" * 58)
        print(" 1. ➕ Add Item")
        print(" 2. 📋 View Inventory")
        print(" 3. 🔍 Filter by Price")
        print(" 4. 🗑 Delete Item")
        print(" 5. 💾 Save Inventory")
        print(" 6. 🚪 Exit")
        print("─" * 58)

        try:
            choice = int(input("Enter your choice (1-6): "))
        except ValueError:
            print("\n❌ Please enter a valid number.")
            continue

        match choice:

            case 1:
                print("\n" + "─" * 58)
                print("               ➕ ADD NEW PRODUCT")
                print("─" * 58)

                name = input("Product Name : ")
                quantity = int(input("Quantity     : "))
                price = float(input("Price (₹)    : "))

                store.add_item(name, quantity, price)
                print("\n✅ Item added successfully!")

            case 2:
                store.display_inventory()

            case 3:
                print("\n" + "─" * 58)
                print("              🔍 FILTER PRODUCTS")
                print("─" * 58)

                max_price = float(input("Maximum Price (₹): "))
                items = store.filter_items(max_price)

                if not items:
                    print("\n❌ No matching products found.")
                else:
                    print(f"\nProducts under ₹{max_price}")
                    for item in items:
                        item.display_info()

            case 4:
                store.display_inventory()

                item_id = int(input("\nEnter Item ID to delete: "))

                if store.delete_item_by_id(item_id):
                    print("\n✅ Item deleted successfully!")
                else:
                    print("\n❌ Item ID not found.")

            case 5:
                store.save_inventory()
                print("\n✅ Inventory saved successfully!")

            case 6:
                print("\n" + "═" * 58)
                print("        Thank you for using Inventory Manager")
                print("═" * 58)
                break

            case _:
                print("\n❌ Please choose a number between 1 and 6.")


if __name__ == "__main__":
    main()
