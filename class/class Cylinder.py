class Cylinder():
    def __init__(self, height="", radius=""):
        self.height = height
        self.radius = radius
    def volume(self):
        return self.height*(3.14)*(self.radius)**2
    def surface_area(self):
        top = (3.14)*(self.radius)**2
        return 2*top + 2*3.14*self.radius*self.height

height = input("Please input height of Cylinder: ")
radius = input("Please input radius of Cylinder: ")
c = Cylinder(height,radius)
print "Volume of cylinder: ", c.volume()
print "Surface area of cylinder: ", c.surface_area()
