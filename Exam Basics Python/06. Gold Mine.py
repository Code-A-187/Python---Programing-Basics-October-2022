# Input

location = int(input())

# Logic

for i in range(location):
    average_mining = float(input())
    mining_days = int(input())
    produced = 0

    for j in range(mining_days):
        day_production = int(input())
        produced += day_production
    average_produced = produced / mining_days
    if average_produced >= average_mining:
        print(f"Good job! Average gold per day: {average_produced:.2f}.")
    else:
        print(f'You need {average_mining - average_produced:.2f} gold.')
