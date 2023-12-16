import turtle

r = 255
g = 0
b = 0

t = turtle.Turtle()
t.speed(0)

for i in range(255):
    turtle.colormode(255)

    if i >= 0 and i <= 50:
        g += 5
    elif i >= 50 and i <= 101:
        r -= 5
    elif i >= 101 and  i <= 152:
        g -= 5
        b += 5
    elif i >= 152 and i <= 203:
        r += 5
    elif i >= 203 and i <= 255:
        r -= 5
        b -= 5
    
    t.pencolor(r, g, b)
    t.forward(i*2)
    t.right(89)

turtle.done()