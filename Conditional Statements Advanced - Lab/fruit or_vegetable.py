# Input

product = input()

# Logic

if product == "banana" or \
        product == "kiwi" or\
        product == "apple" or \
        product == "cherry" or \
        product == "lemon" or \
        product == 'grapes':
    print("fruit")

elif product == "tomato" or \
        product == "cucumber" or \
        product == "pepper" or \
        product == "carrot":
    print("vegetable")

else:
    print("unknown")
