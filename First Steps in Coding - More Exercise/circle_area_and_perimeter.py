from math import pi
# Input

circle_radius = float(input())

# Logic

area = pi * (circle_radius * circle_radius)

perimeter = (pi * circle_radius) * 2

# Output

print(f'{area:.2f}')
print(f'{perimeter:.2f}')
