from turtle import Turtle, Screen
from random import choice

timmy_the_turtle = Turtle()
screen = Screen()
colors = ['cyan', 'green', 'yellow green', 'chocolate', 'pale goldenrod', 'gold', 'dark cyan', 'pale green']

def draw_shapes(no_of_sides):
    for sides in range(no_of_sides):
        timmy_the_turtle.color(choice(colors))
        angle = sides+3
        for _ in range(angle):
            timmy_the_turtle.right(360 / angle)
            timmy_the_turtle.forward(100)


sides = int(input("Number of sides do you want to print: "))

draw_shapes(sides)

screen.exitonclick()