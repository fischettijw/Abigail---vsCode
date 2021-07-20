# import package
import turtle
import os
os.system('cls')


# start recording polygon
t = turtle.Turtle()
s = turtle.Screen()
s.setup(width=1.0, height=1.0, startx=0, starty=0)
# s.addshape('space_ship.gif')
# t.shape('space_ship.gif')
t.shape('turtle')
t.pencolor('red')
t.shapesize(5, 2, 2)

t.forward(300)
t.right(90)
t.forward(300)
# t.begin_poly()

# # form an ellipse
# t.circle(20, 90)
# t.circle(10, 90)
# t.circle(20, 90)
# t.circle(10, 90)

# # end recording polygon
# t.end_poly()

# get poly that recorded
print(t.get_poly(), '\n')

s.exitonclick()

s.mainloop()
