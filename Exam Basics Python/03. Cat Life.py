
from math import floor
# Input

cat_type = input()
gender = input()

years = 0


# Logic

if cat_type == "British Shorthair":
    if gender == "m":
        years = 13
    else:
        years = 14
elif cat_type == "Siamese":
    if gender == "m":
        years = 15
    else:
        years = 16
elif cat_type == "Persian":
    if gender == "m":
        years = 14
    else:
        years = 15
elif cat_type == "Ragdoll":
    if gender == "m":
        years = 16
    else:
        years = 17
elif cat_type == "American Shorthair":
    if gender == "m":
        years = 12
    else:
        years = 13
elif cat_type == "Siberian":
    if gender == "m":
        years = 11
    else:
        years = 12

cat_years = years * 12

if cat_type == "British Shorthair" or \
    cat_type == "Siamese" or \
    cat_type == "Persian" or \
    cat_type == "Ragdoll" or \
    cat_type == "American Shorthair" or \
    cat_type == "Siberian":
    print(f"{floor(cat_years / 6)} cat months")

else:
    print(f'{cat_type} is invalid cat!')



