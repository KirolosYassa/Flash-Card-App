from tkinter import *
import pandas
from get_item import *

BACKGROUND_COLOR = "#B1DDC6"
LANG_FONT = ("Arial", 40, "italic")
FONT = ("Arial", 60, "bold")

STATUS = "fr"
timer = 0

def flip_card(fr=True, lang_word=""):
    canvas.delete('all')
    if fr:
        canvas_image = canvas.create_image(400, 300, image=fr_img_file)
        canvas.create_text(400, 175, text="french", font=LANG_FONT)
        canvas.create_text(400, 300, text=f"{lang_word}", font=FONT)
    else:
        global STATUS
        STATUS = "en"
        canvas_image = canvas.create_image(400, 300, image=en_img_file)
        canvas.create_text(400, 175, text="english", font=LANG_FONT)
        canvas.create_text(400, 300, text=f"{lang_word}", font=FONT)

    
# print(get_item())
# print(get_item(en="to play"))
# print(get_item(fr="fin"))

def check_fr(fr_word):
    get_item(fr=fr_word)


def start():
    global STATUS
    STATUS = "fr"
    fr_word = get_item()
    flip_card(lang_word=fr_word)
    global timer
    timer = window.after(3000, flip_card, False,get_item(fr=fr_word))

def wrong_action():
    global STATUS
    if STATUS == "fr":
        window.after_cancel(timer)
    start()

def right_action():
    global STATUS
    if STATUS == "fr":
        window.after_cancel(timer)
    start()


window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
canvas = Canvas(width=800, height=563, bg=BACKGROUND_COLOR, highlightthickness=0)

fr_img_file = PhotoImage(file="./images/card_front.png")
en_img_file = PhotoImage(file="./images/card_back.png")
canvas_image = canvas.create_image(400, 300, image=fr_img_file)
lang = canvas.create_text(400, 175, text="french", font=LANG_FONT)
word = canvas.create_text(400, 300, text="word", font=FONT)
canvas.grid(row = 0, column = 0, columnspan=2)

wrong_img = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, borderwidth=0, command=wrong_action, padx=50, pady=50)
wrong_button.grid(row = 1, column= 0)

right_img = PhotoImage(file="./images/right.png")
right_button = Button(image=right_img, highlightthickness=0,  borderwidth=0, command=right_action, padx=50, pady=50)
right_button.grid(row = 1, column= 1)

start()

window.mainloop()