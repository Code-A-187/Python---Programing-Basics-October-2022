from math import ceil, floor

# Input

paint = int(input())
rolls = int(input())

price_glove = float(input())
price_brush = float(input())

# Logic

gloves = ceil(rolls * 0.35)
brushes = floor(paint * 0.48)

paint_price = paint * 21.50
rolls_price = rolls * 5.20
gloves_price = price_glove * gloves
brushes_price = price_brush * brushes

price = paint_price + rolls_price + gloves_price + brushes_price

# Output

print(f"This delivery will cost {price / 15:.2f} lv.")
