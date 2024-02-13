# This is code to see if the user passes multiple age checks

age = int(input("What is your age? "))

# Check age against multiple constants and print whether user is allowed to do various activities
if age < 16:
    exit("You are not allowed to do anything. Sorry!")

if age >= 16:
    print("You are old enough to drive!")

if age >= 18:
    print("You are old enough to vote!")

else:
    print("You are not old enough to vote. Sorry!")

if age >= 21:
    print("You are old enough to buy alcohol!")

else:
    print("You are not old enough to purchase alcohol!")

if age >= 65:
    print("You are old enough to receive a senior discount!")

else:
    print("You are not old enough to receive a senior discount!")
