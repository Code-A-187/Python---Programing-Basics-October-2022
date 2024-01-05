# User Input
annual_training_price = int(input())

snickers = 0.40
equipment = 0.20

# Logic
snickers_price = annual_training_price - (annual_training_price * snickers)
equipment_price = snickers_price - (snickers_price * equipment)
ball_price = equipment_price / 4
accessories_price = ball_price / 5

total_training_price = annual_training_price + snickers_price + equipment_price + ball_price + accessories_price

# Print
print(total_training_price)
