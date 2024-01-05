# Input

vegetables_price = float(input())
fruits_price = float(input())
kg_vegetables = int(input())
kg_fruits = int(input())

# Logic

turnover = (vegetables_price * kg_vegetables) + (fruits_price * kg_fruits)

# Output

print(f'{turnover / 1.94:.2f}')
