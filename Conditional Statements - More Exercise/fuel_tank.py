# Input

fuel = input()
volume = float(input())

# Logic

if fuel == 'Diesel':
    fuel = 'diesel'
    if volume >= 25:
        print(f'You have enough {fuel}.')
    else:
        print(f'Fill your tank with {fuel}!')
elif fuel == 'Gasoline':
    fuel = 'gasoline'
    if volume >= 25:
        print(f'You have enough {fuel}.')
    else:
        print(f'Fill your tank with {fuel}!')
elif fuel == 'Gas':
    fuel = "gas"
    if volume >= 25:
        print(f'You have enough {fuel}.')
    else:
        print(f'Fill your tank with {fuel}!')
else:
    print('Invalid fuel!')
