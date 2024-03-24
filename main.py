from tkinter import *
import pandas as pd
from random import *

BACKGROUND = "#B1DDC6"
to_learn = {}
current_card = {}
#------------- CREATE LOGIC -------------#
try:
    Dataframe = pd.read_csv("data/to_learn.csv")
except FileNotFoundError:
    Dataframe = pd.read_csv("data/french_words.csv")
    to_learn = Dataframe.to_dict(orient="records")
else:
    to_learn = Dataframe.to_dict(orient="records")
def cycle_through_cards():
    global current_card, flip_timer
    base.after_cancel(flip_timer)
    current_card = choice(to_learn)
    french_word = current_card["French"]
    C.itemconfig(word, text=french_word, font="Ariel 60 bold", fill="black")
    C.itemconfig(language, text="French", font="Ariel 40 italic", fill="black")
    C.itemconfig(canvas_image, image=card_front_image)
    flip_timer = base.after(3000, flip_card)


def flip_card():
    english_word = current_card["English"]
    C.itemconfig(word, text=english_word, font="Ariel 60 bold", fill="white")
    C.itemconfig(language, text="English", font="Ariel 40 italic", fill="white")
    C.itemconfig(canvas_image, image=card_back_image)


def remove_word():
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv("data/to_learn.csv", index=False)
    cycle_through_cards()

#------------- CREATE CANVAS AND ROOT -------------#
base = Tk()
base.title("Flashy")
base.config(bg=BACKGROUND, padx=50, pady=50)

C = Canvas(base, height=500, width=800)
C.config(bg=BACKGROUND, highlightthickness=0)

card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
canvas_image = C.create_image(400, 250, image=card_front_image)
C.grid(row=0, column=0, sticky=N, columnspan=2)

language = C.create_text(400, 150, text="", font="Ariel 40 italic")
word = C.create_text(400, 330, text="", font="Ariel 60 bold")

flip_timer = base.after(3000, func=flip_card)

#------------- CREATE BUTTONS -------------#
right_image = PhotoImage(file="images/right.png")
button_right = Button(image=right_image, highlightthickness=0, command=remove_word)
button_right.configure(bg=BACKGROUND)
button_right.grid(row=1, column=0)

wrong_image = PhotoImage(file="images/wrong.png")
button_wrong = Button(image=wrong_image, highlightthickness=0, command=cycle_through_cards)
button_wrong.configure(bg=BACKGROUND)
button_wrong.grid(row=1, column=1)

cycle_through_cards()

base.mainloop()