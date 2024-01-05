# Input

min_number = int(input())

# Logic

while True:
    user_input = input()
    if user_input == 'Stop':
        break
    else:
        num = int(user_input)
    if num < min_number:
        min_number = num

# Output

print(min_number)
