from turtle import *

shape('turtle')

def polygon(sides=4, side_length=100):
    for i in range(sides):
        forward(side_length)
        right(360/sides)


"""for i in range(3, 17):
    polygon(i, 50)
"""

polygon(42, 5)

"""forward(100)
right(90)
forward(100)"""

done()