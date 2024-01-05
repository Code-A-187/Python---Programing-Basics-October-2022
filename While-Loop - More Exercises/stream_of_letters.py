# Input

c, o, n = 0, 0, 0

word = ''
result = ''

# Logic

while True:
    if c == 1 and o == 1 and n == 1:
        word += ' '
        c = 0
        o = 0
        n = 0

        result = word

    letter = input()

    if letter == 'End':
        break
    if letter == 'c' and c == 0:
        c += 1
        continue
    if letter == 'o' and o == 0:
        o += 1
        continue

    if letter == 'n' and n == 0:
        n += 1
        continue

    if 65 <= ord(letter) <= 90 or 97 <= ord(letter) <= 122:
        word += letter

# Output

print(f"{result} ")
