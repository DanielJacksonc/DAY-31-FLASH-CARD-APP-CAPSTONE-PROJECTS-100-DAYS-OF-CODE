from tkinter import *
import pandas as pd
import random


BACKGROUND = "#B1DDC6"
to_learn = {}
current_card = {}


try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:

    to_learn = data.to_dict(orient="records")




def next_card():
    global current_card, flip_timer
    canvas.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"],fill="black")
    canvas.itemconfig(background, image=front_image)
    flip_timer = window.after(3000, func=flip_card)
def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(background, image=back_image )


def known_card():
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pd.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()

window = Tk()
window.title("The Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND)

flip_timer = window.after(3000, func=flip_card)


canvas = Canvas(width=800,height=526,  bg=BACKGROUND, highlightthickness=0)
front_image = PhotoImage(file= "./images/card_front.png")
back_image = PhotoImage(file= "./images/card_back.png")
background = canvas.create_image(400, 263, image=front_image)
canvas.grid(row=0, column=0, columnspan=2)
card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))


""" we will have a wrong button and a right button"""

wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, bg=BACKGROUND, command=next_card)
wrong_button.grid(row=1, column=0)

right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, highlightthickness=0, bg=BACKGROUND, command=known_card)
right_button.grid(row=1, column=1)

"""We will have a label """
next_card()








window.mainloop()

#
# from tkinter import *
# import pandas as pd
# import random
# import pandas
# import time
#
# BACKGROUND = "#B1DDC6"
#
# data = pd.read_csv("data/french_words.csv")
# to_learn = data.to_dict(orient="records")
#
#
#
#
# current_card = {}
# def next_card():
#     global current_card, flip_timer
#     canvas.after_cancel(flip_timer)
#     current_card = random.choice(to_learn)
#     canvas.itemconfig(card_title, text="French", fill="black")
#     canvas.itemconfig(card_word, text=current_card["French"],fill="black")
#     canvas.itemconfig(background, image=front_image)
#     flip_timer = window.after(3000, func=flip_card)
#
# def flip_card():
#     canvas.itemconfig(card_title, text="English", fill="white")
#     canvas.itemconfig(card_word, text=current_card["English"], fill="white")
#     canvas.itemconfig(background, image=back_image )
# def known_card():
#     to_learn.remove(current_card)
#
#
#
#
#
#
#
#
#
# window = Tk()
# window.title("The Flash Card")
# window.config(padx=50, pady=50, bg=BACKGROUND)
#
# flip_timer = window.after(3000, func=flip_card)
#
#
# canvas = Canvas(width=800,height=526,  bg=BACKGROUND, highlightthickness=0)
# front_image = PhotoImage(file= "./images/card_front.png")
# back_image = PhotoImage(file= "./images/card_back.png")
# background = canvas.create_image(400, 263, image=front_image)
# canvas.grid(row=0, column=0, columnspan=2)
# card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
# card_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
#
#
# """ we will have a wrong button and a wright button"""
#
# wrong_image = PhotoImage(file="./images/wrong.png")
# wrong_button = Button(image=wrong_image, highlightthickness=0, bg=BACKGROUND,command = next_card)
# wrong_button.grid(row=1, column=0)
#
# right_image = PhotoImage(file="./images/right.png")
# right_button = Button(image=right_image, highlightthickness=0, bg=BACKGROUND, command=known_card)
# right_button.grid(row=1, column=1)
#
# """We will have a label """
# if right_button in to_learn:
#     to_learn.remove(current_card)
# if wi
# next_card()
#
#
#
#
#
#
#
#
# window.mainloop()

