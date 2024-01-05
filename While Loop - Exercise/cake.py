# Input

width, length = int(input()), int(input())

total_pieces = width * length

eaten_peaces = 0

# Logic

while total_pieces >= eaten_peaces:
    pieces = input()

    if pieces == 'STOP':
        print(f"{total_pieces - eaten_peaces} pieces are left.")
        break
    else:
        eaten_peaces += int(pieces)

# Output
else:
    print(f'No more cake left! You need {eaten_peaces - total_pieces} pieces more.')
