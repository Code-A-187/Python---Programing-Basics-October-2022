
rolls_paper = int(input())
rolls_cloth = int(input())
glue_volume = float(input())
discount = int(input()) / 100

# Logic

paper_price = 5.80 * rolls_paper

cloth_price = 7.20 * rolls_cloth

glue_price = 1.20 * glue_volume

price = paper_price + cloth_price + glue_price

# Output

print(f'{price - (price * discount):.3f}')
