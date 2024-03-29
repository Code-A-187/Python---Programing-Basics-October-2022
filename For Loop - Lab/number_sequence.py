import sys
# Input

input_count = int(input())

max_number = -sys.maxsize

min_number = sys.maxsize

# Logic

for i in range(0, input_count):
    num = int(input())

    if num > max_number:
        max_number = num

    if num < min_number:
        min_number = num

# Output
print(f'Max number: {max_number}')
print(f'Min number: {min_number}')
