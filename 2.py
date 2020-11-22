import math
class circle():
    def __init__(self,radius,color):
        self.radius = radius 
        self.color = color

    def GetRadius(self):
        return self.radius
        
    def GetColor(self):
        return self.GetColor

    def GetArea(self): 
        return (self.radius**2)* math.pi
        
class cilinder(circle):
    def __init__(self,height):
        self.height = height

    def Volume(self):
        return(self.GetArea * self.height)


Lingkaran = circle (2,"red")

print(Lingkaran.cilinder)