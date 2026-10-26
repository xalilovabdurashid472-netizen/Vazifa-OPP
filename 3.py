class Circle:
    def __init__(self,radius):
        self.radius=radius
    def  area(self):
        return 3.14*self.radius**2
    def diametr(self):
        return 2*self.radius

circle = Circle(5)
print(circle.area())
print(circle.diametr())