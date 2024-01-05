# Input

budget = float(input())
season = input()

# Logic

if budget > 500:
    car_class = 'Luxury class'
    car = 'Jeep'
    budget *= 0.9
elif budget > 100:
    car_class = 'Compact class'
    if season == 'Summer':
        car = 'Cabrio'
        budget *= 0.45
    else:
        car = 'Jeep'
        budget *= 0.8
else:
    car_class = "Economy class"
    if season == 'Summer':
        car = 'Cabrio'
        budget *= 0.35
    else:
        car = 'Jeep'
        budget *= 0.65
# Output

print(f'{car_class}')
print(f"{car} - {budget:.2f}")
