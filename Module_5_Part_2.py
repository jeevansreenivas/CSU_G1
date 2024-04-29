def main():
    # Prompt user for information
    name = input("Enter your name: ")
    registration_number = input("Enter your student registration number: ")
    books_purchased = int(input("Enter the number of books purchased this month: "))

    # Determine points earned based on number of books purchased
    if books_purchased == 0:
        points = 0
    elif books_purchased == 2:
        points = 5
    elif books_purchased == 4:
        points = 15
    elif books_purchased == 6:
        points = 30
    elif books_purchased >= 8:
        points = 60
    elif books_purchased == 1:
        print("Would you like to buy one more book to earn 5 points, instead of 0 points?")
        choice = input("Enter 'yes' if you want to buy one more book, else enter 'no': ")
        if choice.lower() == "yes":
            books_purchased += 1
            points = 5
        else:
            points = 0
    elif books_purchased == 3:
        print("Would you like to buy one more book to earn 15 points, instead of 5 points?")
        choice = input("Enter 'yes' if you want to buy one more book, else enter 'no': ")
        if choice.lower() == "yes":
            books_purchased += 1
            points = 15
        else:
            points = 0
    elif books_purchased == 5:
        print("Would you like to buy one more book to earn 30 points, instead of 15 points?")
        choice = input("Enter 'yes' if you want to buy one more book, else enter 'no': ")
        if choice.lower() == "yes":
            books_purchased += 1
            points = 30
        else:
            points = 0
    elif books_purchased == 7:
        print("Would you like to buy one more book to earn 60 points, instead of 30 points?")
        choice = input("Enter 'yes' if you want to buy one more book, else enter 'no': ")
        if choice.lower() == "yes":
            books_purchased += 1
            points = 60
        else:
            points = 0

    # Display points earned
    print(f"Dear {name}, your student registration number {registration_number} has earned {points} points this month.")

if __name__ == "__main__":
    main()
