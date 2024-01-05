# Input

n1 = int(input())
n2 = int(input())
operator = input()

result = 0

# Logic

if operator == '+':
    result = n1 + n2

elif operator == '-':
    result = n1 - n2

elif operator == '*':
    result = n1 * n2

elif n2 == 0:
    print(f"Cannot divide {n1} by zero")

elif operator == '/':
    result = n1 / n2

elif operator == '%':
    result = n1 % n2

# Output

if operator == '+' or operator == '-' or operator == '*':
    print(f'{n1} {operator} {n2} = {result}' + (' - even' if result % 2 == 0 else' - odd'))

elif operator == '/' and n2 != 0:
    print(f"{n1} / {n2} = {result:.2f}")

elif operator == '%' and n2 != 0:
    print(f"{n1} % {n2} = {result}")
