# Input

pool_volume = int(input())
p1 = int(input())
p2 = int(input())
away_hours = float(input())


# Logic


p1_debit = p1 * away_hours
p2_debit = p2 * away_hours

fullness = p1_debit + p2_debit

if fullness > pool_volume:
    print(f"For {away_hours:.2f} hours the pool overflows with {fullness - pool_volume:.2f} liters.")

else:
    print(f"The pool is {fullness / pool_volume * 100:.2f}% full."
          f" Pipe 1: {p1_debit / fullness * 100:.2f}%. Pipe 2: {p2_debit / fullness * 100:.2f}%.")
