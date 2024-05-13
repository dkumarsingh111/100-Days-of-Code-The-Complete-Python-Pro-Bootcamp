print("Thank you for choosing Python pizza deliveries!")

bill = 0

size = input("What size pizza do you want? S, M, or L: ")

add_pepperoni = input("Do you want papperoni? Y or N: ")

extra_cheese = input("Do you want extra cheese? Y or N: ")

if(size == 'S'):
    bill += 15
    if(add_pepperoni == 'Y'):
        bill += 2
elif(size == 'M'):
    bill += 20
    if(add_pepperoni == 'Y'):
        bill += 3
elif(size == 'L'):
    bill += 25
    if(add_pepperoni == 'Y'):
        bill += 3


if(extra_cheese == 'Y'):
    bill += 1


print(f"Thank you for choosing Python pizza deliveries!\n Your final bill is: ${bill}.")