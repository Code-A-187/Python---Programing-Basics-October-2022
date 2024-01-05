# Input

budget = float(input())
category = input()
group = int(input())

vip_ticket_price = 499.99
normal_ticket_price = 249.99

# Logic

if group >= 50:
    budget *= 0.75
elif group >= 25:
    budget *= 0.60
elif group >= 10:
    budget *= 0.50
elif group >= 5:
    budget *= 0.40
elif group >= 1:
    budget *= 0.25

if category == 'Normal':
    needed_tickets = group * normal_ticket_price
else:
    needed_tickets = group * vip_ticket_price

# Output

if needed_tickets <= budget:
    print(f'Yes! You have {budget - needed_tickets:.2f} leva left.')
else:
    print(f'Not enough money! You need {needed_tickets - budget:.2f} leva.')
