# Input

vacation_money = float(input())
balance = float(input())

spending_days_count = 0
days = 0

# Logic

while spending_days_count < 5:
    action = input()
    money = float(input())

    days += 1

    if action == 'spend':
        balance = balance - money if balance - money > 0 else 0
        spending_days_count += 1
    else:
        balance += money
        spending_days_count = 0

    if balance >= vacation_money:
        print(f'You saved the money for {days} days.')
        break
# Output
else:
    print("You can't save the money.")
    print(f"{days}")
