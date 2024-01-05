from math import ceil, floor
# Input

days = int(input())
total_food = int(input())

dog_eat = float(input()) * days
cat_eat = float(input()) * days
turtle_eat = (float(input()) * days) / 1000

# Logic

food_eaten = dog_eat + cat_eat + turtle_eat

# Output

if food_eaten > total_food:
    print(f'{ceil(food_eaten - total_food)} more kilos of food are needed.')
else:
    print(f'{floor(total_food - food_eaten)} kilos of food left.')
