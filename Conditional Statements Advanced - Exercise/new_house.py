# Input

flower = input()
flowers_qty = int(input())
budget = int(input())

rose_price = 5
dahlias_price = 3.80
tulip_price = 2.80
narcissus_price = 3
gladiolus_price = 2.50

total = 0

# Logic

if flower == 'Roses':
    total = rose_price * flowers_qty
    if flowers_qty > 80:
        total *= 0.9

elif flower == 'Dahlias':
    total = dahlias_price * flowers_qty
    if flowers_qty > 90:
        total *= 0.85

elif flower == 'Tulips':
    total = tulip_price * flowers_qty
    if flowers_qty > 80:
        total *= 0.85

elif flower == 'Narcissus':
    total = narcissus_price * flowers_qty
    if flowers_qty < 120:
        total *= 1.15

elif flower == 'Gladiolus':
    total = gladiolus_price * flowers_qty
    if flowers_qty < 80:
        total *= 1.2

# Output

if total <= budget:
    print(f"Hey, you have a great garden with {flowers_qty} {flower} and {(budget - total):.2f} leva left.")

else:
    print(f"Not enough money, you need {total - budget:.2f} leva more.")
