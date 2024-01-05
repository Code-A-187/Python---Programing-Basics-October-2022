# Input
hours = int(input())
minutes = int(input()) + 15

# Logic

if minutes > 59:
    hours += 1
    minutes -= 60

if hours > 23:
    hours -= 24

minutes = "0" + str(minutes) if minutes < 10 else minutes

# Output

print(f'{hours}:{minutes}')
