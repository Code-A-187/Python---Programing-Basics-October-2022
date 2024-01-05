# Input

bottles = int(input())

detergent = bottles * 750

used_detergent = 0
clean_dishes = 0
clean_pots = 0

count = 1
# Logic

while detergent >= used_detergent:
    stop = input()
    if stop == "End":
        print("Detergent was enough!")
        print(f"{clean_dishes} dishes and {clean_pots} pots were washed.")
        print(f"Leftover detergent {detergent - used_detergent} ml.")
        break
    dishes = int(stop)
    if count % 3 == 0:
        clean_pots += dishes
        used_detergent += dishes * 15
    else:
        clean_dishes += dishes
        used_detergent += dishes * 5
    count += 1
else:
    print(f"Not enough detergent, {used_detergent - detergent} ml. more necessary!")
