import tkinter

BACKGROUND_COLOR = "#B1DDC6"

# ---------UI-SETUP
# Window setup
window = tkinter.Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Canvas and flash card setup
canvas = tkinter.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightbackground=BACKGROUND_COLOR)

# image file setup
front_card_png = tkinter.PhotoImage(file="./images/card_front.png")
back_card_png = tkinter.PhotoImage(file="./images/card_back.png")

canvas.create_image(400, 263, image=front_card_png)

# Canvas text setup
language = canvas.create_text(400, 150, text="English", font=("Ariel", 40, "italic"), fill="black")
word = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"), fill="black")
canvas.grid(row=0, column=0, columnspan=2)

# Right Button and button image setup
right_button_image = tkinter.PhotoImage(file="./images/right.png")
right_button = tkinter.Button(image=right_button_image, highlightbackground=BACKGROUND_COLOR)
right_button.grid(row=1, column=1)

# Wrong Button and button image setup
wrong_button_image = tkinter.PhotoImage(file="./images/wrong.png")
wrong_button = tkinter.Button(image=wrong_button_image, highlightbackground=BACKGROUND_COLOR)
wrong_button.grid(row=1, column=0)


window.mainloop()

