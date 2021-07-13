import turtle
# from turtle import Screen, Turtle

s = turtle.Screen()
t = turtle.Turtle("turtle")


def initialize():
    t.clear()
    t.goto(0, 0)


def dragging(x, y):  # These parameters will be the mouse position
    t.ondrag(None)
    t.setheading(t.towards(x, y))
    t.goto(x, y)
    t.ondrag(dragging)


def clickRight(x, y):
    t.clear()


def main():  # This will run the program

    t.width(5)
    t.speed(0)

    turtle.listen()

    t.ondrag(dragging)  # When we drag the turtle object call dragging
    turtle.onscreenclick(clickRight, 3)
    # t.onclick(clickRight, 3)

    s.mainloop()  # This will continue running main()


main()
