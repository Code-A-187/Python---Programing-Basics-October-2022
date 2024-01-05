import math

# Input
world_record = float(input())
distance = float(input())
time_one_meter = float(input())

# Logic

swimmer_record = (distance * time_one_meter) + (math.floor(distance / 15) * 12.5)

# Output
if swimmer_record < world_record:
    print(f'Yes, he succeeded! The new world record is {swimmer_record:.2f} seconds.')
else:
    print(f"No, he failed! He was {swimmer_record - world_record:.2f} seconds slower.")
