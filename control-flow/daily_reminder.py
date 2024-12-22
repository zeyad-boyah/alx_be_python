def main():
    task = input("Enter your task: ")
    while True:
        priority = input("Priority (high/medium/low): ").lower()
        if priority in ["high", "medium", "low"]:
            break
        else:
            print("Invalid priority. Please enter 'high', 'medium', or 'low'.")

    time_bound = input("Is it time-bound? (yes/no): ").lower()

    match priority:
        case "high":
            reminder_message = f"Reminder: '{task}' is a high priority task"
        case "medium":
            reminder_message = f"Reminder: '{task}' is a medium priority task."
        case "low":
            reminder_message = f"Reminder: '{task}' is a low priority task."
    if time_bound == "yes":
        reminder_message += " that requires immediate attention today!"
    elif time_bound == "no":
        reminder_message += " Consider completing it when you have free time."

    print(reminder_message)


main()
