from math import pi

# User Input
figure = input()

area = 0

# Logic
if figure == "square":
    length = float(input())
    area = length * length  # формула за площа на квадрат
elif figure == "rectangle":
    a_side = float(input())
    b_side = float(input())
    area = a_side * b_side  # формула за лице на правоъгълник
elif figure == "circle":
    radius = float(input())
    area = radius * (pi * radius)  # формула за площ на кръг
elif figure == "triangle":
    side_length = float(input())
    side_height = float(input())
    area = (side_length * side_height) / 2  # формула за площ на триъгълник

# Output
print(f'{area:.3f}')
