fruits = eval(input())

def make_pie(index):
    try:
        fruit = fruits[index]
        print(fruit + " Pie")
    except:
        print("Fruit Pie")


make_pie(4)