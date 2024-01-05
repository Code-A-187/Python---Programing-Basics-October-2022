# Input

will_money = float(input())
year = int(input())

age = 18
spending = 0
# Logic

for i in range(1800, year + 1):
    if i % 2 == 0:
        spending += 12000
    else:
        spending += 12000 + age * 50
    age += 1

# Output

if will_money >= spending:
    print(f'Yes! He will live a carefree life and will have {will_money - spending:.2f} dollars left.')

else:
    print(f'He will need {spending - will_money:.2f} dollars to survive.')
