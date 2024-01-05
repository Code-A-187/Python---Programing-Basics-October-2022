# Input

string = input()

string_length = len(string)

result = 0

# Logic

for i in range(0, string_length):
    current_char = string[i]
    if current_char == "a":
        result += 1
    if current_char == "e":
        result += 2
    if current_char == "i":
        result += 3
    if current_char == "o":
        result += 4
    if current_char == "u":
        result += 5

# Print

print(result)
