import tkinter as tk
import turtle
import os
os.system('cls')


win = tk.Tk()
win.geometry(f"1650x910+150+50")
win.title("Drawing Turtle")
win.resizable(False, False)

frm_canvas = tk.Frame(win, borderwidth=5, relief='sunken')
canvas = tk.Canvas(frm_canvas, width=1650-205,  # width=1650-195,
                   height=900, bg='pink')
canvas.grid(row=0, column=0)

frm_buttons = tk.Frame(win)
btn_button01 = tk.Button(frm_buttons, text="Button 1",
                         font=('arial', 14, 'normal'),
                         bg='green', width=16)
btn_button01.grid(row=0, column=0, pady=2, padx=1)
btn_button02 = tk.Button(frm_buttons, text="Button 2",
                         font=('arial', 14, 'normal'),
                         bg='yellow', width=16)
btn_button02.grid(row=1, column=0, pady=2, padx=1)
btn_button03 = tk.Button(frm_buttons, text="Button 3",
                         font=('arial', 14, 'normal'),
                         bg='cyan', width=16)
btn_button03.grid(row=2, column=0, pady=2, padx=1)
btn_button04 = tk.Button(frm_buttons, text="Button 4",
                         font=('arial', 14, 'normal'),
                         bg='pink', width=16)
btn_button04.grid(row=3, column=0, pady=2, padx=1)


frm_canvas.grid(row=0, column=0)
frm_buttons.grid(row=0, column=1)

s = turtle.TurtleScreen(canvas)
s.bgcolor('purple')
s.mode('logo')

t = turtle.RawTurtle(s)
t.shape('turtle')
t.setheading(90)
t.speed(0)
t.pensize(10)
t.showturtle()


win.mainloop()
