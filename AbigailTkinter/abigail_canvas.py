import tkinter
from tkinter import *
import os
os.system('cls')


def circle_center(window, x, y, r, **kwargs):
    kwargs = {'width': '20', 'fill': ''} | kwargs
    return window.create_oval(x-r, y-r, x+r, y+r, width=kwargs.get('width'), fill=kwargs.get('fill'))


win = Tk()
win.geometry("1000x800+300+100")
win.title("Abigail's Canvas")

canvas = Canvas(win, width=900, height=700, borderwidth=1, relief='solid')
canvas.pack(padx=10, pady=10)


line = canvas.create_line(300, 300, 600, 600, width=10, fill='green')
circle = canvas.create_oval(50, 50, 200, 200, width=5, fill='red')
rect = canvas.create_rectangle(600, 100, 750, 400, width=5, fill='magenta')
ellipse = canvas.create_oval(610, 110, 740, 390, width=0, fill='yellow')
circle2 = circle_center(canvas, 200, 200, 100)


win.mainloop()
