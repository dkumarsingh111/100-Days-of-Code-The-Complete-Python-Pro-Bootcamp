from turtle import Turtle, Screen

timmy_the_turtle = Turtle()
screen = Screen()


for _ in range(15):
    timmy_the_turtle.forward(10)
    timmy_the_turtle.penup()
    timmy_the_turtle.forward(10)
    timmy_the_turtle.pendown()

screen.exitonclick()