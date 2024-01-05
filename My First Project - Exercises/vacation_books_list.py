# User Input
pages = int(input())
pages_for_hour = int(input())
days = int(input())

# Logic
total_reading_hours = pages / pages_for_hour
hours_per_day = (total_reading_hours / days)

# Print
print(round(hours_per_day))
