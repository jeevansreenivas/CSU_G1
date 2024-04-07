# Part 2: Time Conversion

# Function to calculate the alarm time
def calculate_alarm_time(current_hour, current_minute, hours_to_wait):
    # Convert current time to minutes
    total_minutes = current_hour * 60 + current_minute
    # Add hours to wait (converting to minutes)
    total_minutes += int(hours_to_wait * 60)
    # Calculate alarm time
    alarm_hour = total_minutes // 60 % 24
    alarm_minute = total_minutes % 60
    return alarm_hour, alarm_minute

# Main program
def main():
    print("Please enter the current time in 24-hour format (HH:MM):")
    current_time = input("Example: For 1:30 PM, enter 13:30: ")
    current_hour, current_minute = map(int, current_time.split(":"))

    hours_to_wait = float(input("Enter the number of hours to wait for the alarm: "))

    alarm_hour, alarm_minute = calculate_alarm_time(current_hour, current_minute, hours_to_wait)

    print(f"The alarm will go off at {alarm_hour}:{alarm_minute:02d} (24-hour format).")

if __name__ == "__main__":
    main()
