from math import ceil, floor

# Input

vineyard = int(input())
grape = float(input())
wine_needed = int(input())
workers = int(input())

# Logic

total_grape = vineyard * grape

total_wine = (total_grape * 0.4) / 2.5

remainder = abs(total_wine - wine_needed)

# Output

if total_wine >= wine_needed:
    print(f'Good harvest this year! Total wine: {floor(total_wine)} liters.')
    print(f'{ceil(remainder)} liters left -> {ceil(remainder / workers)} liters per person.')
else:
    print(f'It will be a tough winter! More {floor(remainder)} liters wine needed.')
