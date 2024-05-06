def main():
    # Dictionary containing course numbers and room numbers
    room_numbers = {
        'CSC101': '3004',
        'CSC102': '4501',
        'CSC103': '6755',
        'NET110': '1244',
        'COM241': '1411'
    }

    # Dictionary containing course numbers and instructors
    instructors = {
        'CSC101': 'Haynes',
        'CSC102': 'Alvarado',
        'CSC103': 'Rich',
        'NET110': 'Burke',
        'COM241': 'Lee'
    }

    # Dictionary containing course numbers and meeting times
    meeting_times = {
        'CSC101': '8:00 a.m.',
        'CSC102': '9:00 a.m.',
        'CSC103': '10:00 a.m.',
        'NET110': '11:00 a.m.',
        'COM241': '1:00 p.m.'
    }

    # Print the list of courses available for a meeting today
    print("These are the courses that are included for a meeting today:")
    for index, course in enumerate(room_numbers.keys(), start=1):
        print(f"{index}. {course}")

    # Run the program in a loop
    while True:
        # Get user input for course number
        course_choice = int(input("Enter the number corresponding to the course: "))

        # Validate the user input
        if course_choice < 1 or course_choice > len(room_numbers):
            print("Invalid course number.")
            continue

        # Get the course number corresponding to the user's choice
        course_numbers_list = list(room_numbers.keys())
        selected_course = course_numbers_list[course_choice - 1]

        # Display course details
        print("Room Number:", room_numbers[selected_course])
        print("Instructor:", instructors[selected_course])
        print("Meeting Time:", meeting_times[selected_course])

        # Ask the user if they want to continue or quit
        choice = input("Do you want to continue (yes/no)? ").lower()
        if choice != 'yes':
            break

if __name__ == "__main__":
    main()
