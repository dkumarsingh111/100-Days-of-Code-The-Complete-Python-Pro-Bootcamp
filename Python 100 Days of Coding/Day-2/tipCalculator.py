print("Welcome to the tip calculator")

billAmount = float(input("What was the total bill? $"))

tip = int(input("How much percent tip would you like to give? "))

noOfPeople = int(input("How many people to split the bill? "))

payableAmount = round((billAmount + (billAmount * tip / 100)) / noOfPeople, 2)

print("Each person should pay: $" + str(payableAmount))