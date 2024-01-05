# Input

junior = float(input())
seniors = float(input())
track_type = input()

junior_tax = 0
seniors_tax = 0

# Logic

if track_type == 'trail':
    junior_tax = 5.50
    seniors_tax = 7
elif track_type == 'cross-country':
    junior_tax = 8
    seniors_tax = 9.50
    if junior + seniors >= 50:
        junior_tax = 8 * 0.75
        seniors_tax = 9.50 * 0.75
elif track_type == 'downhill':
    junior_tax = 12.25
    seniors_tax = 13.75
if track_type == 'road':
    junior_tax = 20
    seniors_tax = 21.50

donation = (junior_tax * junior) + (seniors_tax * seniors)

# Output

print(f'{donation * 0.95:.2f}')
