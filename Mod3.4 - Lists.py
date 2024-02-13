# This is a program that lists the days and asks the user to input
# the amount of steps they've taken on that day, which are then totaled
# and averaged, then displayed

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
steps = []
total_steps = 0

for day in days:
    steps_temp = int(input(f'How many steps did you take on {day}? '))
    steps.append(steps_temp)
    total_steps = steps_temp + total_steps

print("Here is how many steps you took each day:")
for i in range(0, len(days)):
    print(f'{days[i]}: {steps[i]}')

average = round(total_steps / len(steps))

print(f'Total steps taken this week: {total_steps}')
print(f'Average steps per day: {average}')
