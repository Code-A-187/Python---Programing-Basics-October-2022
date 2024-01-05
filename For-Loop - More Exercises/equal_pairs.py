# Input
n = int(input())

num_1 = int(input())
num_2 = int(input())

value = num_1 + num_2

diff = 0

max_diff = 0

# Logic

for pair in range(n-1):
    num_1 = int(input())
    num_2 = int(input())

    current_value = num_1 + num_2

    if current_value != value:
        diff = abs(value - current_value)
        value = current_value
    if diff > max_diff:
        max_diff = diff

# Output

if diff == 0:
    print(f"Yes, value={value}")
else:
    print(f"No, maxdiff={max_diff}")
