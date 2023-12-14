import turtle

design = turtle.Turtle()
design.speed(0)
design.color("red")

for i in range(500):
    design.forward(i)
    design.right(89)

    if i > 50:
        design.color("orange")
    if i > 100:
        design.color("yellow")
    if i > 150:
        design.color("green")
    if i > 200:
        design.color("aqua")
    if i > 250:
        design.color("blue")
    if i > 300:
        design.color("indigo")
    if i > 350:
        design.color("purple")
    if i > 400:
        design.color("pink")
    if i > 450:
        design.color("black")

turtle.done()