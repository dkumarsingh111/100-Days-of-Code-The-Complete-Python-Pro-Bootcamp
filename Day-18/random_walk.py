from turtle import Turtle, Screen
from random import choice

timmy_the_turtle = Turtle()
screen = Screen()
colors = ['CornflowerBlue', 'DarkOrchid', 'IndianRed', 'DeepSkyBlue', 'LightSeaGreen', 'wheat', 'SeaGreen', 'cyan', 'green', 'yellow green', 'chocolate', 'pale goldenrod', 'gold', 'dark cyan', 'pale green']
directions = [0, 90, 180, 270]


for _ in range(200):
    timmy_the_turtle.color(choice(colors))
    timmy_the_turtle.pensize(10)
    timmy_the_turtle.forward(30)
    timmy_the_turtle.setheading(choice(directions))
