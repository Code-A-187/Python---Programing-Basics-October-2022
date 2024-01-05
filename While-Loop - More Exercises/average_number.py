
num = int(input())

average = 0

for i in range(num):
    number = int(input())
    average += number

print(f'{average / num:.2f}')
