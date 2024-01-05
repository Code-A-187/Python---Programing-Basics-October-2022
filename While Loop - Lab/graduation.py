# Input

name = input()
average = 0
grade = 1
fails = 0

# Logic

while True:
    current_grade = float(input())
    if current_grade < 4:
        fails += 1
        if fails >= 2:
            break
        continue
    average += current_grade
    grade += 1
    if grade > 12:
        break

# Output

if fails >= 2:
    print(f"{name} has been excluded at {grade} grade")

else:
    print(f"{name} graduated. Average grade: {average / 12:.2f}")
