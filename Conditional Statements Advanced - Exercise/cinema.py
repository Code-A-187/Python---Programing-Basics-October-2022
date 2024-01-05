# Input

screening = input()
row = int(input())
columns = int(input())

income = 0

cinema_capacity = row * columns

# Logic

if screening == 'Premiere':
    income = cinema_capacity * 12.00
elif screening == 'Normal':
    income = cinema_capacity * 7.50
elif screening == 'Discount':
    income = cinema_capacity * 5.00

# Output
print(f'{income:.2f} leva')
