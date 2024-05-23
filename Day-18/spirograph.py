import turtle
from random import choice, randint

timmy_the_turtle = turtle.Turtle()
screen = turtle.Screen()
turtle.colormode(255)
#timmy_the_turtle.speed("fastest")


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return (r, g, b)

degree = int(input("Enter spiral degree: "))
for _ in range(int(360 / degree)):
    
    timmy_the_turtle.color(random_color())
    timmy_the_turtle.circle(100)
    timmy_the_turtle.setheading(timmy_the_turtle.heading() + degree)


screen.exitonclick()    
