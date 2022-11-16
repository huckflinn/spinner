from turtle import *

state = {"turn" : 0}

def spinner():
    clear()
    angle = state["turn"] / 10
    right(angle)
    forward(100)
    dot(120, "red")
    back(100)
    right(120)
    forward(100)
    right(60)
    forward(100)
    dot(120, "green")
    back(100)
    left(60)
    back(100)
    right(120)
    forward(100)
    left(60)
    forward(100)
    dot(120, "blue")
    back(100)
    right(60)
    back(100)
    right(120)
    update()

def animate():
    if state["turn"] > 0:
        state["turn"] -= 1
    if state["turn"] < 0:
        state["turn"] += 1

    spinner()
    ontimer(animate, 20)

def flickright():
    state["turn"] += 10

def flickleft():
    state["turn"] -= 10

setup(840, 840, 370, 0)
hideturtle()
tracer(False)
width(5)
onkey(flickright, "Right")
onkey(flickleft, "Left")
listen()
animate()
done()