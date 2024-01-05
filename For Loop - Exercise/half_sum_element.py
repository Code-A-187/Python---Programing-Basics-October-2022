import sys
# Input

number = int(input())

max_number = -sys.maxsize
sum_numbers = 0

# Logic

for i in range(number):
    number = int(input())

    if number > max_number:
        max_number = number

    sum_numbers += number

# Output

if max_number == sum_numbers - max_number:
    print(f'Yes\nSum = {max_number}')

else:
    print(f'No\nDiff = {abs (max_number - (sum_numbers - max_number))}')
