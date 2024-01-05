# User Input
pack_pencils = int(input())
pack_markers = int(input())
cleaner = int(input())
discount = int(input()) / 100

pen_price = 5.80
marker_price = 7.20
cleaner_price = 1.20

# Logic
price_before_discount = (pen_price * pack_pencils) + (marker_price * pack_markers) + (cleaner_price * cleaner)
total_discount_price = price_before_discount - (price_before_discount * discount)

# Print
print(total_discount_price)
