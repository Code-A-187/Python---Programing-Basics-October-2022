# Input

dancers = int(input())
points = float(input())
season = input()
place = input()

charity = 0

# Logic
if place == 'Abroad':
    charity = (dancers * points) * 1.5
    if season == 'summer':
        charity *= 0.9
    else:
        charity *= 0.85
elif place == 'Bulgaria':
    charity = dancers * points
    if season == 'summer':
        charity *= 0.95
    else:
        charity *= 0.92


# Output

print(f'Charity - {charity * 0.75:.2f}')
print(f'Money per dancer - {(charity * 0.25) / dancers:.2f}')
