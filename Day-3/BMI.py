height = float(input("Enter your height in meters = "))
weight = float(input("Enter your weight in KG = "))


bmi = round(weight / (height ** 2), 2)

if(bmi <= 18.5):
    print(f"Your BMI is {bmi}, you are underweight.\n")
elif(bmi > 18.5 and bmi <= 25):
    print(f"Your BMI is {bmi}, you have a normal weight.\n")    
elif(bmi > 25 and bmi <= 30):
    print(f"Your BMI is {bmi}, you are slightly overweight.\n")  
elif(bmi > 30 and bmi <= 35):
    print(f"Your BMI is {bmi}, you are obese.\n")  
else:
    print(f"Your BMI is {bmi}, you are critically obese.\n")  