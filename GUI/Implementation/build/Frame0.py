
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets/frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("766x508")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 508,
    width = 766,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    383.0,
    254.0,
    image=image_image_1
)

canvas.create_text(
    171.0,
    81.0,
    anchor="nw",
    text="Criminal Investigation System",
    fill="#FFFFFF",
    font=("RobotoRoman Bold", 32 * -1)
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    387.0,
    100.0,
    image=image_image_2
)

canvas.create_text(
    298.0,
    184.0,
    anchor="nw",
    text="Choose Mode",
    fill="#FFFFFF",
    font=("RobotoRoman Bold", 28 * -1)
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    387.0,
    199.0,
    image=image_image_3
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=247.0,
    y=263.0,
    width=281.0,
    height=60.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("Developer Button Clicked!"),
    relief="flat"
)
button_2.place(
    x=247.0,
    y=263.0,
    width=281.0,
    height=60.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("User Button Clicked!"),
    relief="flat"
)
button_3.place(
    x=247.0,
    y=362.0,
    width=281.0,
    height=60.0
)
window.resizable(False, False)
window.mainloop()
