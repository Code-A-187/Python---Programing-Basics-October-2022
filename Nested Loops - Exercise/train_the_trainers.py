# Input
judges = int(input())

judges_grades = 0
all_grades = 0

# Logic

while True:
    presentation_name = input()

    if presentation_name == 'Finish':
        break

    grades_sum = 0

    for i in range(judges):
        grades_sum += float(input())

    judges_grades += judges
    all_grades += grades_sum

    print(f'{presentation_name} - {grades_sum / judges:.2f}.')

print(f"Student's final assessment is {all_grades / judges_grades:.2f}.")
