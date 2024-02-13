# This is a program that lists the days and asks the user to input
# the amount of steps they've taken on that day, which are then totaled
# and averaged, then displayed

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
steps = []
total_steps = 0

# Receive input from user on steps taken for each day of the week
# while also utilizing for loop to get total steps as well

for day in days:
    steps_temp = int(input(f'How many steps did you take on {day}? '))
    steps.append(steps_temp)
    total_steps = steps_temp + total_steps

# Calculate average and display steps taken on each day and total

average = round(total_steps / len(steps))


print("Here is how many steps you took each day:")
for i in range(0, len(days)):
    print(f'{days[i]}: {steps[i]}')

print(f'Total steps taken this week: {total_steps}')
print(f'Average steps per day: {average}')
