from tkinter import *
# import pandas
from data import *

BACKGROUND_COLOR = "#B1DDC6"
LANG_FONT = ("Arial", 40, "italic")
FONT = ("Arial", 60, "bold")

STATUS = "fr"
timer = 0
card = ""

def flip_card(status, lang_word):
    canvas.delete('all')
    if status == "fr":
        word = lang_word["French"]
        canvas_image = canvas.create_image(400, 300, image=fr_img_file)
        canvas.create_text(400, 175, text="french", font=LANG_FONT)
        canvas.create_text(400, 300, text=f"{word}", font=FONT)
    else:
        global STATUS
        STATUS = "en"
        word = lang_word["English"]
        canvas_image = canvas.create_image(400, 300, image=en_img_file)
        canvas.create_text(400, 175, text="english", font=LANG_FONT)
        canvas.create_text(400, 300, text=f"{word}", font=FONT)
    print(STATUS)

    
# print(get_item())
# print(get_item(en="to play"))
# print(get_item(fr="fin"))

# def check_fr(fr_word):
#     get_item(fr=fr_word)


def start():
    global STATUS, card, timer
    STATUS = "fr"
    # print(STATUS)
    card = get_item()
    flip_card(status="fr", lang_word=card)
    timer = window.after(3000, flip_card, "en", card)

def wrong_action():
    global STATUS
    if STATUS == "fr":
        window.after_cancel(timer)
    start()

def right_action():
    global words_to_learn
    for index in range(len(words_to_learn)):
        if words_to_learn[index] == card:
            del words_to_learn[index]
            print(f"{card} is deleted from words_to_learn")
            break
    print(words_to_learn)
    print(len(words_to_learn))
    new_data = pandas.DataFrame(words_to_learn)
    new_data.to_csv("./data/words_to_learn.csv", index=False)
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
# run()
window.mainloop()