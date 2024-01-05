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

total = (puzzle * puzzle_price) + \
        (doll * doll_price) + \
        (teddy_bear * teddy_bear_price) + \
        (minion * minion_price) + \
        (truck * truck_price)

if puzzle + doll + teddy_bear + minion + truck >= 50:
    total *= 0.75

total *= 0.9

profit = total - excursion

# Print

if profit >= 0:
    print(f"Yes! {profit:.2f} lv left.")

else:
    print(f"Not enough money! {abs(profit):.2f} lv needed.")
