import tkinter
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

# ---------LANGUAGE-DATA-FILE-SETUP
data = pandas.read_csv("./data/Language_data.csv")
word_list_dict = pandas.DataFrame.to_dict(data, "records")
new_word = {}

# ---------BUTTON-FUNCTION-SETUP
known_count = -1
unknown_count = 0


def right_button_click():
    global new_word
    global flip_timer
    global known_count
    window.after_cancel(flip_timer)
    new_word = random.choice(word_list_dict)
    canvas.itemconfig(canvas_image, image=front_card_png)
    canvas.itemconfig(word_title, text=f"{new_word["German"]}", fill="black")
    canvas.itemconfig(language_title, text="German", fill="black")
    flip_timer = window.after(3000, func=flip_card)
    known_count += 1
    label.config(text=f"unknown word count: {unknown_count}, known word count: {known_count}")


def wrong_button_click():
    global new_word
    global flip_timer
    global unknown_count
    window.after_cancel(flip_timer)
    new_word = random.choice(word_list_dict)
    canvas.itemconfig(canvas_image, image=front_card_png)
    canvas.itemconfig(word_title, text=f"{new_word["German"]}", fill="black")
    canvas.itemconfig(language_title, text="German", fill="black")
    flip_timer = window.after(3000, func=flip_card)
    unknown_count += 1
    label.config(text=f"unknown word count: {unknown_count}, known word count: {known_count}")


# -------CHANGE-CARD
def flip_card():
    canvas.itemconfig(canvas_image, image=back_card_png)
    canvas.itemconfig(language_title, text="English", fill="white")
    canvas.itemconfig(word_title, text=f"{new_word["English"]}", fill="white")


# ---------UI-SETUP
# Window setup
window = tkinter.Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

# Canvas and flash card setup
canvas = tkinter.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightbackground=BACKGROUND_COLOR)

# image file setup
front_card_png = tkinter.PhotoImage(file="./images/card_front.png")
back_card_png = tkinter.PhotoImage(file="./images/card_back.png")

canvas_image = canvas.create_image(400, 263, image=front_card_png)

# Canvas text setup
language_title = canvas.create_text(400, 150, font=("Ariel", 40, "italic"), fill="black")
word_title = canvas.create_text(400, 263, font=("Ariel", 60, "bold"), fill="black")
canvas.grid(row=0, column=0, columnspan=2)

# Right Button and button image setup
right_button_image = tkinter.PhotoImage(file="./images/right.png")
right_button = tkinter.Button(image=right_button_image, highlightbackground=BACKGROUND_COLOR,
                              command=right_button_click)
right_button.grid(row=1, column=1)

# Wrong Button and button image setup
wrong_button_image = tkinter.PhotoImage(file="./images/wrong.png")
wrong_button = tkinter.Button(image=wrong_button_image, highlightbackground=BACKGROUND_COLOR,
                              command=wrong_button_click)
wrong_button.grid(row=1, column=0)

# Label
label = tkinter.Label(text=f"unknown word count: {unknown_count}, known word count: {known_count}", bg=BACKGROUND_COLOR,
                      fg="black", pady=10, font=("Arial", 16, "bold"))
label.grid(row=2, column=0, columnspan=2)

right_button_click()

window.mainloop()
