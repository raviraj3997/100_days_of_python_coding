import turtle as t
import random

tim = t.Turtle()
screen = t.Screen()
tim.shape('turtle')
tim.speed(0)
tim.pensize(3)
t.colormode(255)


def color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


def draw_spirograph(gap):
    for _ in range(int(360/gap)):
        tim.lt(gap)
        tim.color(color())
        tim.circle(100)


draw_spirograph(35)
draw_spirograph(5)
screen.exitonclick()
