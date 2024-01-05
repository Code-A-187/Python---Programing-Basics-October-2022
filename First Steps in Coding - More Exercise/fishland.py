# Input

skumriq_price = float(input())
caca_price = float(input())
palamud = float(input())
safrid = float(input())
midi = int(input()) * 7.50

# Logic

palamud_price = (skumriq_price * 1.6) * palamud
safrid_price = (caca_price * 1.8) * safrid

total_price = midi + palamud_price + safrid_price

# Output

print(f'{total_price:.2f}')
