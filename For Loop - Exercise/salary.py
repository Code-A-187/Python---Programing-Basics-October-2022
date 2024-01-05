# Input

tabs_count = int(input())
salary = int(input())

# Logic

for _ in range(tabs_count):
    web_site = input()

    if web_site == 'Facebook':
        salary -= 150
    elif web_site == 'Instagram':
        salary -= 100
    elif web_site == 'Reddit':
        salary -= 50

    if salary <= 0:
        print("You have lost your salary.")
        break
else:
    print(salary)
