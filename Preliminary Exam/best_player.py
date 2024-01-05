# Input

player_name = input()

best_scorer = ''

most_goals = 0

while True:
    if player_name == "END":
        break

    goals = int(input())

    if goals > most_goals:
        most_goals = goals
        best_scorer = player_name

    if most_goals >= 10:
        break
    player_name = input()

print(f"{best_scorer} is the best player!")

if most_goals >= 3:
    print(f"He has scored {most_goals} goals and made a hat-trick !!!")
else:
    print(f"He has scored {most_goals} goals.")
