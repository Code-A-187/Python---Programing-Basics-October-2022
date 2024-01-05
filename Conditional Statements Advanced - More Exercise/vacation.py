# Input

budget = float(input())
season = input()

accommodation = ''
location = ''
# Logic

if budget > 3000:
    accommodation = "Hotel"
    budget *= 0.9
    if season == "Summer":
        location = 'Alaska'
    else:
        location = 'Morocco'
elif budget > 1000:
    accommodation = 'Hut'
    if season == "Summer":
        budget *= 0.8
        location = 'Alaska'
    else:
        budget *= 0.6
        location = 'Morocco'
else:
    accommodation = 'Camp'
    if season == "Summer":
        budget *= 0.65
        location = 'Alaska'
    else:
        budget *= 0.45
        location = 'Morocco'

# Output

print(f"{location} - {accommodation} - {budget:.2f}")
