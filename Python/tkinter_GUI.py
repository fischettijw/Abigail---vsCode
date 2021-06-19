# https://www.youtube.com/watch?v=yuoSKkSEhQg&list=PL6lxxT7IdTxGoHfouzEK-dFcwr_QClME_&index=1

import tkinter as tk
import os
os.system('cls')

ab_window, win_title, win_width, win_height, win_x, win_y = 0, 0, 0, 0, 0, 0


def initialize_variables():
    global win_title, win_width, win_height, win_x, win_y
    win_title = "Abigails's Window"
    win_width = 800
    win_height = 600
    win_x = 300
    win_y = 100


def create_ab_window():
    global ab_window
    ab_window = tk.Tk()
    ab_window.title(win_title)
    ab_window.config(background='red')
    ab_window.geometry(f'{win_width}x{win_height}+{win_x}+{win_y}')
    ab_window.resizable(width=True, height=False)


def create_GUI():
    lbl_title_txt = tk.StringVar()
    lbl_title_txt.set("Abigail's Trivia Game")
    lbl_title = tk.Label(ab_window, textvariable=lbl_title_txt,
                         background='red', foreground='black',
                         font="Courier 32 bold italic")
    lbl_title.pack(pady=0)

    lbl_question_number = tk.Label(ab_window, text='Question #1',
                                   background='red', foreground='black',
                                   font="Courier 28 bold italic")
    lbl_question_number.pack(pady=0)

    lbl_question = tk.Label(ab_window, text='How many legs does a spider have?',
                            background='red', foreground='black',
                            font="Courier 24 bold")
    lbl_question.pack(pady=20)

    lbl_option = tk.Label(ab_window, text='1:  6\n2:  8\n3: 10\n4: 12',
                          background='red', foreground='black',
                          font="Courier 20")
    lbl_option.pack(pady=0)


# https://www.youtube.com/watch?v=mYmqsJ_eSbU&list=PL6lxxT7IdTxGoHfouzEK-dFcwr_QClME_&index=11

initialize_variables()
create_ab_window()
create_GUI()

# label_title_txt.set('This is a test')

ab_window.mainloop()

# https://www.youtube.com/watch?v=ixoXj1WDPbw&list=PL6lxxT7IdTxGoHfouzEK-dFcwr_QClME_&index=24
# https://www.youtube.com/watch?v=ZHix5eYa0m8&list=PL6lxxT7IdTxGoHfouzEK-dFcwr_QClME_&index=21
