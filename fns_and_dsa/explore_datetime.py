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
#                  Friday, june 27 2025 09:15:45
# current_date.strftime('%A, %B %d %Y %H:%M:%S')  ##ABdY

# 📅 Date Components
# Code	Meaning	Example
# %Y	Year with century	2025
# %y	Year without century (00–99)	25
# %m	Month (01–12)	06
# %B	Full month name	June
# %b	Abbreviated month name	Jun
# %d	Day of the month (01–31)	27
# %j	Day of the year (001–366)	178
# %A	Full weekday name	Friday
# %a	Abbreviated weekday name	Fri
# %w	Weekday (0=Sunday, 6=Saturday)	5
# %U	Week number (Sunday first)	25
# %W	Week number (Monday first)	25

# 🕒 Time Components
# Code	Meaning	Example
# %H	Hour (00–23, 24-hour clock)	09
# %I	Hour (01–12, 12-hour clock)	09
# %p	AM or PM	AM
# %M	Minute (00–59)	15
# %S	Second (00–59)	45
# %f	Microsecond (000000–999999)	000123
# %z	UTC offset	+0300
# %Z	Timezone name	EAT

# 🧩 Miscellaneous
# Code	Meaning	Example
# %c	Full date and time	Fri Jun 27 09:15:45 2025
# %x	Local date representation	06/27/25 (depends on locale)
# %X	Local time representation	09:15:45
# %%	Literal % character	%

# ❌ Common Mistakes
# Mistaken Code	Correction
# %h	❌ Invalid — use %b for short month name
# %D	❌ Not standard — use %m/%d/%y manually
# %r	❌ Not available in all systems — use %I:%M:%S %p instead

