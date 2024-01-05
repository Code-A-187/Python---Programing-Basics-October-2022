from math import floor

# Input

width = float(input())
length = float(input())
height = float(input())
astronauts_height = float(input())

# Logic

spaceship_volume = width * length * height

room_volume = (astronauts_height + 0.4) * 2 * 2

astronauts = floor(spaceship_volume / room_volume)

if astronauts > 10:
    print("The spacecraft is too big.")
elif astronauts > 3:
    print(f"The spacecraft holds {astronauts} astronauts.")
else:
    print("The spacecraft is too small.")

