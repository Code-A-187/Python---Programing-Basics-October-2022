from math import floor
# Input

tournaments = int(input())
start_points = int(input())

points = 0

wins = 0

# Logic

for _ in range(tournaments):
    stage = input()

    if stage == 'W':
        points += 2000
        wins += 1
    elif stage == 'F':
        points += 1200
    elif stage == 'SF':
        points += 720

# Output

print(f'Final points: {start_points + points}')
print(f'Average points: {floor(points / tournaments)}')
print(f'{wins / tournaments * 100:.2f}%')
