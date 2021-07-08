# https://stackoverflow.com/questions/44634947/how-to-set-a-turtle-to-a-turtle-screen/44639041#44639041


import turtle
import keyboard
global t, s, drag_segments, arrow_movement

t = turtle.Turtle()
s = turtle.Screen()

drag_segments = 1
arrow_movement = 10


def square(side):
    if side == None:
        side = s.numinput(
            'Square', 'What size SQUARE would you like?', default=100)
    for n in range(4):
        t.forward(side)
        t.right(90)


def hide():
    t.hideturtle()


def show():
    t.showturtle()


def clear():
    s.clear()


def bkground():
    bColor = s.textinput('Change Background Color',
                         'What color would you like?')
    s.bgcolor(bColor)


def write_text():
    txt = s.textinput('Input Text', 'What TEXT would you like?')
    t.write(txt, align='center', font=('Arial', 30, 'bold'))


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
