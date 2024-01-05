# Input

start_num = int(input())
end_num = int(input())
magic_num = int(input())

counter = 0

is_found = False

# Logic

for first_digit in range(start_num, end_num + 1):
    if is_found:
        break
    for second_digit in range(start_num, end_num + 1):
        counter += 1
        if first_digit + second_digit == magic_num:
            print(f'Combination N:{counter} ({first_digit} + {second_digit} = {magic_num})')
            is_found = True
            break

if not is_found:
    print(f'{counter} combinations - neither equals {magic_num}')
