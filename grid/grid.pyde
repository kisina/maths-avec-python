

def setup():
    global xscl, yscl
    size(600,600)
    xscl = width / rangex
    yscl = -height / rangey

def draw():
    # Paramètre l'intervalle des x
    xmin = -10
    xmax = 1
    
    # Paramètre l'intervalle des y
    ymin = -10
    ymax = 10
    
    # Calcul l'intervalle
    rangex = xmax - xmin
    rangey = ymax - ymin
    global xscl, yscl
    background(255) # blanc
    translate(width/2, height/2)
    # lignes de couleur cyan
    strokeWeight(1)
    stroke(0,255,255)
    for i in range(xmin, xmax + 1):
        line(i*xscl,ymin*yscl,i*xscl,ymax*yscl)
    for i in range(ymin, ymax + 1):
        line(xmin*xscl, i*yscl, xmax*xscl, i*yscl)
        
