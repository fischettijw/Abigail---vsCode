# https://stackoverflow.com/questions/44634947/how-to-set-a-turtle-to-a-turtle-screen/44639041#44639041


import turtle
# import keyboard
import os
os.system('cls')

# t = turtle.Turtle()
# s = turtle.Screen()


def move_up(event):
    global drag_segments
    t.setheading(0)
    t.forward(arrow_movement)
    drag_segments = 1


def move_right(event):
    global drag_segments
    t.setheading(90)
    t.forward(arrow_movement)
    drag_segments = 1


def move_down(event):
    global drag_segments
    t.setheading(180)
    t.forward(arrow_movement)
    drag_segments = 1


def move_left(event):
    global drag_segments
    t.setheading(270)
    t.forward(arrow_movement)
    drag_segments = 1


def left_mouse_click(x, y):
    global drag_segments
    t.pendown()
    t.setheading(t.towards(x, y))
    t.goto(x, y)
    drag_segments = 1


def right_mouse_click(x, y):
    global drag_segments
    t.penup()
    t.setheading(t.towards(x, y))
    t.goto(x, y)
    drag_segments = 1


def middle_mouse_click(x, y):
    global drag_segments
    for n in range(0, drag_segments):
        t.undo()
    drag_segments = 1


def dragging(x, y):  # These parameters will be the mouse position
    global drag_segments
    t.ondrag(None)
    t.setheading(t.towards(x, y))
    t.goto(x, y)
    drag_segments += 1
    t.ondrag(dragging)


t = turtle.Turtle()
s = turtle.Screen()

drag_segments = 1
arrow_movement = 10

s.setup(width=1200, height=800, startx=0, starty=None)
s.title("Abigail's Drawing Program")
s.bgcolor('magenta')
s.mode('logo')  # up = 0, right = 90, down = 180, left = 270

t.shape('turtle')
t.pensize(20)
t.speed('fastest')


#                 *****  EVENTS    *****

t.ondrag(dragging)
# t.onclick(turtle_click)

s.onclick(left_mouse_click, btn=1)      # left buttom
s.onclick(middle_mouse_click, btn=2)    # Middle buttom
s.onclick(right_mouse_click, btn=3)     # Right buttom

s.listen()  # listen for KEY Events
s.getcanvas().bind("<Up>", move_up)
s.getcanvas().bind("<Right>", move_right)
s.getcanvas().bind("<Down>", move_down)
s.getcanvas().bind("<Left>", move_left)
# s.onkey(move_up, "Up")
# s.onkey(move_right, "Right")
# s.onkey(move_down, "Down")
# s.onkey(move_left, "Left")


s.mainloop()
