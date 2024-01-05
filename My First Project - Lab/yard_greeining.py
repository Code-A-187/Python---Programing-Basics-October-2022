# Read user input
area = float(input())

# Logic
before_discount = area * 7.61

discount = before_discount * 0.18

total = before_discount - discount

# Print
print(f"The final price is: {total} lv.")

print(f"The discount is: {discount} lv.")
