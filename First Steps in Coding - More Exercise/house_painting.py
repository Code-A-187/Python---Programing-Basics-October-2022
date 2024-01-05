# Input

x = float(input())
y = float(input())
h = float(input())

# Logic

front_walls = ((x * x) * 2) - (1.2 * 2)
side_walls = ((x * y) * 2) - ((1.5 * 1.5) * 2)

ceiling = ((x * y) * 2) + (((x * h) / 2) * 2)

green_paint = (front_walls + side_walls) / 3.4
red_paint = ceiling / 4.3

# Output

print(f'{green_paint:.2f}')
print(f'{red_paint:.2f}')
