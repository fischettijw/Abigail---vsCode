#  https://docs.python.org/3.3/library/turtle.html?highlight=turtle

import turtle
import os
os.system('cls')


def square(t, num, size):
    for s in range(num):
        t.forward(size)
        t.left(360/num)


scrn = turtle.Screen()
scrn.mode('standard')   # standard    logo

t1 = turtle.Turtle()
t1.penup()
t1.setpos(0, 0)
t2 = turtle.Turtle()
t2.penup()
t2.setpos(0, 0)
# t2 = turtle.Turtle()
# t2.penup()
# t2.setpos(160, 130)


scrn.bgcolor('yellow')
scrn.title('Turtle Graphics by Abigail')


t1.pendown()
t2.pendown()


t1.speed(5)
t1.width(4)
t1.pencolor('red')
t1.fillcolor('cyan')

t2.speed(5)
t2.width(4)
t2.pencolor('green')
t2.fillcolor('purple')

t1.begin_fill()
t2.begin_fill()

t1.forward(100)
t2.forward(50)
t1.right(90)
t2.right(90)
t1.forward(100)
t2.forward(50)
t1.right(90)
t2.right(90)
t1.forward(100)
t2.forward(50)
t1.right(90)
t2.right(90)
t1.forward(100)
t2.forward(50)
t1.right(90)
t2.right(90)

t2.end_fill()
t1.end_fill()

t1.hideturtle()
t2.hideturtle()

scrn.exitonclick()

turtle.done()
