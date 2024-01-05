# Input

pocket_money = float(input())
selling_money = float(input())
expenses = float(input())
gift_price = float(input())

# Logic

saved_money = ((pocket_money + selling_money) * 5) - expenses

# Output

if saved_money < gift_price:
    print(f'Insufficient money: {gift_price - saved_money:.2f} BGN.')
else:
    print(f'Profit: {saved_money:.2f} BGN, the gift has been purchased.')
