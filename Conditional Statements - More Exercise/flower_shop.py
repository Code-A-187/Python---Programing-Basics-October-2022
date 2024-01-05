from math import ceil, floor

# Input

magnolias = int(input()) * 3.25
hyacinths = int(input()) * 4
roses = int(input()) * 3.50
cactus = int(input()) * 8
gift = float(input())

# Logic

turnover = (magnolias + hyacinths + roses + cactus) * 0.95

# Output
if turnover >= gift:
    print(f'She is left with {floor(turnover - gift)} leva.')
else:
    print(f'She will have to borrow {ceil(gift - turnover)} leva.')
