import tkinter as tk
from tkinter import colorchooser
import turtle
import os
os.system('cls')

# region functions


def square(size):
    t.penup()
    x_orig = t.position()[0]
    y_orig = t.position()[1]
    heading_orig = t.heading()

    if txt_square_size.get().isnumeric():
        size = int(txt_square_size.get())

    if not size:
        size = s.numinput(
            'Square', 'What size SQUARE would you like?', default=100)

    if square_center.get():
        t.forward(-size/2)
        t.left(-90)
        t.forward(-size/2)
        t.setheading(heading_orig)

    t.pendown()
    for n in range(4):
        t.forward(size)
        t.right(90)
    t.penup()
    t.goto(x_orig, y_orig)
    t.setheading(heading_orig)


def pen_color():
    bgclr = tk.colorchooser.askcolor(title="Choose color")[1]
    btn_pencolor.config(bg=bgclr)
    t.pencolor(bgclr)


# endregion functions

win = tk.Tk()
win.geometry(f"1650x915+150+50")
win.title("Drawing Turtle")
win.resizable(False, False)

frm_canvas = tk.Frame(win, borderwidth=5, relief='sunken')
canvas = tk.Canvas(frm_canvas, width=1650-205,  # width=1650-195,
                   height=915-15, bg='pink')
canvas.grid(row=0, column=0)

frm_buttons = tk.Frame(win)
btn_Square = tk.Button(frm_buttons, text="Square",
                       font=('arial', 14, 'normal'),
                       bg='green2', width=10, borderwidth=2,
                       command=lambda: square(None))
btn_Square.grid(row=0, column=0, pady=2, padx=1, sticky='w')
square_center = tk.BooleanVar()
ckb_Square_center = tk.Checkbutton(frm_buttons, text='center',
                                   variable=square_center)
ckb_Square_center.grid(row=0, column=0, pady=2, padx=1, sticky='e')

txt_square_size = tk.Entry(frm_buttons,
                           font=('arial', 14, 'normal'), bd=5,
                           bg='green2', width=16, justify='center')
txt_square_size.grid(row=1, column=0, pady=(2, 10), padx=1)
# txt_square_size.insert(0, 20)


btn_pencolor = tk.Button(frm_buttons, text="Pen Color",
                         font=('arial', 14, 'normal'),
                         bg='yellow', width=16,
                         command=pen_color)
btn_pencolor.grid(row=2, column=0, pady=2, padx=1)
btn_button03 = tk.Button(frm_buttons, text="Button 3",
                         font=('arial', 14, 'normal'),
                         bg='cyan', width=16)
btn_button03.grid(row=3, column=0, pady=2, padx=1)
btn_button04 = tk.Button(frm_buttons, text="Button 4",
                         font=('arial', 14, 'normal'),
                         bg='pink', width=16)
btn_button04.grid(row=4, column=0, pady=2, padx=1)


frm_canvas.grid(row=0, column=0)
frm_buttons.grid(row=0, column=1)

s = turtle.TurtleScreen(canvas)
s.bgcolor('purple')
s.mode('logo')

t = turtle.RawTurtle(s)
t.shape('turtle')
t.setheading(90)
t.speed(0)
t.pensize(3)
t.pencolor('red')
btn_pencolor.config(bg='red')
t.showturtle()

t.right(289)

t.hideturtle()
t.pensize(5)

square_center.set(True)
for n in range(9):
    square(500)
    t.right(10)

t.hideturtle()
t.pensize(4)
for n in range(9):
    square(400)
    t.right(10)

t.pensize(3)
for n in range(9):
    square(300)
    t.right(10)

square_center.set(False)
t.pensize(2)
for n in range(36):
    square(150)
    t.right(10)

# t.pensize(1)
# for n in range(18):
#     square(170)
#     t.right(10)

t.showturtle()


win.mainloop()
