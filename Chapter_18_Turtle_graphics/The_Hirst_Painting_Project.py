"""This code will not work in repl.it as there is no access to the colorgram package here.###
   We talk about this in the video tutorials"""
import colorgram
import turtle as t
import random

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_colors.append((r, g, b))

print(rgb_colors)

tim = t.Turtle()
screen = t.Screen()
t.colormode(255)


def create_dot(turtle, dot_size):
    turtle.dot(dot_size, random.choice(rgb_colors))


def create_grid(turtle, grid_size, gap):
    turtle.penup()
    turtle.setpos(-grid_size*gap/2, -grid_size*gap/2)
    for i in range(1, grid_size+1):
        v_pos = i*gap
        for _ in range(grid_size):
            turtle.forward(gap)
            create_dot(turtle, gap/2)
        turtle.lt(90)
        turtle.forward(gap)
        turtle.lt(90)
        turtle.forward(grid_size*gap)
        turtle.lt(90)
        turtle.lt(90)


create_grid(turtle=tim, grid_size=5, gap=40)


screen.exitonclick()
