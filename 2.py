import math
class circle():
    def __init__(self,radius,color):
        self.radius = radius 
        self.color = color

    def GetRadius(self):
        return self.radius
        
    def GetColor(self):
        return self.color

    def GetArea(self): 
        return (self.radius**2)* math.pi
        
    def SetRadius(self):
        return self.radius
    
    def SetColor(self):
        return self.color

class cilinder(circle):
    def __init__(self,height):
        self.height = height

    def Volume(self):
        return(self.GetArea * self.height)


Lingkaran = circle (2,"red")
