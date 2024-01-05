# Input

budget = float(input())
season = input()

spending = 0
destination = ''

# Logic

if budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        vacation = 'Camp'
        spending = budget * 0.3
    else:
        vacation = 'Hotel'
        spending = budget * 0.7

elif 100 < budget <= 1000:
    destination = 'Balkans'
    if season == 'summer':
        vacation = 'Camp'
        spending = budget * 0.4
    else:
        vacation = 'Hotel'
        spending = budget * 0.8

else:
    destination = 'Europe'
    vacation = 'Hotel'
    spending = budget * 0.9


# Output

print(f"Somewhere in {destination}")

print(f"{vacation} - {spending:.2f}")
