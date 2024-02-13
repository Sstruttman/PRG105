# This program is meant to take a number grade and return a letter grade

# Accept input from user in order to get number grade

grade = int(input("What is the number grade you received? "))

# Use if and elif statement to determine grade

if grade >= 90:
    print("Congratulations! You got an A!")

elif grade >= 80:
    print("Congratulations! You got a B!")

elif grade >= 70:
    print("Congratulations! You got a C!")

elif grade >= 60:
    print("Congratulations! You got a D!")

else:
    print("Oh no! You got an F! You got it next time!")
