# Input

groups_count = int(input())

musala, monblan, kilimandjaro, k2, everest = 0, 0, 0, 0, 0

total = 0

# Logic

for _ in range(groups_count):
    group = int(input())
    if group <= 5:
        musala += group
    elif group <= 12:
        monblan += group
    elif group <= 25:
        kilimandjaro += group
    elif group <= 40:
        k2 += group
    else:
        everest += group

total = musala + monblan + kilimandjaro + k2 + everest

# Output

print(f'{musala / total * 100:.2f}%')
print(f'{monblan / total * 100:.2f}%')
print(f'{kilimandjaro / total * 100:.2f}%')
print(f'{k2 / total * 100:.2f}%')
print(f'{everest / total * 100:.2f}%')
