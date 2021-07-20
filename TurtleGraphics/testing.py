import turtle
import os
os.system('cls')


s = turtle.Screen()
s.bgcolor('light yellow')
t = turtle.Turtle('turtle')
t.speed('fastest')
t.dot(10)
t.pensize(3)
t.penup()
t.hideturtle()
t.goto(-100, 100)

t.dot(10)
t.pencolor('red')

orig_heading = t.heading()
xorig = t.pos()[0]
xmin = t.pos()[0]
xmax = t.pos()[0]
yorig = t.pos()[1]
ymin = t.pos()[1]
ymax = t.pos()[1]

# xorig = xmin = xmax = t.pos()[0]
# yorig = ymin = ymax = t.pos()[1]

print(xorig, yorig)
t.dot(10)

for num in range(5, 10):
    t.goto(xorig, yorig)
    # num = 4
    size = 100
    t.penup()
    t.hideturtle()

    print(int(t.pos()[0]), int(t.pos()[1]))
    for n in range(num):
        # print(int(t.pos()[0]), int(t.pos()[1]))
        x = int(t.pos()[0])
        y = int(t.pos()[1])
        xmin = x if x <= xmin else xmin
        xmax = x if x >= xmax else xmax
        ymin = y if y <= ymin else ymin
        ymax = y if y >= ymax else ymax
        t.forward(size)
        t.right(360/num)

    xavg = (xmax+xmin)/2
    yavg = (ymin+ymax)/2

    t.goto(xavg, yavg)
    t.showturtle()
    t.goto(xorig, yorig)

    t.goto(xorig-xavg, yorig-yavg)
    t.pendown()

    for n in range(num):
        t.forward(size)
        t.right(360/num)

    t.penup()

    # t.goto(xorig, yorig)
    # print(int(t.pos()[0]), int(t.pos()[1]))/

s.mainloop()
