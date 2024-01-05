# User Input
deposit = float(input())
deposit_term = int(input())
annual_interest_rate = float(input()) / 100
# Logic
sum_deposit = deposit + deposit_term * ((deposit * annual_interest_rate) / 12)
# Print
print(sum_deposit)
