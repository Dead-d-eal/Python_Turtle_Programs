import turtle
colors = ['Blue', 'purple', 'red', 'lightgreen', 'green', 'brown']
t = turtle.Pen()
turtle.bgcolor('black')
for x in range(180):
    t.pencolor(colors[x%6])
    t.width(x//50 + 1)
    t.forward(x)
    t.left(59)
for y in range(180):
    t.pencolor(colors[y%6])
    t.width(y//50 * 1)
    t.backward(y)
    t.right(59)