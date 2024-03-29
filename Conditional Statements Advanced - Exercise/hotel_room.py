# Input

month = input()
nights = int(input())

studio_price = 0
apartment_price = 0

# Logic

if month == 'May' or month == 'October':
    studio_price = 50
    apartment_price = 65
    if nights > 14:
        studio_price *= 0.7
    elif nights > 7:
        studio_price *= 0.95

elif month == 'June' or month == 'September':
    studio_price = 75.20
    apartment_price = 68.70
    if nights > 14:
        studio_price *= 0.80

else:
    studio_price = 76
    apartment_price = 77

if nights > 14:
    apartment_price *= 0.9

# Output

print(f'Apartment: {apartment_price * nights:.2f} lv.')
print(f'Studio: {studio_price * nights:.2f} lv.')
