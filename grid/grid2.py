strokeWeight(1) # Lignes de couleur cyan
stroke(0,255,255)
for i inrange(xmin,xmax+1):
    line(i*xscl,ymin*yscl,i*xscl,ymax*yscl)
for i in range(ymin, ymax + 1):
    line(xmin*xscl, i*yscl, xmax*xscl, i*yscl)
stroke(0) # Axes noirs
line(0,ymin*yscl,0,ymax*yscl)
line(xmin*xscl,0,xmax*xscl,0)
