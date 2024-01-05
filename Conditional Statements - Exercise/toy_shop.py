# Input
excursion = float(input())

puzzle = int(input())
doll = int(input())
teddy_bear = int(input())
minion = int(input())
truck = int(input())

puzzle_price = 2.60
doll_price = 3
teddy_bear_price = 4.10
minion_price = 8.20
truck_price = 2

profit = 0

# Logic

total_toys_count = puzzle + doll + teddy_bear + minion + truck

total_price = (puzzle * puzzle_price) + \
    (doll * doll_price) + \
    (teddy_bear * teddy_bear_price) + \
    (minion * minion_price) + \
    (truck * truck_price)

if total_toys_count >= 50:
    total_price *= 0.75

total_price *= 0.9


# Print
if total_price >= excursion:
    print(f"Yes! {total_price - excursion:.2f} lv left.")

else:
    print(f"Not enough money! {excursion - total_price:.2f} lv needed.")
