# Input

season = input()
gender = input()
students_number = int(input())
overnights = int(input())

price = 0
sport = ''
# Logic

if season == "Winter":
    price = students_number * overnights * 9.60
    if gender == 'boys':
        sport = "Judo"
    elif gender == 'girls':
        sport = 'Gymnastics'
    else:
        sport = 'Ski'
        price = students_number * overnights * 10
elif season == 'Spring':
    price = students_number * overnights * 7.20
    if gender == 'boys':
        sport = "Tennis"
    elif gender == 'girls':
        sport = 'Athletics'
    else:
        sport = 'Cycling'
        price = students_number * overnights * 9.50
elif season == 'Summer':
    price = students_number * overnights * 15
    if gender == 'boys':
        sport = "Football"
    elif gender == 'girls':
        sport = 'Volleyball'
    else:
        sport = 'Swimming'
        price = students_number * overnights * 20

if students_number >= 50:
    price *= 0.5
elif students_number >= 20:
    price *= 0.85
elif students_number >= 10:
    price *= 0.95

# Output

print(f'{sport} {price:.2f} lv.')
