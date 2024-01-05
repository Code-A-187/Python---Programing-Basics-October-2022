# User input
nylon = int(input())
paint = int(input())
paint_thinner = int(input())
work_hours = int(input())

nylon_price = 1.50
paint_price = 14.50
paint_thinner_price = 5.00
bag_price = 0.40
work_price_hour = 0.30
nylon += 2
paint += paint * 0.10

# Logic
total_material_price = (nylon * nylon_price) + (paint * paint_price) + (paint_thinner * paint_thinner_price) + bag_price
total_work_price = (total_material_price * work_price_hour) * work_hours
total_price = total_material_price + total_work_price

# Print
print(total_price)
