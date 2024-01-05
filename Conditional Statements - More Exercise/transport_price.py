# Input

distance_km = int(input())
day_part = input()

bus = 0.09
train = 0.06
taxi = 0

transport_expenses = 0

# Logic

if day_part == 'day':
    taxi = 0.79
else:
    taxi = 0.90

if distance_km >= 100:
    transport_expenses = train * distance_km
elif distance_km >= 20:
    transport_expenses = bus * distance_km
else:
    transport_expenses = taxi * distance_km + 0.70

# Output

print(f'{transport_expenses:.2f}')
