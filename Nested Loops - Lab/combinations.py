# Input

number = int(input())

counter = 0

# Logic

for i in range(0, number + 1):
    for j in range(0, number + 1):
        for k in range(0, number + 1):
            if i + j + k == number:
                counter += 1

# Output

print(counter)
