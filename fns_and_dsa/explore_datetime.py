# explore_datetime.py

from datetime import datetime, timedelta

def display_current_datetime():
    """
    Displays the current date and time in a readable format.
    """
    current_date = datetime.now()
    print(f"Current date and time: {current_date.strftime('%Y-%m-%d %H:%M:%S')}")

def calculate_future_date():
    """
    Prompts the user for a number of days and calculates the future date.
    """
    try:
        num_days = int(input("Enter the number of days to add to the current date: "))
        current_date = datetime.now()
        future_date = current_date + timedelta(days=num_days)
        print(f"Future date: {future_date.strftime('%Y-%m-%d')}")
    except ValueError:
        print("Invalid input. Please enter an integer for the number of days.")

if __name__ == "__main__":
    display_current_datetime()
    calculate_future_date()