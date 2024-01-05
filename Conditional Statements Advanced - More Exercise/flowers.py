# Input

chrysanthemums, roses, tulips = int(input()), int(input()), int(input())
season, holidays = input(), input()

chrysanthemums_price, roses_price, tulips_price = 0, 0, 0

total_flowers = chrysanthemums + roses + tulips

# Logic

if season == 'Spring' or season == 'Summer':
    chrysanthemums_price = 2.00 * chrysanthemums
    roses_price = 4.10 * roses
    tulips_price = 2.50 * tulips
else:
    chrysanthemums_price = 3.75 * chrysanthemums
    roses_price = 4.50 * roses
    tulips_price = 4.15 * tulips

if holidays == "Y":
    chrysanthemums_price *= 1.15
    roses_price *= 1.15
    tulips_price *= 1.15

bouquet_price = chrysanthemums_price + roses_price + tulips_price

if season == 'Spring' and tulips > 7:
    bouquet_price *= 0.95


if season == 'Winter' and roses >= 10:
    bouquet_price *= 0.90

if total_flowers > 20:
    bouquet_price *= 0.8

# Output

print(f'{bouquet_price + 2:.2f}')
