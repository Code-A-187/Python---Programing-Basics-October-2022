# Input
film_budget = float(input())
extra = int(input())
cloths_price = float(input()) * extra

# Logic

if extra > 150:
    cloths_price *= 0.9

decor = film_budget * 0.1

extra_budget = cloths_price + decor

# Output

if extra_budget > film_budget:
    print(f'{"Not enough money!"}')
    print(f'Wingard needs {extra_budget - film_budget:.2f} leva more.')

else:
    print("Action!")
    print(f"Wingard starts filming with {film_budget - extra_budget:.2f} leva left.")
