from math import sqrt

def quad(a, b, c):
    ''' Retourne les solutions de l'équation ax² + bx + c = 0 '''
    x1 = (-b + sqrt(b**2 - 4*a*c)) / (2*a)
    x2 = (-b - sqrt(b**2 - 4*a*c)) / (2*a)
    return x1, x2

print(quad(2,7,-15))

