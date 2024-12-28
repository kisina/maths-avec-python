def setup():
    size(600,600)
    
def draw():
    """for i in range(10):
        translate(10, 10)
        rect(20, 40, 50, 30)
    """
    translate(width/2, height/2)
    for i in range(12):
        #ellipse(200,0,50,50)
        rect(200, 0, 50, 50)
        rotate(radians(360/12))
    
