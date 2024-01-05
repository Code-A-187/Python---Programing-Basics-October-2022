#read user input
dogs_food = int(input())
cats_food = int(input())

#logic
dogs_total = dogs_food * 2.5
cats_total = cats_food * 4
total_price = dogs_total + cats_total

# print output
print(f'{total_price} lv.')