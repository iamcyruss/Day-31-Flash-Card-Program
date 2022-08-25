from tkinter import *
from tkinter import messagebox
import pandas
import random


BACKGROUND_COLOR = "#B1DDC6"
current_card = {}

"""
I tried doing the try except but I ran into problems so I did a normal if statement
but the instructor wants us to use the try except.
if open("data/words_to_learn.csv"):
    spanish_words = pandas.read_csv("data/words_to_learn.csv")
    spanish_words_dict = spanish_words.to_dict(orient='records')
elif open("data/spanish_data_set.csv"):
    spanish_words = pandas.read_csv("data/spanish_data_set.csv")
    spanish_words_dict = spanish_words.to_dict(orient='records')
else:
    messagebox.showinfo(title="No input data files found. Please fix input file and rerun this program.")
instructor solution below.
"""
try:
    spanish_words = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_file = pandas.read_csv("data/spanish_data_set.csv")
    spanish_words_dict = original_file.to_dict(orient='records')
else:
    spanish_words_dict = spanish_words.to_dict(orient='records')


def new_word():
    """
    below is the code I made which works. But instructor did it slightly different
    num_in_dict = len(spanish_words_dict) - 1
    card.itemconfig(word_text, text=spanish_words_dict[random.randrange(num_in_dict)]['spanish'])
    """
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(spanish_words_dict)
    card.itemconfig(title_text, text="Spanish", fill="black")
    card.itemconfig(word_text, text=current_card['spanish'], fill="black")
    card.itemconfig(card_background, image=front_card)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    card.itemconfig(card_background, image=back_card)
    card.itemconfig(title_text, text="English", fill="white")
    card.itemconfig(word_text, text=current_card['english'], fill="white")


def know_this():
    spanish_words_dict.remove(current_card)
    pandas_dataframe = pandas.DataFrame(spanish_words_dict)
    pandas_dataframe.to_csv('data/words_to_learn.csv', index=False)
    new_word()


window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

right_button = PhotoImage(file="images/right.png")
wrong_button = PhotoImage(file="images/wrong.png")
front_card = PhotoImage(file="images/card_front.png")
back_card = PhotoImage(file="images/card_back.png")

card = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_background = card.create_image(400, 263, image=front_card)
card.grid(column=0, row=0, columnspan=2, rowspan=2)

title_text = card.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word_text = card.create_text(400, 263, text="", font=("Ariel", 60, "bold"))


wrong = Button(image=wrong_button, highlightthickness=0, command=new_word)
wrong.grid(column=0, row=3)
right = Button(image=right_button, highlightthickness=0, command=know_this)
right.grid(column=1, row=3)



new_word()
window.mainloop()
