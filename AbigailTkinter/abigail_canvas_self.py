import tkinter
from tkinter import *
from abigail_tkinter_func import *
import os
os.system('cls')

win = Tk()
win.geometry("1000x800+300+100")
win.title("Abigail's Canvas")

canvas = Canvas(win, width=900, height=700, borderwidth=1, relief='solid')
canvas.pack(padx=10, pady=10)

clr = canvas.rgb_to_tkColor(255, 128, 255)

line = canvas.create_line(300, 300, 600, 600, width=10, fill=clr)
circle = canvas.create_oval(50, 50, 200, 200, width=5, fill='red')
rect = canvas.create_rectangle(600, 100, 750, 400, width=5, fill='magenta')
ellipse = canvas.create_oval(610, 110, 740, 390, width=0, fill='green')
circle2 = canvas.create_circle_center(200, 200, 100, width=5, fill='blue')
circle2 = canvas.create_circle_center_ul(200, 200, 100,  fill='gray')


win.mainloop()
