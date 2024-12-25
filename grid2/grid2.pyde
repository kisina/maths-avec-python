# Paramètre l'intervalle des x
xmin = -10
xmax = 10

# Paramètre l'intervalle des y
ymin = -10
ymax = 10

# Calcul l'intervalle
rangex = xmax - xmin
rangey = ymax - ymin


def setup():
    global xscl, yscl
    size(600,600)
    xscl = width / rangex
    yscl = -height / rangey

def draw():
    global xscl, yscl
    background(255) # blanc
    translate(width/2, height/2)
    grid(xscl,yscl) # Trace la grille
    graphFunction()
    
    #Test avec un cercle
    #fill(0)
    #ellipse(3*xscl,6*yscl,10,10)
    
def grid(xscl,yscl):
    # Trace une grille graphique
    # Lignes de couleur cyan
    strokeWeight(1)
    stroke(0,255,255)
    for i in range(xmin, xmax + 1):
        line(i*xscl,ymin*yscl,i*xscl,ymax*yscl)
    for i in range(ymin, ymax + 1):
        line(xmin*xscl, i*yscl, xmax*xscl, i*yscl)
    stroke(0) # Axes noirs
    line(0,ymin*yscl,0,ymax*yscl)
    line(xmin*xscl,0,xmax*xscl,0)
    
    
def f(x):
    return x
    #return 6*x**3 + 3.1*x**2 + 3*x - 10
    #return 2*x**2 + 7*x - 15


def graphFunction():
    x = xmin
    stroke(255,0,0)
    while x <= xmax:
        fill(0)
        line(x*xscl,f(x)*yscl,(x+0.01)*xscl,f(x+0.01)*yscl)
        x += 0.01
