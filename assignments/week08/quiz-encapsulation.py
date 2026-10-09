"""
Write a Python class Rectangle with:

Private attributes for length and width
Methods to calculate area (getArea()) and perimeter getPerimeter())
A method to check if it's a square (isSquare())

"""

class Rectangle:
 
    def __init__(self, length, width):
        self.__length = length
        self.__width = width
 
    def getArea(self):
        return self.__length * self.__width
 
    def getPerimeter(self):
        return 2 * (self.__length + self.__width)
 
    def isSquare(self):
        return self.__length == self.__width
 
 
# Create an object
 
r1 = Rectangle(5, 5)
print("Area:", r1.getArea())
print("Perimeter:", r1.getPerimeter())
print("Is Square:", r1.isSquare())