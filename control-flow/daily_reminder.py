# task
# priority
# time_bound

task = input("Enter your task: ").lower()
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()


match time_bound:
    case 'yes':
        if priority == 'high':
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
    case 'no':
        if priority == 'low':
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")

