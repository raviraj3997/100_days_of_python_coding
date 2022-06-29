from turtle import Turtle, Screen, colormode
import random

# ----------------------------------
# drawing Random walk of the turtle with random r g b color.
# ----------------------------------
screen = Screen()


tom = Turtle()
colormode(255)
tom.speed(0)
tom.shape('turtle')
tom.color("green")

angles = [0, 90, 180, 270]
tom.pensize(10)
screen.colormode(255)


def color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


def step2():
    tom.forward(50)
    tom.setheading(random.choice(angles))
    color_new = color()
    tom.color(color_new)


for _ in range(100):
    step2()

screen.exitonclick()