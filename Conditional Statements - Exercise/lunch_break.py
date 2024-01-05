# Input
import math

series_name = input()
episode_time = int(input())
lunch_break = int(input())

lunch_time = lunch_break * 1/8

rest_time = lunch_break * 1/4

# Logic

remaining_time = lunch_break - (lunch_time + rest_time)

# Output

if remaining_time >= episode_time:
    print(f"You have enough time to watch {series_name} and left with {math.ceil(remaining_time - episode_time)} minutes free time.")

else:
    print(f"You don't have enough time to watch {series_name}, you need {math.ceil(episode_time - remaining_time)} more minutes.")
