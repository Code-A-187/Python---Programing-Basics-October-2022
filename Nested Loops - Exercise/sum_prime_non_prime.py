
prime_num = 0
non_prime_num = 0

while True:
    command = input()
    if command == "stop":
        break

    current_number = int(command)
    is_prime = True
    if current_number < 0:
        print('Number is negative.')
        continue

    for number in range(2, current_number):
        if current_number % number == 0:
            is_prime = False
            break
    if is_prime:
        prime_num += current_number
    else:
        non_prime_num += current_number

print(f'Sum of all prime numbers is: {prime_num}')
print(f'Sum of all non prime numbers is: {non_prime_num}')
