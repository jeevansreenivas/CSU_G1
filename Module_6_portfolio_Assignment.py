from datetime import datetime

class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0, item_quantity=0, item_description="none", date_added=None):
        # Initialize item attributes
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description
        if date_added is None:
            self.date_added = datetime.now().strftime("%B %d, %Y")
        else:
            self.date_added = date_added

    def print_item_cost(self):
        # Print cost of the item
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${self.item_quantity * self.item_price}")

    def print_item_description(self):
        # Print description of the item
        print(f"{self.item_name}: {self.item_description} (Added on: {self.date_added})")


class ShoppingCart:
    def __init__(self, customer_name="none", current_date=None):
        # Parameterized constructor to initialize customer name and current date
        self.customer_name = customer_name
        if current_date is None:
            # Use current date if not provided
            self.current_date = datetime.now().strftime("%B %d, %Y")
        else:
            self.current_date = current_date
        self.cart_items = []

    def add_item(self, item):
        # Add item to the shopping cart
        self.cart_items.append(item)

    def remove_item(self, item_name):
        # Remove item from the shopping cart
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                return
        print("Item not found in cart. Nothing removed.")

    def modify_item(self, item_name, new_item):
        # Modify item in the shopping cart
        for i in range(len(self.cart_items)):
            if self.cart_items[i].item_name == item_name:
                if new_item.item_description != "none":
                    self.cart_items[i].item_description = new_item.item_description
                if new_item.item_price != 0:
                    self.cart_items[i].item_price = new_item.item_price
                if new_item.item_quantity != 0:
                    self.cart_items[i].item_quantity = new_item.item_quantity
                return
        print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        # Get total quantity of items in the cart
        return sum(item.item_quantity for item in self.cart_items)

    def get_cost_of_cart(self):
        # Get total cost of items in the cart
        return sum(item.item_price * item.item_quantity for item in self.cart_items)

    def print_total(self):
        # Print total cost and details of items in the cart
        if not self.cart_items:
            print("SHOPPING CART IS EMPTY")
            return
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Number of Items:", self.get_num_items_in_cart())
        for item in self.cart_items:
            item.print_item_cost()
        print("Total:", f"${self.get_cost_of_cart()}")

    def print_descriptions(self):
        # Print descriptions of all items in the cart
        if not self.cart_items:
            print("SHOPPING CART IS EMPTY")
            return
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions")
        for item in self.cart_items:
            item.print_item_description()


def print_menu(cart):
    # Print menu options to handle user input
    option = ""
    while option != "q":
        print("\nMENU")
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("c - Change item quantity")
        print("i - Output items' descriptions")
        print("o - Output shopping cart")
        print("q - Quit")
        option = input("Choose an option: ")
        if option == "a":
            item_name = input("Enter the item name: ")
            item_description = input("Enter the item description: ")
            item_price = float(input("Enter the item price: "))
            item_quantity = int(input("Enter the item quantity: "))
            cart.add_item(ItemToPurchase(item_name, item_price, item_quantity, item_description))
        elif option == "r":
            item_name = input("Enter the name of the item to remove: ")
            cart.remove_item(item_name)
        elif option == "c":
            item_name = input("Enter the name of the item to modify: ")
            new_description = input("Enter the new description (press Enter to skip): ")
            new_price_input = input("Enter the new price (press Enter to skip): ")
            new_quantity_input = input("Enter the new quantity (press Enter to skip): ")

            # Find the item in the cart
            found_item = None
            for item in cart.cart_items:
                if item.item_name == item_name:
                    found_item = item
                    break

            if found_item:
                # Create a new ItemToPurchase object with updated values
                new_item = ItemToPurchase(item_name)
                if new_description:
                    new_item.item_description = new_description
                if new_price_input:
                    new_item.item_price = float(new_price_input)
                if new_quantity_input:
                    new_item.item_quantity = int(new_quantity_input)

                # Modify the item in the cart
                cart.modify_item(item_name, new_item)
            else:
                print("Item not found in cart. Nothing modified.")

        elif option == "i":
            cart.print_descriptions()
        elif option == "o":
            cart.print_total()
        elif option == "q":
            print("Goodbye!")
        else:
            print("Invalid option. Please choose again.")


def main():
    # Main function to create shopping cart and start menu
    customer_name = input("Enter customer's name: ")
    date_input = input("Enter the date (e.g., January 1, 2024): ")

    try:
        # Try to parse the date input in the expected format
        current_date = datetime.strptime(date_input, "%B %d, %Y").strftime("%B %d, %Y")
    except ValueError:
        # If the input format is incorrect, use the current date
        current_date = datetime.now().strftime("%B %d, %Y")
        print("Invalid date format. Using current date instead.")

    print_menu(ShoppingCart(customer_name, current_date))


if __name__ == "__main__":
    main()
