# Input

num_one, num_two = int(input()), int(input())

odd_sum = 0
even_sum = 0

# Logic

for number in range(num_one, num_two +1):
    odd_sum, even_sum = 0, 0

    for index, digit in enumerate(str(number)):
        if index % 2 == 0:
            even_sum += int(digit)
        else:
            odd_sum += int(digit)

# Output

    if odd_sum == even_sum:
        print (f'{number}', end=' ')
