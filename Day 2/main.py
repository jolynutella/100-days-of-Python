#This program calculates amount of pay per person considering total bill, tip percentage and number of people

print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill?\n$"))
percentage = int(input("What percentage would you like to give? (10, 12, 15 or more)\n%"))
num_people = int(input("How many people to split the bill?\n"))
pay_per_person = round((total_bill * (1 + (percentage / 100)) / num_people), 2)
print(f"Each person should pay: {pay_per_person}$")