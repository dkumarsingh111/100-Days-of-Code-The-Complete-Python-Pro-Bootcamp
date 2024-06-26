from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.title("Turtle Racing Game!")
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-75, -45, -15, 15, 45, 75]
all_turtles = []

for turtle_index in range(0, len(colors)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-240, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                screen.title(f"You've won! The {winning_color} turtle is the winner!")
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                screen.title(f"You've lost! The {winning_color} turtle is the winner!")
                print(f"You've lost! The {winning_color} turtle is the winner!")
        
        random_distance = random.randint(0,2)
        turtle.forward(random_distance)

screen.exitonclick()