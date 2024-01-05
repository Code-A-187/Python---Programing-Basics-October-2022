# Input

bigger_number = int(input())

# Logic

while True:
    user_input = input()
    if user_input == 'Stop':
        break
    else:
        num = int(user_input)
    if num > bigger_number:
        bigger_number = num

# Output

print(bigger_number)
