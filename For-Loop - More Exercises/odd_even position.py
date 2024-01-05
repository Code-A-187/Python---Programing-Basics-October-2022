import sys

# Input


num = int(input())

oddsum = 0
evensum = 0

evenmin = sys.maxsize
evenmax = -sys.maxsize
oddmin = sys.maxsize
oddmax = -sys.maxsize

# Logic

for i in range(1, num + 1):
    number = float(input())

    if i % 2 == 0:
        if number > evenmax:
            evenmax = number
        if number < evenmin:
            evenmin = number
        evensum += number

    else:
        if number > oddmax:
            oddmax = number
        if number < oddmin:
            oddmin = number
        oddsum += number
# Output

print(f"OddSum={oddsum:.2f},")
if oddmin == sys.maxsize:
    print(f"OddMin=No,")
else:
    print(f"OddMin={oddmin:.2f},")
if oddmax == - sys.maxsize:
    print(f'OddMax=No,')
else:
    print(f"OddMax={oddmax:.2f},")

print(f"EvenSum={evensum:.2f},")
if evenmin == sys.maxsize:
    print(f'EvenMin=No,')
else:
    print(f"EvenMin={evenmin:.2f},")
if evenmax == -sys.maxsize:
    print(f'EvenMax=No')
else:
    print(f"EvenMax={evenmax:.2f}")
