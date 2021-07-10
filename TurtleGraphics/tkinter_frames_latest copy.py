import tkinter as tk
from tkinter import colorchooser
import turtle
import os
os.system('cls')

# region functions


def initialize_screen_and_turtle():
    s.bgcolor('purple')
    s.mode('logo')
    t.reset()
    t.shape('turtle')
    t.setheading(90)
    t.speed(0)
    t.pensize(3)
    t.pencolor('red')
    btn_pencolor.config(bg='red')
    t.showturtle()


def test():
    square_center.set(True)
    t.hideturtle()
    t.pensize(5)
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
    for n in range(27):
        square(150)
        t.right(10)

    t.showturtle()


def square(size):
    x_orig = t.position()[0]
    y_orig = t.position()[1]
    heading_orig = t.heading()

    if txt_square_size.get().isnumeric():
        size = int(txt_square_size.get())
    elif not size:
        size = s.numinput(
            'Square', 'What size SQUARE would you like?', default=100)

    if square_center.get():
        t.penup()
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
win.geometry(f"1710x915+150+50")
win.title("Drawing Turtle")
win.resizable(False, False)

frm_canvas = tk.Frame(win, borderwidth=5, relief='sunken')
frm_buttons = tk.Frame(win, borderwidth=5, relief='sunken',
                       background='light gray')
canvas = tk.Canvas(frm_canvas, width=1710-225,
                   height=915-15, bg='pink')
canvas.grid(row=0, column=0)

frm_buttons.option_add("*font", 'arial 14 normal')

btn_Square = tk.Button(frm_buttons, text="Square",
                       bg='#aaffaa', width=10, borderwidth=2,
                       command=lambda: square(None))
btn_Square.grid(row=0, column=0, pady=2, padx=(3, 1), sticky=tk.W)
square_center = tk.BooleanVar()
ckb_Square_center = tk.Checkbutton(frm_buttons, text='center',
                                   font=('arial', 8, 'normal'),
                                   variable=square_center,
                                   background='light gray')
ckb_Square_center.grid(row=0, column=0, pady=2, padx=1, sticky=tk.E)

txt_square_size = tk.Entry(frm_buttons, bd=5, bg='#aaffaa',
                           width=16, justify=tk.CENTER)
txt_square_size.grid(row=1, column=0, pady=(2, 10), padx=1)
# txt_square_size.insert(0, 20)

btn_pencolor = tk.Button(frm_buttons, text="Pen Color",
                         bg='yellow', width=16,
                         command=pen_color)
btn_pencolor.grid(row=2, column=0, pady=2, padx=1)
btn_clear = tk.Button(frm_buttons, text="Initialize",
                      bg='white', width=16, command=initialize_screen_and_turtle)
btn_clear.grid(row=3, column=0, pady=2, padx=1)
btn_test = tk.Button(frm_buttons, text="TEST",
                     bg='#ffaaaa', width=16, command=test)
btn_test.grid(row=4, column=0, pady=2, padx=1, sticky=tk.W)


frm_canvas.grid(row=0, column=0, padx=2, pady=2, sticky=tk.NS)
frm_buttons.grid(row=0, column=1, padx=2, pady=2, sticky=tk.NSEW)

s = turtle.TurtleScreen(canvas)
t = turtle.RawTurtle(s)

initialize_screen_and_turtle()


win.mainloop()
