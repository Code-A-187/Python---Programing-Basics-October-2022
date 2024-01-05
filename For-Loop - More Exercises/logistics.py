# Input

load_num = int(input())

sum_loads = 0

bus = 0
truck = 0
train = 0

# Logic

for _ in range(1, load_num + 1):
    load = int(input())

    sum_loads += load

    if load >= 12:
        train += load
    elif load >= 4:
        truck += load
    else:
        bus += load

# Output
print(f'{(bus * 200 + truck * 175 + train * 120) / sum_loads:.2f}')
print(f'{bus / sum_loads * 100:.2f}%')
print(f'{truck / sum_loads * 100:.2f}%')
print(f'{train / sum_loads * 100:.2f}%')
