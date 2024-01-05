# Input

season = input()
distance = float(input())

salary = 0
# Logic

if 10000 < distance <= 20000:
    salary = distance * 1.45
elif distance > 5000:
    if season == 'Winter':
        salary = distance * 1.25
    elif season == 'Summer':
        salary = distance * 1.10
    else:
        salary = distance * 0.95
else:
    if season == 'Winter':
        salary = distance * 1.05
    elif season == 'Summer':
        salary = distance * 0.90
    else:
        salary = distance * 0.75

# Output

print(f'{(salary * 4) * 0.9:.2f}')
