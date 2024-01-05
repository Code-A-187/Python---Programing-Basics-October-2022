# Input

num = int(input())

student_5 = 0
student_4 = 0
student_3 = 0
student_2 = 0

grades_sum = 0

# Logic

for _ in range(num):
    grade = float(input())
    grades_sum += grade
    if grade >= 5:
        student_5 += 1
    elif grade >= 4:
        student_4 += 1
    elif grade >= 3:
        student_3 += 1
    else:
        student_2 += 1

# Output

print(f"Top students: {student_5 / num * 100:.2f}%")
print(f"Between 4.00 and 4.99: {student_4 / num * 100:.2f}%")
print(f"Between 3.00 and 3.99: {student_3 / num * 100:.2f}%")
print(f"Fail: {student_2 / num * 100:.2f}%")
print(f"Average: {grades_sum / num:.2f}")
