from turtle import *
from random import randint


speed(0)
shape("turtle")


def wander():
    orientation = 0
    while True:
        forward(3)
        if xcor() >= 200 or xcor() <= -200 or ycor() >= 200 or ycor() <= -200:
            backward(3)
            angle_rotation = randint(90, 180)
            left(angle_rotation)
            orientation = (orientation+angle_rotation) % 360
            print(orientation)
        if xcor() <= -200:
        if ycor() >= 200:
        if ycor() <= -200:
wander()

