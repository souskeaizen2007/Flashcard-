import random
from tkinter import *

import pandas
BACKGROUND_COLOR = "#B1DDC6"
words={}
try:
    data = pandas.read_csv("words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("french_words.csv")
    words=original_data.to_dict(orient="records")
else:
    words = data.to_dict(orient="records")
current_card={}

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(words)
    canvas.itemconfig(card_title, text="French",fill="black")
    canvas.itemconfig(card_word, text=current_card["French"],fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer=window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)

def is_known():
    words.remove(current_card)
    rm_data = pandas.DataFrame(words)
    rm_data.to_csv("words_to_learn.csv", index=False)
    next_card()


window = Tk()
window.title("French Flash Card App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer=window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="card_front.png")
card_back_img=PhotoImage(file="card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title=canvas.create_text(400, 100, text="", font=("Arial", 40, "italic"))
card_word=canvas.create_text(400, 263, text="",font=("Arial", 50, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=3)

cross_image=PhotoImage(file="wrong.png")
cross_button=Button(image=cross_image, highlightthickness=0, command=next_card)
cross_button.grid(column=0, row=2)

tick_image=PhotoImage(file="right.png")
tick_button=Button(image=tick_image, highlightthickness=0, command=is_known)
tick_button.grid(column=2, row=2)

next_card()

window.mainloop()