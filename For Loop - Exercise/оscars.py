TRES_HOLD = 1250.5

# Input

act_name = input()
points = float(input())
judge_count = int(input())

# Logic

for _ in range(judge_count):
    judge_name = input()
    judge_points = float(input())

    points += len(judge_name) * judge_points / 2

    if points > TRES_HOLD:
        print(f"Congratulations, {act_name} got a nominee for leading role with {points:.1f}!")
        break
else:
    print(f"Sorry, {act_name} you need {TRES_HOLD - points:.1f} more!")
