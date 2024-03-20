def addition(numbers):
    return sum(numbers)


def subtraction(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result -= num
    return result


def multiplication(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result


def division(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        if num != 0:
            result /= num
        else:
            return "Cannot divide by zero"
    return result


def main():

    while True:
        print("\nMenu:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "5":
            print("Exiting the program. Goodbye!")
            break

        try:
            operation = int(choice)
            if operation < 1 or operation > 4:
                print("Invalid choice. Please enter a number between 1 and 5.")
                continue

            num_count = int(input("How many numbers do you want to input? "))
            numbers = [float(input(f"Enter number {i + 1}: ")) for i in range(num_count)]

            if operation == 1:
                result = addition(numbers)
            elif operation == 2:
                result = subtraction(numbers)
            elif operation == 3:
                result = multiplication(numbers)
            elif operation == 4:
                result = division(numbers)

            print(f"The result is: {result}")

        except ValueError:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
