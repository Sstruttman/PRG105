# This program is meant to demonstrate the bubble sort algorithm

# Receive input from user for list names

names = []
name_temp = 'not_done'
while name_temp != 'done':
    name_temp = str(input("Please enter a name or enter 'Done' to finish. "))
    name_temp = name_temp.lower()
    if name_temp == 'done':
        break
    names.append(name_temp)

# Utilize bubble sort algorithm to swap names around

swapped = True
while swapped:
    swapped = False
    for i in range(len(names) - 1):
        if names[i] > names[i + 1]:
            swapped = True
            names[i], names[i + 1] = names[i + 1], names[i]

# Print sorted list and reversed list

print(names)
names.reverse()
print(names)
