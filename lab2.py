
from random import randint
import turtle


number_of_turtles = 7
steps_of_time_number = 100


pool = [turtle.Turtle(shape='turtle') for i in range(number_of_turtles)]
for unit in pool:
    unit.penup()
    unit.speed(50)
    unit.goto(randint(-200, 200), randint(-200, 200))


for i in range(steps_of_time_number):
    for unit in pool:
        unit.forward(2)
        
for count_square in range(15):
    size = 100 - count_square*5
    for j in range(4):
        turtle.pendown()
        turtle.forward(size)
        turtle.right(90)
    turtle.penup()
    turtle.forward(3)
    turtle.right(90)
    turtle.forward(3)
    turtle.left(90)
input()
