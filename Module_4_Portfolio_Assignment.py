class ItemToPurchase:
    #default constructor __init__() initializes the attributes of the ItemToPurchase object and takes 3 optional parameters
    def __init__(self, item_name="none", item_price=0, item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    def print_item_cost(self):
        total_cost = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${total_cost}")

# Ask the user how many items to input
num_items = int(input("Enter the number of items: "))

# Create a list to store the items
items = []

# Input details for each item
for i in range(num_items):
    print(f"\nItem {i + 1}")
    item_name = input("Enter the item name: ")
    item_price = float(input("Enter the item price: "))
    item_quantity = int(input("Enter the item quantity: "))
    items.append(ItemToPurchase(item_name, item_price, item_quantity))

# Calculate total cost
total_cost = sum(item.item_price * item.item_quantity for item in items)

# Output total cost
print("\nTOTAL COST")
for item in items:
    item.print_item_cost()
print(f"Total: ${total_cost}")
