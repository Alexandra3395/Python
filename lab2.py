'''import turtle

turtle.shape('turtle')
NOL = [100, 200, 100, 200]
ODIN = [150,200]
turtle.penup()
turtle.goto(-400,0)
for i in range(len(NOL)):
    turtle.pendown()
    turtle.forward(NOL[i])
    turtle.left(90)

turtle.penup()
turtle.goto(-250,100)
turtle.pendown()
turtle.left(45)
turtle.forward(ODIN[0])
turtle.right(135)
turtle.forward(ODIN[1])'''
from random import randint
import turtle


number_of_turtles = 5
steps_of_time_number = 100


pool = [turtle.Turtle(shape='turtle') for i in range(number_of_turtles)]
for unit in pool:
    unit.penup()
    unit.speed(50)
    unit.goto(randint(-200, 200), randint(-200, 200))


for i in range(steps_of_time_number):
    for unit in pool:
        unit.forward(2)
input()