# Input

fuel = input()
volume = float(input())
card_verification = input()

price = 0

gasoline = 2.22
diesel = 2.33
gas = 0.93


# Logic

if fuel == 'Gasoline':
    if card_verification == 'Yes':
        gasoline = gasoline - 0.18
    else:
        gasoline = gasoline
    if volume > 25:
        price = volume * (gasoline * 0.90)
    elif volume > 20:
        price = volume * (gasoline * 0.92)
    else:
        price = volume * gasoline

elif fuel == 'Diesel':
    if card_verification == 'Yes':
        diesel = diesel - 0.12
    else:
        diesel = diesel
    if volume > 25:
        price = volume * (diesel * 0.90)
    elif volume > 20:
        price = volume * (diesel * 0.92)
    else:
        price = volume * diesel

elif fuel == 'Gas':
    if card_verification == 'Yes':
        gas = gas - 0.08
    else:
        gas = gas
    if volume > 25:
        price = volume * (gas * 0.90)
    elif volume > 20:
        price = volume * (gas * 0.92)
    else:
        price = volume * gas

# Output

print(f'{price:.2f} lv.')
