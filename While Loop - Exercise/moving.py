total_volume = int(input()) * int(input()) * int(input())
space_filled = 0

while space_filled < total_volume:
    carton = input()

    if carton == 'Done':
        print(f"{total_volume - space_filled} Cubic meters left.")
        break

    space_filled += int(carton)
else:
    print(f"No more free space! You need {space_filled - total_volume} Cubic meters more.")
