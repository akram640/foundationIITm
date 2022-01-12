class Vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def print(self):
        print(f'({self.x},{self.y})')

    def magnitude(self):
        return (self.x**2+self.y**2)**0.5

    def scale(self,s):
        self.x = self.x*s
        self.y = self.y*s

    def rotate_xaxis(self):
        self.y = -self.y

    def rotate_yaxis(self):
        self.x = -self.x

    def add(self,P):
        result = Vector(0,0)
        result.x = self.x + P.x
        result.y = self.y + P.y
        return result

## Collection of Vectors

triangle = [Vector(0,1),Vector(1,3),Vector(3,0)]
