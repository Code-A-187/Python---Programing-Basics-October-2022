# Input

n, m, s, = int(input()), int(input()), int(input())

# Logic

for address in range(m, n, -1):
    if address % 2 == 0 and address % 3 == 0:
        if address == s:
            break
        print(address, end=' ')
