# Part 1: Calculate Total Amount of a Meal( Cost of Meal + Tip + Tax)

# Function to calculate total amount including tip and tax
def calculate_total(charge):
    # Calculate tip(18%) and tax(7%)
    tip = 0.18 * charge
    tax = 0.07 * charge
    # Calculate total amount
    total_amount = charge + tip + tax
    return tip, tax, total_amount

# Main program
def main():
    while True:
        # Input charge for food
        charge = float(input("Enter the charge for the food: $"))

        # Calculate total amount
        tip, tax, total_amount = calculate_total(charge)

        # Display amounts
        print("Breakdown of Charges:")
        print(f"  Tip: ${tip:.2f}")
        print(f"  Sales Tax: ${tax:.2f}")
        print(f"  Total Price: ${total_amount:.2f}")

        # Check if the user wants to continue for another meal
        continue_option = input("\nDo you want to calculate for another meal? (yes/no): ").lower()
        if continue_option != 'yes':
            print("Thank you for using our service! Have a great day!")
            break

if __name__ == "__main__":
    main()
