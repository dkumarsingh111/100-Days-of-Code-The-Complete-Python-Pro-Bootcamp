import math

def paint_calc(height, width, cover):
    num_cans = (height * width) / cover
    round_up_cans = math.ceil(num_cans)
    print(f"You will need {round_up_cans} cans of paint.")


height = int(input("Height of the wall = "))
width = int(input("Width of the wall = "))
coverage = 5

paint_calc(height, width, coverage)