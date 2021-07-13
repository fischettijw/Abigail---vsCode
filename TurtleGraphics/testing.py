import turtle
import os
os.system('cls')


s = turtle.Screen()
s.bgcolor('light yellow')
t = turtle.Turtle('turtle')
t.speed('fastest')
t.pensize(3)
t.dot(10)
t.pencolor('red')

xx = []
yy = []
xmin = t.pos()[0]
xmax = t.pos()[0]
ymin = t.pos()[1]
ymax = t.pos()[1]
num = 50
size = 10
t.pendown()
for n in range(num):
    x = int(t.pos()[0])
    y = int(t.pos()[1])
    xx.append(x)
    yy.append(y)
    xmin = x if x <= xmin else xmin
    xmax = x if x >= xmax else xmax
    ymin = y if y <= ymin else ymin
    ymax = y if y >= ymax else ymax

    t.forward(size)
    t.right(360/num)

xavg = (xmax+xmin)/2
yavg = (ymin+ymax)/2
print(xx, '\n', yy)
print(xmin, xmax, ymin, ymax)
print(xavg, yavg)
t.penup()
t.goto(xavg, yavg)


s.mainloop()
