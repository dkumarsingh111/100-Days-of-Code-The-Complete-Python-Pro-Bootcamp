import turtle
from random import choice, randint

timmy_the_turtle = turtle.Turtle()
screen = turtle.Screen()
turtle.colormode(255)

def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return (r, g, b)


directions = [0, 90, 180, 270]
timmy_the_turtle.pensize(10)
timmy_the_turtle.speed("fastest")

for _ in range(200):
    timmy_the_turtle.color(random_color())
    timmy_the_turtle.forward(30)
    timmy_the_turtle.setheading(choice(directions))


screen.exitonclick()    
