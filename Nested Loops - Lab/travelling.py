# Input
money = 0

# Logic

while True:
    destination = input()
    if destination == 'End':
        break
    budget = float(input())
    while True:
        sum = float(input())
        money += sum
        if money >= budget:
            print(f'Going to {destination}!')
            money = 0
            break
