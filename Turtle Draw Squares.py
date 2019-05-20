import turtle
import random


my_screen = turtle.Screen()
my_screen.setup(0.5,0.75,0,0)
my_turtle = turtle.Turtle()

def square_placement(xposition, yposition):
    my_turtle.pu()
    my_turtle.setx(xposition)
    my_turtle.sety(yposition)
    my_turtle.pd()


def draw_square(xposition, yposition, length):
    square_placement(xposition, yposition)
    my_turtle.setheading(90)
    my_turtle.fd(length)
    my_turtle.setheading(180)
    my_turtle.fd(length)
    my_turtle.setheading(270)
    my_turtle.fd(length)
    my_turtle.setheading(360)
    my_turtle.fd(length)
    my_turtle.setheading(0)
    my_turtle.pu()

for i in range(0,200):
    a = random.randint(0,200)
    b = random.randint(0,200)
    c = random.randint(0,200)
    draw_square(a,b,c)

