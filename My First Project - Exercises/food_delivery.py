# User Input

chicken_menu = int(input())
fish_menu = int(input())
veggie_menu = int(input())

chicken_price = 10.35
fish_price = 12.40
veggie_price = 8.15
dessert = 0.20
delivery_price = 2.50

# Logic

menus_price = (chicken_price * chicken_menu) + (fish_menu * fish_price) + (veggie_menu * veggie_price)
desert_price = menus_price * dessert
total_price = menus_price + desert_price + delivery_price

# Print

print(round(total_price, 2))
