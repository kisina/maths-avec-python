from turtle import *

shape('turtle')

longueur = 30
nombre_cotes = 5

for i in range(nombre_cotes):
    forward(longueur)
    right(360/nombre_cotes)


done()
