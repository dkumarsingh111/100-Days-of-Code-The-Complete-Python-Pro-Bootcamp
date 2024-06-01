import turtle
import pandas

DEFAULT_PATH = "d:/Deepak/100-Days-of-Code-The-Complete-Python-Pro-Bootcamp/Day-25"


screen = turtle.Screen()
screen.title("U.S. States Game")
image = f"{DEFAULT_PATH}/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
guessed_states = []

data = pandas.read_csv(f"{DEFAULT_PATH}/50_states.csv")
all_states = data.state.to_list()

while len(guessed_states) < 50:

    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", 
                                    prompt="what's another state's name?").title()

    
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("./missed_states.csv")
        break
    
    if answer_state in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())
        guessed_states.append(state_data.state.item())







# def get_mouse_click_coor(x, y):
#     print(x, y)


# turtle.onscreenclick(get_mouse_click_coor)
#turtle.mainloop()