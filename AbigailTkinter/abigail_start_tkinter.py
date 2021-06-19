from tkinter import *
import os
os.system('cls')


def print_hello():
    print('HELLO')
    btn_click.flash()
    btn_click.flash()
    btn_click.flash()


win = Tk()
win.geometry("800x600")

lbl_hello = Label(win, text="My Name is Abigail", font="arial 30 bold",
                  fg="red", bg="blue", width="30", height="3")
lbl_hello.pack()

btn_click = Button(win, text="Click", font="arial 30 bold",
                   fg="green", bg="orange", width="20", command=print_hello)
btn_click.pack(pady="20")

txt_input = Entry(win, font="arial 48 italic", width="10", justify="center")
txt_input.pack()

win.mainloop()
