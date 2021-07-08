# https://stackoverflow.com/questions/44634947/how-to-set-a-turtle-to-a-turtle-screen/44639041#44639041

from draw_module import *
import turtle
import os
os.system('cls')


# t = turtle.Turtle()
# s = turtle.Screen()

# drag_segments = 1
# arrow_movement = 10

s.setup(width=1200, height=800, startx=None, starty=None)
s.title("Abigail's Drawing Program")
s.bgcolor('yellow')
s.mode('logo')  # up = 0, right = 90, down = 180, left = 270

t.shape('turtle')
t.color('white')
t.pensize(3)
t.speed('fastest')
t.pencolor("red")


#                 *****  EVENTS    *****

t.ondrag(dragging)

s.onclick(left_mouse_click, btn=1)      # left buttom
s.onclick(middle_mouse_click, btn=2)    # Middle buttom
s.onclick(right_mouse_click, btn=3)     # Right buttom

s.listen()  # listen for KEY Events
s.getcanvas().bind("<Up>", move_up)
s.getcanvas().bind("<Right>", move_right)
s.getcanvas().bind("<Down>", move_down)
s.getcanvas().bind("<Left>", move_left)

s.onkey(hide, 'i')      # make TURTLE invisible
s.onkey(show, 'v')      # make TURTLE visible
s.onkey(clear, 'c')     # clear screen
s.onkey(bkground, 'B')  # change background color
s.onkey(write_text, 'T')      # write TEXT on screen

s.onkey(lambda: square(None), 'S')  # draw SQUARE and request size
s.onkey(lambda: square(50), 's')    # draw SQUARE with provided size

s.mainloop()
