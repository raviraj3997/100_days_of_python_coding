from turtle import Turtle, Screen, colormode
import random

tim = Turtle()
screen = Screen()
tim.speed(0)
tim.shape('turtle')
tim.color("green")
color_list = ['alice blue', 'AliceBlue', 'antique white', 'AntiqueWhite', 'AntiqueWhite4', 'aquamarine', 'aquamarine1',
              'azure', 'azure1', 'azure2', 'beige', 'bisque', 'bisque3', 'bisque4', 'black', 'blanched almond',
              'BlanchedAlmond', 'blue', 'blue violet', 'blue1', 'blue4', 'BlueViolet', 'brown', 'brown1',
              'brown4', 'burlywood', 'burlywood3']
# ----------------------------------
# draw the square.
# ----------------------------------

# screen.clear()
for _ in range(4):
    tim.forward(100)
    tim.lt(90)

# ----------------------------------
# draw the dashed lines.
# ----------------------------------

# screen.clear()
for _ in range(4):
    for _ in range(10):
        tim.forward(10)
        tim.penup()
        tim.forward(10)
        tim.pendown()

    tim.lt(90)

# ----------------------------------
# drawing different Shapes.
# ----------------------------------
# screen.clear()


def draw_shape(num_edge):
    angle = 360/num_edge
    tim.color(random.choice(color_list))
    for i in range(num_edge):
        tim.forward(100)
        tim.rt(angle)


for number_edges in range(3, 20):
    draw_shape(number_edges)


# ----------------------------------
# drawing Random walk of the turtle.
# ----------------------------------
angles = [0, 90, 180, 270]


def step():
    tim.forward(25)
    next_move = random.choice([tim.lt, tim.rt])
    next_move(random.choice(angles))
    tim.color(random.choice(color_list))


tim.pensize(10)
for _ in range(100):
    step()

screen.exitonclick()
