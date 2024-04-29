import random

def main():
    while True:
        num_years = int(input("Enter the number of years: "))
        start_year = int(input("Enter the starting year: "))

        manual_entry = input("Do you want to enter rainfall data manually? (yes/no): ").lower() == "yes"

        total_rainfall = 0
        total_months = 0

        print("\nRainfall Data:")
        for year in range(start_year, start_year + num_years):
            for month in range(1, 13):
                if manual_entry:
                    inches = float(input(f"Enter inches of rainfall for {month}/{year}: "))
                else:
                    inches = random.uniform(0, 10)
                total_rainfall += inches
                total_months += 1
                print(f"{month}/{year}: {inches:.2f} inches")

        average_rainfall = total_rainfall / total_months

        print("\nRainfall Summary:")
        print("Total number of months:", total_months)
        print("Total inches of rainfall:", total_rainfall)
        print("Average rainfall per month:", average_rainfall)

        choice = input("Do you want to do another round? (yes/no): ")
        if choice.lower() != "yes":
            break

if __name__ == "__main__":
    main()
