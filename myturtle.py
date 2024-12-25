from turtle import *
shape("turtle")

tracer(0)

def square(side_length=100):
    for i in range(4):
        forward(side_length)
        right(90)

def triangle(side_length=100):
    for i in range(3):
        forward(side_length)
        right(120)

def polygon(sides=4, side_length=100):
    for i in range(sides):
        forward(side_length)
        right(360/sides)

def star(side_length=100):
    for i in range(5):
        forward(side_length)
        right(144)

"""for i in range(72):
    left(5)
    square(150)
"""

"""for i in range(72):
    left(5)
    square()
"""

"""
length = 5
for i in range(60):
    right(5)
    square(length)
    length += 5
"""

# triangle(100)

# polygon(4, 30)

"""for i in range(3, 16):
    polygon(i, 40)
"""

#star()

length = 5
for i in range(100):
    right(5)
    triangle(length)
    length += 5

setposition(-2*length, 0)
length = 5
for i in range(100):
    right(5)
    triangle(length)
    length += 5


update()

done()