import math
class Shape:
    def area(self):
        raise NotImplementedError("This method should be overridden in subclasses")
    def peri(self):
        raise NotImplementedError("This method should be overridden in subclasses")
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return math.pi*(self.radius**2)
    def peri(self):
        return 2*math.pi*self.radius
class Triangle(Shape):
    def __init__(self,base,height,side1,side2):
        self.base=base
        self.height=height
        self.side1=side1
        self.side2=side2
    def area(self):
        return 0.5*self.base*self.height
    def peri(self):
        return self.base+self.side1+self.side2
class Square(Shape):
    def __init__(self,side):
        self.side=side
    def area(self):
        return self.side*self.side
    def peri(self):
        return 4*self.side
def main():
    circle=Circle(5)
    print("Circle Area:",circle.area())
    print("Circle Perimeter:",circle.peri())
    triangle=Triangle(5,3,4,5)
    print("Triangle Area:",triangle.area())
    print("Triangle Perimeter:",triangle.peri())
    square=Square(5)
    print("Square Area:",square.area())
    print("Square Perimeter:",square.peri())
    
    