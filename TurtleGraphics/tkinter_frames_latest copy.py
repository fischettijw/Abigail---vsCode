
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
    btn_pencolor.config(bg='red')
    t.showturtle()


def pen_size(sz):
    t.pensize(sz)


def apothem(num_of_sides, len_of_side):
    return (len_of_side/2)/tan(radians(360/(2*num_of_sides)))


def circle(size=100):
    t.pendown()
    size = s.numinput(
        'Circle', 'What size CIRCLE would you like?', default=size)
    t.circle(size)


def triangle(size=100):
    t.pendown()
    size = s.numinput(
        'Triangle', 'What size TRIANGLE would you like?', default=size)
    for n in range(3):
        t.forward(size)
        t.right(120)

    lbl_status_1['text'] = f'TRIANGLE ({int(size)})'


def hexagon(size=100):
    t.pendown()
    size = s.numinput(
        'Hexagon', 'What size HEXAGON would you like?', default=size)
    for n in range(6):
        t.forward(size)
        t.right(60)


def poly(num=6, size=100, ask=False):
    x_orig = t.position()[0]
    y_orig = t.position()[1]
    heading_orig = t.heading()

    if ask:
        num = int(s.numinput(
            'Polygon', 'How many SIDES would you like?', default=num))
        size = int(s.numinput(
            'Polygon', 'What LENGTH sides would you like?', default=size))

    if square_center.get():
        t.penup()
        t.forward(-apothem(num, size))
        t.left(-90)
        t.forward(-apothem(num, size))
        t.setheading(heading_orig)

    t.pendown()
    for n in range(num):
        t.forward(size)
        t.right(360/num)

    t.penup()
    t.goto(x_orig, y_orig)
    t.setheading(heading_orig)

    lbl_status_1['text'] = f'POLYGON ({num} X {int(size)})'


def write_text():
    text = s.textinput(
        'Enter Text', 'What TEXT would you like to write to the canvas?')
    t.write(text, font=('Arial', 24, 'bold'), align='center')


# https://jaxenter.com/implement-switch-case-statement-python-138315.html
def cbx_changed(event):
    cbx_choice = event.widget.get()
    switcher = {
        'circle': lambda: circle(150),
        'triangle': triangle,
        'square': lambda: square(None),
        'hexagon': hexagon
    }
    # func = switcher.get(cbx_choice,
    #                     lambda: print(func=switcher[cbx_choice]))
    func = switcher[cbx_choice]
    func()


def square(size=125):
    x_orig = t.position()[0]
    y_orig = t.position()[1]
    heading_orig = t.heading()

    if txt_square_size.get().isnumeric():
        size = int(txt_square_size.get())
    else:  # https://stackoverflow.com/questions/16373887/how-to-set-the-text-value-content-of-an-entry-widget-using-a-button-in-tkinter
        txt_square_size.delete(0, tk.END)
        size = s.numinput(
            'Square', 'What size SQUARE would you like?', default=size)
        if size == None:
            return

    if square_center.get():
        t.penup()
        t.forward(-apothem(4, size))
        # t.forward(-size/2)
        t.left(-90)
        t.forward(-apothem(4, size))
        # t.forward(-size/2)
        t.setheading(heading_orig)

    t.pendown()
    for n in range(4):
        t.forward(size)
        t.right(90)
    t.penup()
    t.goto(x_orig, y_orig)
    t.setheading(heading_orig)

    lbl_status_1['text'] = f'SQUARE ({int(size)})'


def pen_color():
    bgclr = colorchooser.askcolor(title="Choose color")[1]
    btn_pencolor.config(bg=bgclr)
    t.pencolor(bgclr)


def left_mouse_click(x, y):
    t.pendown()
    t.setheading(t.towards(x, y))
    t.goto(x, y)


def right_mouse_click(x, y):
    t.penup()
    t.setheading(t.towards(x, y))
    t.goto(x, y)


def dragging(x, y):  # These parameters will be the mouse position
    t.ondrag(None)
    t.setheading(t.towards(x, y))
    t.goto(x, y)
    t.ondrag(dragging)


# endregion functions

# region root Tkinter window
win = tk.Tk()
win.geometry(f"1780x945+70+30")
# win.geometry(f"1780x915+70+50")
win.title("Drawing Turtle")
win.resizable(False, False)

# endregion root Tkinter window

# region GUI

# region Frames
frm_menubar = tk.Frame(win, borderwidth=0, relief='flat')
frm_canvas = tk.Frame(win, borderwidth=5, relief='sunken')
frm_buttons = tk.Frame(win, borderwidth=5, relief='sunken',
                       background='light gray')
# endregion Frames

# region Menubar & Status Bar
menu_bar = tk.Menu(win)

file_menu = tk.Menu(menu_bar)
file_menu.add_command(label='Open')
file_menu.add_command(label='Save')
menu_bar.add_cascade(label='File', menu=file_menu)

pen_menu = tk.Menu(menu_bar)
pen_menu.add_command(label='Pen Color', command=pen_color)
pen_menu.add_command(label='Pen Thickness')
menu_bar.add_cascade(label='Pen', menu=pen_menu)

shapes_menu = tk.Menu(menu_bar)
shapes_menu.add_command(label='Triangle')
shapes_menu.add_command(label='Square', command=lambda: square(100))
shapes_menu.add_command(label='Pentagon', command=lambda: poly(5, 100, True))
menu_bar.add_cascade(label='Shapes', menu=shapes_menu)

help_menu = tk.Menu(menu_bar)
help_menu.add_command(label='Mouse Commands')
help_menu.add_command(label='Key Commands')
menu_bar.add_cascade(label='Help', menu=help_menu)

win.config(menu=menu_bar)

# status_bar = tk.Label(win, text="This will contain STATUS !!!!!!",
#                       bd=1, relief=tk.SUNKEN, anchor=tk.W)
# status_bar.pack(side=tk.BOTTOM, fill=tk.X)


# endregion Menubar & Status Bar


canvas = tk.Canvas(frm_canvas, width=1780-225-10,
                   height=915-15)
canvas.grid(row=0, column=0, columnspan=3)

# status_bar = tk.Label(frm_canvas, text="This will contain STATUS !!!!!!",
#                       bd=1, relief=tk.SUNKEN, anchor=tk.W, font='courier 14')
# status_bar.grid(row=1, column=0, sticky=tk.EW)
lbl_status_1 = tk.Label(frm_canvas, text="This will contain STATUS 1 !!!!!!",
                        bd=1, relief=tk.SUNKEN,  font='courier 14', width=1)
lbl_status_1.grid(row=1, column=0, sticky=tk.EW)
lbl_status_2 = tk.Label(frm_canvas, text="This will contain STATUS 2 !!!!!!",
                        bd=1, relief=tk.SUNKEN,  font='courier 14', width=1)
lbl_status_2.grid(row=1, column=1, sticky=tk.EW)
lbl_status_3 = tk.Label(frm_canvas, text="This will contain STATUS 3 !!!!!!",
                        bd=1, relief=tk.SUNKEN,  font='courier 14', width=1)
lbl_status_3.grid(row=1, column=2, sticky=tk.EW)

frm_buttons.option_add("*font", 'arial 14 normal')

btn_Square = tk.Button(frm_buttons, text="Square",
                       bg='#aaffaa', width=8, borderwidth=2,
                       command=lambda: square(25))
btn_Square.grid(row=0, column=0, pady=2, padx=(8, 0), sticky=tk.W)
square_center = tk.BooleanVar()
ckb_Square_center = tk.Checkbutton(frm_buttons, text='center',
                                   font=('arial', 12, 'normal'),
                                   variable=square_center,
                                   background='light gray')
ckb_Square_center.grid(row=0, column=0, pady=2, padx=16, sticky=tk.E)

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

cbx_var = tk.StringVar()
cbx_options = ['circle', 'triangle', 'square', 'hexagon']

cbx_functions = ttk.Combobox(frm_buttons, text="Select Function",
                             width=15, state='readonly',
                             textvariable=cbx_var, values=cbx_options)
cbx_functions.grid(row=5, column=0, pady=2, padx=8,  sticky=tk.W)
cbx_functions.bind('<<ComboboxSelected>>', cbx_changed)

btn_poly = tk.Button(frm_buttons, text="Polyagon",
                     bg='#ffaaaa', width=16, command=lambda: poly(ask=True))
btn_poly.grid(row=6, column=0, pady=2, padx=8, sticky=tk.W)


scl_pensize_var = tk.IntVar()
scl_pensize = tk.Scale(frm_buttons, orient='horizontal',
                       resolution=1.0, from_=1, to=20,
                       length=180, variable=scl_pensize_var, command=pen_size)
scl_pensize.grid(row=7, column=0, pady=2, padx=8, sticky=tk.W)


btn_text = tk.Button(frm_buttons, text="Write Text",
                     bg='#ffaaaa', width=16, command=write_text)
btn_text.grid(row=8, column=0, pady=2, padx=8, sticky=tk.W)


frm_canvas.grid(row=0, column=0, padx=2, pady=2, sticky=tk.NS)
frm_buttons.grid(row=0, column=1, padx=2, pady=2, sticky=tk.NSEW)

# endregion GUI

# region turtle and screen definition
s = turtle.TurtleScreen(canvas)
t = turtle.RawTurtle(s)

initialize_screen_and_turtle()

# endregion turtle and screen definition


# region events   *****          EVENTS         *****
s.onclick(left_mouse_click, btn=1)
s.onclick(right_mouse_click, btn=3)

t.ondrag(dragging)


# key is pressed    https://www.youtube.com/watch?v=InBr_Kh4a5Y

# endregion events

win.mainloop()
