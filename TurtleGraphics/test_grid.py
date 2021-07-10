import tkinter as tk

win = tk.Tk()
win.geometry(f"1000x800+360+140")
win.config(back='red')

win.option_add("*font", "Arial 30 bold")
win.option_add("*height", 4)
win.option_add("*foreground", "cyan")
win.option_add("*background", "yellow")
win.option_add("*Button.relief", "solid")


frm00 = tk.Frame(win, borderwidth=5, relief='flat', background='cyan')
frm01 = tk.Frame(win, borderwidth=5, relief='flat', background='cyan')

btn = tk.Button(frm00, text="btn 1", width=13)
btn.grid(row=0, column=0, padx=(2, 2), pady=5, sticky=tk.EW)

btn1 = tk.Button(frm01, text="btn 1", width=10)
btn1.grid(row=0, column=0, padx=(2, 2), pady=5, sticky=tk.EW)
btn2 = tk.Button(frm01, text="btn 2")
btn2.grid(row=0,  column=1, padx=(2, 0), sticky=tk.EW)
btn3 = tk.Button(frm01, text="btn 3", width=25)
btn3.grid(row=2, columnspan=2,  sticky=tk.EW, padx=2, pady=2)
btn4 = tk.Button(frm01, text="btn 4")
btn4.grid(row=3, column=0,  sticky=tk.EW, padx=2, pady=2)


frm00.grid(row=0, column=0, padx=10, pady=10, sticky=tk.NS)
frm01.grid(row=0, column=1, padx=10, pady=10, sticky=tk.NS)

win.mainloop()
