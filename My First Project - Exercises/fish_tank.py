# User Input
length = int(input())
width = int(input())
high = int(input())
percent = float(input()) / 100

# Logic
volume = length * width * high
volume_litres = volume / 1000
volume_litres -= volume_litres * percent

# Print
print(volume_litres)
