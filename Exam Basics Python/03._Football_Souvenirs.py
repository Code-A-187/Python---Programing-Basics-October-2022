club_name = input()
souvenirs = input()
zet_souvenirs = int(input())

price = 0
country = True
stock = True

if club_name == "Argentina":
    if souvenirs == "flags":
        price = zet_souvenirs * 3.25
    elif souvenirs == "caps":
        price = zet_souvenirs * 7.20
    elif souvenirs == "posters":
        price = zet_souvenirs * 5.10
    elif souvenirs == "stickers":
        price = zet_souvenirs * 1.25
    else:
        stock = False
elif club_name == "Brazil":
    if souvenirs == "flags":
        price = zet_souvenirs * 4.20
    elif souvenirs == "caps":
        price = zet_souvenirs * 8.50
    elif souvenirs == "posters":
        price = zet_souvenirs * 5.35
    elif souvenirs == "stickers":
        price = zet_souvenirs * 1.20
    else:
        stock = False
elif club_name == "Croatia":
    if souvenirs == "flags":
        price = zet_souvenirs * 2.75
    elif souvenirs == "caps":
        price = zet_souvenirs * 6.90
    elif souvenirs == "posters":
        price = zet_souvenirs * 4.95
    elif souvenirs == "stickers":
        price = zet_souvenirs * 1.10
    else:
        stock = False
elif club_name == "Denmark":
    if souvenirs == "flags":
        price = zet_souvenirs * 3.10
    elif souvenirs == "caps":
        price = zet_souvenirs * 6.50
    elif souvenirs == "posters":
        price = zet_souvenirs * 4.80
    elif souvenirs == "stickers":
        price = zet_souvenirs * 0.90
    else:
        stock = False
else:
    country = False

if country == True and stock == True:
    print(f"Pepi bought {zet_souvenirs} {souvenirs} of {club_name} for {price:.2f} lv.")

elif not country:
    print(f'Invalid country!')

else:
    print(f'Invalid stock!')
