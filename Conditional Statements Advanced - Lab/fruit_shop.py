# Input

fruit = input()
week_day = input()
quantity = float(input())

total = 0

# Logic

if week_day == 'Saturday' or week_day == "Sunday":
    if fruit == "banana":
        total = 2.70 * quantity
    if fruit == "apple":
        total = 1.25 * quantity
    if fruit == "orange":
        total = 0.90 * quantity
    if fruit == "grapefruit":
        total = 1.60 * quantity
    if fruit == "kiwi":
        total = 3.00 * quantity
    if fruit == "pineapple":
        total = 5.60 * quantity
    if fruit == "grapes":
        total = 4.20 * quantity

elif week_day == 'Monday' or \
        week_day == "Tuesday" or \
        week_day == "Wednesday" or \
        week_day == "Thursday" or \
        week_day == "Friday":
    if fruit == "banana":
        total = 2.50 * quantity
    if fruit == "apple":
        total = 1.20 * quantity
    if fruit == "orange":
        total = 0.85 * quantity
    if fruit == "grapefruit":
        total = 1.45 * quantity
    if fruit == "kiwi":
        total = 2.70 * quantity
    if fruit == "pineapple":
        total = 5.50 * quantity
    if fruit == "grapes":
        total = 3.85 * quantity

# Output
if total == 0:
    print("error")

else:
    print(f"{total:.2f}")
