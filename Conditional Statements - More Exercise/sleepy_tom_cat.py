# Input

holidays = int(input())
play_norm = 30000

# Logic

total_play = (holidays * 127) + ((365 - holidays) * 63)

time = abs(play_norm - total_play)

hours = time // 60
minutes = time % 60

# Output

if play_norm < total_play:
    print('Tom will run away')
    print(f'{hours} hours and {minutes} minutes more for play')

else:
    print('Tom sleeps well')
    print(f'{hours} hours and {minutes} minutes less for play')
