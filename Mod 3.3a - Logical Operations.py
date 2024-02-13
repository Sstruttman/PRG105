# This program is meant to demonstrate the use of the operators and, or, not

x = int(input("Enter an integer: "))
y = int(input("Enter another integer: "))

# Statements using and

z = x > 50 and y > 50
print(f'Both numbers are greater than 50: {z}')

z = x < 50 and y < 50
print(f'Both numbers are less than 50: {z}')

# Statements using or

z = x % 2 == 0 or y % 2 == 0
print(f'Either number is even: {z}')

z = x > 1000 or y > 1000
print(f'Either number is greater than 1000: {z}')

# Statements using not

if not x == 0:
    print("Number 1 is not 0: True")

else:
    print("Number 1 is not 0: False")

if not x == y:
    print("Number 1 is not Number 2: True")

else:
    print("Number 1 is not Number 2: False")
