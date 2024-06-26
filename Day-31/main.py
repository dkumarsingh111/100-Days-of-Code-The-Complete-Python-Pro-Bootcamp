from tkinter import *
import pandas as pd
import random


FILE_PATH="c:/Users/100-Days-of-Code-The-Complete-Python-Pro-Bootcamp/Day-31"
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}


try:
    data = pd.read_csv(f"{FILE_PATH}/data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv(f"{FILE_PATH}/data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)

    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


def is_known():
    to_learn.remove(current_card)

    data = pd.DataFrame(to_learn)
    data.to_csv(f"{FILE_PATH}/data/words_to_learn.csv", index=False)

    next_card()


window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


flip_timer = window.after(3000, func=flip_card)


canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file=f"{FILE_PATH}/images/card_front.png")
card_back_img = PhotoImage(file=f"{FILE_PATH}/images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)


cross_img = PhotoImage(file=f"{FILE_PATH}/images/wrong.png")
wrong_btn = Button(image=cross_img, highlightthickness=0, command=next_card)
wrong_btn.grid(row=1, column=0)

tick_img = PhotoImage(file=f"{FILE_PATH}/images/right.png")
right_btn = Button(image=tick_img, highlightthickness=0, command=is_known)
right_btn.grid(row=1, column=1)


next_card()


window.mainloop()