# Input

max_unwanted_grades = int(input())

current_unwanted_grades = 0
total_grades = 0
grades_sum = 0
last_problem = ''

# Logic

while current_unwanted_grades < max_unwanted_grades:
    exercise = input()
    if exercise == 'Enough':
        print(f"Average score: {grades_sum / total_grades:.2f}")
        print(f"Number of problems: {total_grades}")
        print(f"Last problem: {last_problem}")
        break

    grade = int(input())

    if grade <= 4:
        current_unwanted_grades += 1

    grades_sum += grade
    total_grades += 1
    last_problem = exercise

# Output

else:
    print(f"You need a break, {current_unwanted_grades} poor grades.")
