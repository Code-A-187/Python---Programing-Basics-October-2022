# Input

moves_num = int(input())

final_score = 0

score_nine = 0
score_nineteen = 0
score_twenty_nine = 0
score_thirty_nine = 0
score_fifty = 0
invalid_numbers = 0

# Logic

for i in range(moves_num):
    num = int(input())
    if num > 50 or num < 0:
        invalid_numbers += 1
        final_score /= 2
    elif num >= 40:
        score_fifty += 1
        final_score += 100
    elif num >= 30:
        score_thirty_nine += 1
        final_score += 50
    elif num >= 20:
        score_twenty_nine += 1
        final_score += num * 0.4
    elif num >= 10:
        score_nineteen += 1
        final_score += num * 0.3
    elif num >= 0:
        score_nine += 1
        final_score += num * 0.2
# Output

print(f"{final_score:.2f}")
print(f"From 0 to 9: {score_nine / moves_num * 100:.2f}%")
print(f"From 10 to 19: {score_nineteen / moves_num * 100:.2f}%")
print(f"From 20 to 29: {score_twenty_nine / moves_num * 100:.2f}%")
print(f"From 30 to 39: {score_thirty_nine / moves_num * 100:.2f}%")
print(f"From 40 to 50: {score_fifty / moves_num * 100:.2f}%")
print(f"Invalid numbers: {invalid_numbers / moves_num * 100:.2f}%")
