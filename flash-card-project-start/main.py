from tkinter import *
import pandas
import random
from tkinter import messagebox

TIMER = None
BACKGROUND_COLOR = "#B1DDC6"

#   -------DATA MANAGEMENT--------- #
try:
    data = pandas.read_csv("data/words_to_learn.csv")

except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")


to_learn = data.to_dict(orient="records")

current_card = {}


def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)

    next_card()


def next_card():
    global current_card
    global flip_timer

    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(canvas_image, image=front_image)
    flip_timer = window.after(3000, func=flip_card)


#   --------FLIP IMAGE----------    #
def flip_card():
    global user_knows
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(canvas_image, image=back_image)


#   ---------UI SETUP-----------    #
window = Tk()
window.title("Flash Card")
window.configure(bg=BACKGROUND_COLOR, padx=50, pady=50)
flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(410, 273, image=front_image)
canvas.grid(row=0, column=0, columnspan=2)


card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"), tags="value")


right_button_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_button_img, highlightthickness=0, width=100, command=is_known)
right_button.grid(row=1, column=1, sticky=E)

wrong_button_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_button_img, highlightthickness=0, width=100, command=next_card)
wrong_button.grid(row=1, column=0, sticky=W)

next_card()

window.mainloop()
