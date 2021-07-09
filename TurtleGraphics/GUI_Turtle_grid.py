# https://www.youtube.com/watch?v=Mxk4cMBaH3g&list=PL6lxxT7IdTxGoHfouzEK-dFcwr_QClME_&index=36

import os
from turtle import *
import turtle
import tkinter as tk
from tkinter import *
from tkinter import colorchooser
os.system('cls')


def color_square(t, sz):
    for c in ['red', 'purple', 'hotpink', 'blue']:
        t.pencolor(c)
        t.forward(sz)
        t.left(90)


def draw_color_squares():
    t.pensize(6)
    t.hideturtle()
    if txt_square_size.get().isnumeric():
        sz = int(txt_square_size.get())
    else:
        txt_square_size.delete(0, 'end')
        return
    for n in range(18):
        color_square(t, sz)
        sz += 20
        t.forward(20)
        t.right(20)
    t.showturtle()


def change_bgcolor():
    bgclr = colorchooser.askcolor(title="Choose color")[1]
    s.bgcolor(bgclr)
    # btn_bgcolor.config(bg=bgclr)


win = Tk()
win.geometry(f"1240x800+360+140")
win.title("Abigail's Drawing Turtle")
win.configure(background='white')
win.resizable(False, False)

frm_canvas = tk.Frame(win)
canvas = tk.Canvas(frm_canvas)
canvas.configure(width=1200-200, height=800, bg='pink')
frm_canvas.grid(row=0, column=0)


frm_buttons = tk.Frame(win)
lbl_test = tk.Label(frm_buttons, text='Tesy', font=('arial', 14),
                    justify='left', bg='yellow')
frm_buttons.grid(row=0, column=1)


s = TurtleScreen(canvas)
s.mode('logo')

t = turtle.RawTurtle(s)
t.shape('turtle')
# t.setheading(90)
# t.speed(0)
# t.pensize(10)
# t.showturtle()


# txt_square_size = tk.Entry(win, font=('arial', 14), bg='light yellow',
#                            justify='center', relief='solid')
# txt_square_size.grid(row=0, column=5)
# txt_square_size.insert(0, 20)


# btn_draw_color_squares = tk.Button(win, text='Color Squares',
#                                    font=('arial', 14, 'normal'),
#                                    bg='light yellow',
#                                    command=draw_color_squares)
# btn_draw_color_squares.grid(row=35, column=5)

# lbl_bg_color = tk.Label(win, text='BkClr', font=('arial', 14),
#                         justify='left', bg='#AFEEEE')
# lbl_bg_color.pack(side=LEFT, anchor=NW, padx=2, pady=2)

# lbl_pen_color = tk.Label(win, text='PenClr', font=('arial', 14),
#                          justify='left', bg='#AFEEEE')
# lbl_pen_color.pack(side=LEFT, anchor=NW, padx=2, pady=2)


# txt_bgcolor = tk.Entry(win, font=('arial', 18), bg='#AFEEEE',
#                        justify='center', relief='solid', width=5)
# txt_bgcolor.pack(side=TOP, anchor=NE, padx=2, pady=2)
# txt_bgcolor.insert(0, 'BgClr')

# btn_bgcolor = tk.Button(win, text='BgColor',
#                         font=('arial', 14, 'normal'),
#                         bg='light yellow',
#                         command=change_bgcolor)
# btn_bgcolor.pack(row=2, column=5)
# # btn_bgcolor.pack(side=LEFT,anchor=NW, padx=2, pady=2)


win.mainloop()
