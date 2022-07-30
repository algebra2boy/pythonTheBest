from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

# -------------------------------  Create Flash Cards----------------------------------------------------------------- #
try: # read the file that contains cards that we have not read yet
    words = pandas.read_csv("data/words_to_learn.csv")  # the class type is DataFrame
except FileNotFoundError:  # read the original file
    original_file = pandas.read_csv("data/french_words.csv")
    to_learn = original_file.to_dict(orient="records")
else:
    to_learn = words.to_dict(orient="records")


def next_card():
    global current_card
    global filp_timer
    window.after_cancel(filp_timer)  # cancel the timer when it got flip to the other side
    current_card = random.choice(to_learn)
    canvas.itemconfig(canva_title, text="French", fill="black")
    canvas.itemconfig(canva_word, text=current_card['French'], fill="black")
    filp_timer = window.after(3000, func=flip_card)  # start the timer once the card is flip

def flip_card():
    canvas.itemconfig(canva_title, text="English",fill="white")
    canvas.itemconfig(canva_word, text=current_card['English'],fill="white")
    canvas.itemconfig(card_background, image=card_back_img)

def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()

# -------------------------------   Window Set Up----------------------------------------------------------------- #
window = Tk()
window.title("flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

filp_timer = window.after(3000, func=flip_card)

canvas = Canvas(height=526, width=800)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400,263, image=card_front_img)
canva_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
canva_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0) # highlightthickness is to get rid of the highlight thickness
canvas.grid(row=0,column=0, columnspan=2)

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image,  highlightthickness=0, command=next_card)
unknown_button.grid(row=1,column=0)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image,  highlightthickness=0, command=is_known)
known_button.grid(row=1,column=1)

next_card()


window.mainloop()
