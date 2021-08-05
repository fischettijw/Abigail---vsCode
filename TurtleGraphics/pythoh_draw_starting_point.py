# region Links

# Python Course (12 hours)      https://www.youtube.com/watch?v=XKHEtdqhLK8
# Python Course (200 Videos)    https://www.youtube.com/watch?v=wqPzyszZrQc&list=PL6lxxT7IdTxFKo9DguLxGM2dhgb8-u976

# Tkinter Course (5 1/2 hours)  https://www.youtube.com/watch?v=YXPyB4XeYLA&t=17644s
# Tkinter Course (72 Videos)    https://www.youtube.com/watch?v=yuoSKkSEhQg&list=PL6lxxT7IdTxGoHfouzEK-dFcwr_QClME_

# Tkinter Documentation (Text)  https://tkdocs.com/tutorial/index.html
# Tkinter Events (Text)         https://docstore.mik.ua/orelly/other/python/0596001886_pythonian-chp-16-sect-9.html

# Turtle Documentation (Text)   https://docs.python.org/3.3/library/turtle.html?highlight=turtle
# Turtle Events (7 Videos)      https://www.youtube.com/watch?v=9PlmASWfVMg&list=PLreacSZInFp3jMjmrp6FZdB0GxfAsgIAu
# Turtle GUI (36 minutes)       https://www.youtube.com/watch?v=G5QmFeSkAxk

# endregion Links

# region imports
from math import tan, radians
import time as tm
import tkinter as tk
from tkinter import ttk
from tkinter import colorchooser
import turtle
import os
os.system('cls')

# endregion imports

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
    t.showturtle()


# endregion functions
# region root Tkinter window
win = tk.Tk()
win.geometry(f"1780x945+70+30")
win.title("Python Draw by Miguel")
win.resizable(False, False)

# endregion root Tkinter window

# region GUI

# region Frames

# endregion Frames

# region Menubar & Status Bar


# endregion Menubar & Status Bar

canvas = tk.Canvas(win, width=1780-225-10, height=915 -
                   15)    # this assumes NO frames
canvas.grid(row=0, column=0, columnspan=3)

# endregion GUI

# region turtle and screen definition
s = turtle.TurtleScreen(canvas)
t = turtle.RawTurtle(s)

initialize_screen_and_turtle()

# endregion turtle and screen definitßion


# region events   *****          EVENTS         *****


# key is pressed    https://www.youtube.com/watch?v=InBr_Kh4a5Y

# endregion events

win.mainloop()
