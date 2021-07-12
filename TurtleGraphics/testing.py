import tkinter as tk

app = tk.Tk()
app.geometry('300x200')
app.title("Tkitner Scale Example")

scaleExample = tk.Scale(app,
                        orient='horizontal',
                        resolution=1,
                        from_=0,
                        to=10)
scaleExample.pack()
print(scaleExample)
app.mainloop()
