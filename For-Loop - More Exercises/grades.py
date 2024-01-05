# Input

students_num = int(input())

top_grade = 0
four_grade = 0
three_grade = 0
fail_grade = 0

average_grade = 0

# Logic

for i in range(students_num):
    grade = float(input())
    average_grade += grade
    if grade >= 5:
        top_grade += 1
    elif grade >= 4:
        four_grade += 1
    elif grade >= 3:
        three_grade += 1
    else:
        fail_grade += 1

# Output
print(f'Top students: {top_grade /  students_num * 100:.2f}%')
print(f'Between 4.00 and 4.99: {four_grade / students_num * 100:.2f}%')
print(f'Between 3.00 and 3.99: {three_grade / students_num * 100:.2f}%')
print(f'Fail: {fail_grade / students_num * 100:.2f}%')
print(f'Average: {average_grade / students_num:.2f}')
