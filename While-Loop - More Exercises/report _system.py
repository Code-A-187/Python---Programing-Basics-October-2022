# Input

charity = int(input())

payments_count = 0

cash_count = 0
cash_payment = 0
card_count = 0
card_payment = 0
counter = 0

# Logic

while charity > payments_count:
    stop = input()
    if stop == "End":
        print("Failed to collect required money for charity.")
        break
    else:
        payment = int(stop)
        counter += 1
        if counter % 2 == 1:
            if payment > 100:
                print("Error in transaction!")
                continue
            else:
                cash_count += 1
                cash_payment += payment
                payments_count += payment
                print('Product sold!')
                continue
        else:
            if payment < 10:
                print("Error in transaction!")
                continue
            else:
                card_count += 1
                card_payment += payment
                payments_count += payment
                print('Product sold!')
                continue
else:
    print(f'Average CS: {cash_payment / cash_count:.2f}')
    print(f'Average CC: {card_payment / card_count:.2f}')
