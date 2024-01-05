# Input
hours = int(input())
minutes = int(input())

# Logic
hours = hours * 60

total_time = hours + minutes + 15

hours = total_time // 60

minutes = total_time % 60

if hours == 24:
    hours = "0"

minutes = "0" + str(minutes) if minutes < 10 else minutes

# Output

print(f'{hours}:{minutes}')
