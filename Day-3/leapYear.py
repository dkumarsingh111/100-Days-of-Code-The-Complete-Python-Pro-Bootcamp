year = int(input("Enter Year: "))

if(year % 4 == 0):
    if(year % 100 == 0):
        if(year % 400 == 0):
            print("Leap year")
        else:
            print("Not leap year")
    else:
        print("Leap year")
else:
    print("Not leap year")


print(year % 100)