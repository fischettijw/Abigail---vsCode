# https://www.youtube.com/watch?v=yuoSKkSEhQg&list=PL6lxxT7IdTxGoHfouzEK-dFcwr_QClME_&index=1

import tkinter as tk
import os
os.system('cls')

ab_window, win_title, win_width, win_height, win_x, win_y = 0, 0, 0, 0, 0, 0


def initialize_variables():
    global win_title, win_width, win_height, win_x, win_y
    win_title = "Trivia Challenge by Abigail Lightle"
    win_width = 800
    win_height = 800
    win_x = 300
    win_y = 100


def create_ab_window():
    global ab_window
    ab_window = tk.Tk()
    ab_window.title(win_title)
    ab_window.config(background='red')
    ab_window.geometry(f'{win_width}x{win_height}+{win_x}+{win_y}')
    ab_window.resizable(width=True, height=True)


def btn_click(answer):
    lbl_btn_click = tk.Label(
        ab_window, text=f'Your selected Option #{answer}',
        font="Courier 24 bold", background='red').pack()
    print(lbl_btn_click['text'])


def create_GUI():
    lbl_title_txt = tk.StringVar()
    lbl_title_txt.set("Abigails's Trivia Challenge")
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

    btn_option1 = tk.Button(ab_window, text='OPTION 1',
                            height=2, font='Courier 16 bold', width=60, command=lambda: btn_click(1)).pack(pady=20)

    btn_option2 = tk.Button(ab_window, text='OPTION 2',
                            height=2, font='Courier 16 bold', width=60, command=lambda: btn_click(2)).pack(pady=20)

    btn_option3 = tk.Button(ab_window, text='OPTION 3',
                            height=2, font='Courier 16 bold', width=60, command=lambda: btn_click(3)).pack(pady=20)

    btn_option4 = tk.Button(ab_window, text='OPTION 4',
                            height=2, font='Courier 16 bold', width=60, command=lambda: btn_click(4)).pack(pady=20)


# https://www.youtube.com/watch?v=mYmqsJ_eSbU&list=PL6lxxT7IdTxGoHfouzEK-dFcwr_QClME_&index=11
initialize_variables()
create_ab_window()
create_GUI()

# label_title_txt.set('This is a test')

ab_window.mainloop()

# https://www.youtube.com/watch?v=ixoXj1WDPbw&list=PL6lxxT7IdTxGoHfouzEK-dFcwr_QClME_&index=24
# https://www.youtube.com/watch?v=ZHix5eYa0m8&list=PL6lxxT7IdTxGoHfouzEK-dFcwr_QClME_&index=21
