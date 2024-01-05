# Input

months_num = int(input())

electricity = 0
water = 0
internet = 0
others = 0

# Logic
for i in range(months_num):
    bills = float(input())
    electricity += bills
    water += 20
    internet += 15
    others += (bills + 20 + 15) * 1.2

average = electricity + water + internet + others

# Output

print(f"Electricity: {electricity:.2f} lv")
print(f"Water: {water:.2f} lv")
print(f"Internet: {internet:.2f} lv")
print(f"Other: {others:.2f} lv")
print(f"Average: {average / months_num:.2f} lv")
