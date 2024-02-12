# This program is meant to take various household expenditures and calculate the percentages each takes up in a budget
# and displays them

# First, prompt the user to enter their budget and how much they spend in each section
total_budget = float(input("What is your yearly budget? "))
housing = float(input("How much is spent on housing? "))
utilities = float(input("How much is spent on utilities? "))
groceries = float(input("How much is spent on groceries? "))
transportation = float(input("How much is spent on transportation? "))
healthcare = float(input("How much is spent on health care? "))
personalcare = float(input("How much do you spend on personal care? "))
clothing = float(input("How much do you spend on clothing? "))
debt = float(input("How much do you spend debt? "))

# Calculate using expenditure / total_budget = expenditure_percent
housing_percent = (housing / total_budget) * 100
utilities_percent = (utilities / total_budget) * 100
groceries_percent = (groceries / total_budget) * 100
transportation_percent = (transportation / total_budget) * 100
healthcare_percent = (healthcare / total_budget) * 100
personalcare_percent = (personalcare / total_budget) * 100
clothing_percent = (clothing / total_budget) * 100
debt_percent = (debt / total_budget) * 100

# Print each expenditure percent and format using .2f
print(f'the percentage of the total budget taken up by each expenditure is displayed below')
print(f'Housing: {housing_percent:.2f}%')
print(f'Utilities: {utilities_percent:.2f}%')
print(f'Groceries: {groceries_percent:.2f}%')
print(f'Transportation: {transportation_percent:.2f}%')
print(f'Health Care: {healthcare_percent:.2f}%')
print(f'Personal Care: {personalcare:.2f}%')
print(f'Clothing: {clothing_percent:.2f}%')
print(f'Debt: {debt_percent:.2f}%')
