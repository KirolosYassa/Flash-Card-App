from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
LANG_FONT = ("Arial", 40, "italic")
FONT = ("Arial", 60, "bold")


def wrong_action():
    pass


def right_action():
    pass

window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
canvas = Canvas(width=800, height=563, bg=BACKGROUND_COLOR, highlightthickness=0)
img_file = PhotoImage(file="./images/card_front.png")
canvas.create_image(400, 300, image=img_file)
lang = canvas.create_text(400, 175, text="title", font=LANG_FONT)
word = canvas.create_text(400, 300, text="word", font=FONT)
canvas.grid(row = 0, column = 0, columnspan=2)

wrong_img = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, borderwidth=0, command=wrong_action, padx=50, pady=50)
wrong_button.grid(row = 1, column= 0)

right_img = PhotoImage(file="./images/right.png")
right_button = Button(image=right_img, highlightthickness=0,  borderwidth=0, command=right_action, padx=50, pady=50)
right_button.grid(row = 1, column= 1)


window.mainloop()