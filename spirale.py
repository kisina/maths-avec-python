from turtle import *

# tracer(0)

length = 1
angle = 30

penup()
goto(400, 0)
pendown()

for i in range(351):
    angle = angle * 0.995
    length = length * 1.01
    right(angle)
    forward(length)


for i in range(351):
    angle = angle / 0.995
    length = length / 1.01
    left(angle)
    forward(length)


update()

done()