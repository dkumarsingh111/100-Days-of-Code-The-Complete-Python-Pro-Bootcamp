target = int(input("Enter a number between 2 and 1000: ")) 

sumOfEvenNum = 0

for number in range(2, target+1, 2):
    sumOfEvenNum += number

print(sumOfEvenNum)    