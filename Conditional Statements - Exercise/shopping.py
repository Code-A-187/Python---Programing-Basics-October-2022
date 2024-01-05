# Input
budget = float(input())

video_card = int(input())
processor = int(input())
ram = int(input())

video_card_price = video_card * 250
processor_price = processor * video_card_price * 0.35
ram_price = ram * video_card_price * 0.1

# Logic

money_needed = video_card_price + processor_price + ram_price

if video_card > processor:
    money_needed *= 0.85

# Output

if budget >= money_needed:
    print(f"You have {budget - money_needed:.2f} leva left!")

else:
    print(f"Not enough money! You need {money_needed - budget:.2f} leva more!")
