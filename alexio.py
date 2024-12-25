"""i = 0
while True:
    i = i + 1
    print(f"salut {i} fois")"""

"""
a = 16736872
b = 237298732

resultat = a + b

print(resultat)
"""

from turtle import *

shape('turtle')

forward(20)

for i in range(4):
    length = (i+1) * 5
    for i in range(36):
        right(10)
        forward(length)

for i in range(4):
    length = (i+1) * 5
    for i in range(36):
        left(10)
        forward(length)

circle(200)

done()
