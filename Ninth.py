import turtle
from turtle import *

wn = Screen()
wn.setup(width=1200, height=680)
t = Turtle()
wn.bgcolor('black')
t.speed(0)
colors = ['white', 'violet']

for i in range(180):
    t.pencolor(colors[i%len(colors)])
    t.rt(i)
    t.circle(150, i)
    t.fd(i)
    t.rt(150)
    t.fd(i)

wn.mainloop()