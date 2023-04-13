import turtle
from turtle import *

wn = Screen()
wn.setup(width=1200, height=680)
t = Turtle()
wn.bgcolor('black')
t.speed(0)
colors = ['gold', 'silver', 'red', 'purple']

for i in range(180):
    t.pencolor(colors[i%len(colors)])
    t.rt(i)
    t.circle(100, i)
    t.fd(i)
    t.rt(175)
    t.fd(i)

wn.mainloop()