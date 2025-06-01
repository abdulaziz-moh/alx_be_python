# daily_reminder.py

# Loop to allow only valid input for priority and time-bound
while True:
    # Prompt for task details
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    # Validate inputs
    if priority not in ["high", "medium", "low"]:
        print("Please enter a valid priority: high, medium, or low.")
        continue
    if time_bound not in ["yes", "no"]:
        print("Please enter 'yes' or 'no' for time-bound.")
        continue

    # Process task with match-case
    match priority:
        case "high":
            message = f"Reminder: '{task}' is a high priority task"
        case "medium":
            message = f"Reminder: '{task}' is a medium priority task"
        case "low":
            message = f"Note: '{task}' is a low priority task"
        case _:
            message = f"Note: '{task}' has an unrecognized priority"

    # Add time-bound info
    if time_bound == "yes":
        message += " that requires immediate attention today!"
    else:
        message += ". Consider completing it when you have free time."

    # Print the final message and exit loop
    print("\n" + message)
    break
