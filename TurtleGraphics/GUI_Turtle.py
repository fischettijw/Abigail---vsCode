# https://www.youtube.com/watch?v=G5QmFeSkAxk

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


win = Tk()
win.geometry(f"1200x800+360+140")
win.title("Abigail's Drawing Turtle")
win.configure(background='white')
win.resizable(False, False)

canvas = tk.Canvas(win)
canvas.configure(width=1200-200, height=800)
canvas.pack(side=LEFT, padx=0, pady=0)

s = TurtleScreen(canvas)
s.bgcolor(colorchooser.askcolor(title="Choose color")[1])
s.mode('logo')

t = turtle.RawTurtle(s)
t.shape('turtle')
t.setheading(90)
t.speed(0)
t.pensize(10)
t.showturtle()


txt_square_size = tk.Entry(win, font=('arial', 14), bg='light yellow',
                           justify='center', relief='solid')
txt_square_size.pack(fill=tk.BOTH, padx=2, pady=2)
txt_square_size.insert(0, 20)


btn_draw_color_squares = tk.Button(win, text='Color Squares',
                                   font=('arial', 14, 'normal'),
                                   bg='light yellow',
                                   command=draw_color_squares)
btn_draw_color_squares.pack(fill=BOTH, padx=2, pady=2)

lbl_bg_color = tk.Label(win, text='BkClr', font=('arial', 14),
                        justify='left', bg='#AFEEEE')
lbl_bg_color.pack(side=LEFT, anchor=NW, padx=2, pady=2)

lbl_pen_color = tk.Label(win, text='PenClr', font=('arial', 14),
                         justify='left', bg='#AFEEEE')
lbl_pen_color.pack(side=LEFT, anchor=NW, padx=2, pady=2)


txt_bgcolor = tk.Entry(win, font=('arial', 18), bg='#AFEEEE',
                       justify='center', relief='solid', width=5)
txt_bgcolor.pack(side=TOP, anchor=NE, padx=2, pady=2)
txt_bgcolor.insert(0, 'BgClr')


win.mainloop()
