num_1, num_2, num_3 = int(input()), int(input()), int(input())

for i in range(1, num_1 + 1):
    if i % 2 != 0:
        continue
    for j in range(2, num_2 + 1):
        if j > 7 or j % 1 != 0:
            continue
        for k in range(1, num_3 + 1):
            if k % 2 != 0:
                print(i, j, k)
