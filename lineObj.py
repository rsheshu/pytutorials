import math as Math
class Line(object):
    def __init__(self,coord1, coord2):
        self.x1, self.y1 = coord1
        self.x2, self.y2 = coord2
        self.disat = 0
    def dist(self):

        X  = (self.x2-self.x1)**2
        Y = (self.y2 - self.y1) ** 2
        self.disat = Math.sqrt(X + Y)
        return self.disat

coord1 = (3, 2)
coord2 = (8, 10)

liner = Line(coord1, coord2)
print(liner.dist())
