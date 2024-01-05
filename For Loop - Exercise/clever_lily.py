# Input

age = int(input())
wash_mash_price = float(input())
toy_price = int(input())

money_given = 10
saved = 0
toys = 0

# Logic
for i in range(1, age + 1):
    if i % 2 == 0:
        saved += money_given - 1
        money_given += 10
    else:
        toys += 1

toys *= toy_price

budget = saved + toys

# Print

if budget >= wash_mash_price:
    print(f'Yes! {budget - wash_mash_price:.2f}')
else:
    print(f'No! {wash_mash_price - budget:.2f}')
