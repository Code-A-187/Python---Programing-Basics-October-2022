# Input

under_sixteen = 0
above_sixteen = 0

# Logic

while True:
    end = input()
    if end == "Christmas":
        print(f"Number of adults: {above_sixteen}")
        print(f"Number of kids: {under_sixteen}")
        print(f"Money for toys: {under_sixteen * 5:.0f}")
        print(f"Money for sweaters: {above_sixteen * 15:.0f}")
        break
    else:
        age = int(end)
    if age > 16:
        above_sixteen += 1
    else:
        under_sixteen += 1
