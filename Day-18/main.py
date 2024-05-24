import turtle as turtle_module
from random import randint

def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return (r, g, b)

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fast")
tim.penup()
tim.hideturtle()
screen = turtle_module.Screen()

tim.setheading(225)
tim.forward(300)
tim.setheading(0)

no_of_dots = 100

for dot_count in range(1, no_of_dots+1):
    tim.dot(20, random_color())
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen.exitonclick()
