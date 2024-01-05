# Input

days = int(input()) - 1
room = input()
evaluation = input()

price = 0

# Logic

if room == 'room for one person':
    price = 18

elif room == 'apartment':
    price = 25

    if days > 15:
        price *= 0.5
    elif days < 10:
        price *= 0.7
    else:
        price *= 0.65

elif room == 'president apartment':
    price = 35
    if days > 15:
        price *= 0.8
    elif days < 10:
        price *= 0.9
    else:
        price *= 0.85

if evaluation == 'negative':
    price *= 0.9

else:
    price *= 1.25

# Output

print(f"{price * days:.2f}")
