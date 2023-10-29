
import turtle
from turtle import Turtle, Screen
import random

color_list = [(198, 13, 32), (248, 236, 25), (40, 76, 188), (39, 216, 69), (238, 227, 5), (227, 159, 49), (29, 40, 154),
              (212, 76, 15), (17, 153, 17), (241, 36, 161), (195, 16, 12), (223, 21, 120), (68, 10, 31), (61, 15, 8),
              (223, 141, 206), (11, 97, 62), (219, 159, 11), (54, 209, 229), (19, 21, 49), (238, 157, 216),
              (79, 74, 212), (10, 228, 238), (73, 212, 168), (93, 233, 198), (65, 231, 239), (217, 88, 51)]

turtle.colormode(255)
tim = Turtle()
screen = Screen()
color_number = len(color_list)
screen.setup(900, 900)
tim_position = tim.pos()
tim.penup()
tim.setposition(-275, -275)
x = tim.xcor()
tim.hideturtle()
tim.speed("fastest")


def draw(color_list_index):
    tim.forward(50)
    tim.pendown()
    dot_color = color_list[random.randint(0, color_number - 1)]
    tim.dot(20, dot_color)
    tim.penup()


def new_line(x_axis):
    y = tim.ycor()
    y += 50
    tim.setposition(x_axis, y)


for step in range(10):
    for _ in range(10):
        draw(color_number)
    new_line(x)

screen = Screen()
screen.exitonclick()
