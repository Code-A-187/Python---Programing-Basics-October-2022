# Input

number = int(input())

counter = 0

# Logic

for row in range(1, number + 1):
    for column in range(1, row + 1):
        counter += 1

        print(f'{counter}', end=' ') if row != column else print(f'{counter}')

        if counter == number:
            exit()

# Output

print()
