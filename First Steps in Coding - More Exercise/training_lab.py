# Input

w = float(input()) * 100
h = float(input()) * 100

# Logic

row_places = w // 120

length_places = (h - 100) // 70

total_places = row_places * length_places - 3

# Output

print(f'{total_places:.2f}')
