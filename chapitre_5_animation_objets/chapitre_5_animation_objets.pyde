t = 0

def setup():
    size(600,600)
    rectMode(CENTER)
    
def draw():
    global t
    background(255)
    translate(width/2, height/2)
    rotate(radians(t))
    for i in range(12):
        pushMatrix() # Sauvegarde l'orientation
        translate(200, 0)
        rotate(radians(6*t))
        rect(0, 0, 50, 50)
        popMatrix() # Restitue l'orientation
        rotate(radians(360/12))
    t += 0.1
    
