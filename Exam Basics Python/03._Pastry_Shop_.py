# Input

sweet_type = input()
sweets_number = int(input())
month_day = int(input())

price = 0

# Logic

if month_day > 15:
    if sweet_type == 'Cake':
        price = sweets_number * 28.70
    elif sweet_type == "Souffle":
        price = sweets_number * 9.80
    elif sweet_type == "Baklava":
        price = sweets_number * 16.98
else:
    if sweet_type == 'Cake':
        price = sweets_number * 24
    elif sweet_type == "Souffle":
        price = sweets_number * 6.66

    elif sweet_type == "Baklava":
        price = sweets_number * 12.60

if month_day <= 22:
    price = 

# Output

print(f'{price:.2f}')
