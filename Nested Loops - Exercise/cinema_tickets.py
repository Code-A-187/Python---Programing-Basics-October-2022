# Input
student_tickets, standard_tickets, kids_tickets =0, 0, 0

# Logic

while True:
    film_name = input()
    if film_name == "Finish":
        break

    capacity = int(input())
    sold_tickets = 0

    while sold_tickets < capacity:
        type_of_ticket = input()

        if type_of_ticket == "End":
           break

        if type_of_ticket == 'student':
            student_tickets += +1

        elif type_of_ticket == 'standard':
             standard_tickets+= 1

        else:
             kids_tickets += 1

        sold_tickets += 1

    print(f'{film_name} - {sold_tickets / capacity * 100:.2f}% full.')

total_tickets = standard_tickets + student_tickets +kids_tickets

# Output
print(f"Total tickets: {total_tickets}")
print(f"{student_tickets / total_tickets * 100:.2f}% student tickets.")
print(f"{standard_tickets / total_tickets * 100:.2f}% standard tickets.")
print(f"{kids_tickets / total_tickets * 100:.2f}% kids tickets.")
