# daily_reminder.py

# Get user input
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Use match-case to handle different priority levels
match priority:
    case "high":
        print(f"Reminder: '{task}' is a high priority task.", end = "" )
        
        if time_bound == "yes":
            print(" that requires immediate attention today!")
        else:
            print(" Consider completing it when you have free time.")


    case "medium":
        print(f"Reminder: '{task}' is a medium priority task.", end = "" )
        if time_bound == "yes":
            print(" that requires immediate attention today!")
        else:
            print(" Consider completing it when you have free time.")

    case "low":
        print(f"Note: '{task}' is a low priority task.", end = "" )
        if time_bound == "yes":
            print(" that requires immediate attention today!")
        else:
            print(" Consider completing it when you have free time.")

    case _:
        print(f"Note: '{task}' has an unknown priority.")
       
