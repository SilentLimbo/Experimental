import math 

class Circle:
    # Construct a circle object 
    def __init__(self, radius = 1):
        self.__radius = radius

    def getRadius(self):
        return self.__radius

    def setRadius(self,radius):
        self.__radius=radius

    def getPerimeter(self):
        return 2 * self.__radius * math.pi

    def getArea(self):
        return self.__radius * self.__radius * math.pi
      
def main():
    # Create a circle with radius 1
    
    circle1 = Circle()
    print("The area of the circle of radius",
        circle1.getRadius(), "is", circle1.getArea())

    # Create a circle with radius 25
    circle2 = Circle(25)
    print("The area of the circle of radius",
        circle2.getRadius(), "is", circle2.getArea())

    # Create a circle with radius 125
    circle3 = Circle(125)
    print("The area of the circle of radius",
        circle3.getRadius(), "is", circle3.getArea())

    # Modify circle radius
    circle2.radius=100
    print()
    print("Direct access when radius is private does not change from 25 to 100")
    print("The area of the circle of radius", 
        circle2.getRadius(), "is", circle2.getArea())

    circle2.setRadius(5)
    print()
    print("Private data member can only be access via a mutator method- setradius()")
    print("The area of the circle of radius", 
        circle2.getRadius(), "is", circle2.getArea())
    
main() # Call the main function

'''
>>> 
The area of the circle of radius 1 is 3.141592653589793
The area of the circle of radius 25 is 1963.4954084936207
The area of the circle of radius 125 is 49087.385212340516
The area of the circle of radius 25 is 1963.4954084936207
The area of the circle of radius 5 is 78.53981633974483
>>> 
'''
