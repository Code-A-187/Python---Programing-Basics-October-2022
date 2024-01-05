# Input

days = int(input())

doctors = 7
examined_patients = 0
unexamined_patients = 0

# Logic
for i in range(1, days + 1):
    patients = int(input())

    if i % 3 == 0 and unexamined_patients > examined_patients:
        doctors += 1

    if patients > doctors:
        examined_patients += doctors
        unexamined_patients += patients - doctors
    else:
        examined_patients += patients

# Output

print(f'Treated patients: {examined_patients}.')
print(f'Untreated patients: {unexamined_patients}.')
