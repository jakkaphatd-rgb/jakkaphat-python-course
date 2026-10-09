"""
    สร้าง class Rectangle โดยกำหนดให้
    - มี attribute ชื่อ length และ width ที่เก็บข้อมูลความยาวและความกว้างของสี่เหลี่ยม
    - มี method ชื่อ get_area() ที่คืนค่าพื้นที่ของสี่เหลี่ยม
    - มี method ชื่อ get_perimeter() ที่คืนค่ารอบรูปของสี่เหลี่ยม
"""

"""
    สร้าง class Rectangle โดยกำหนดให้
    - มี attribute ชื่อ length และ width ที่เก็บข้อมูลความยาวและความกว้างของสี่เหลี่ยม
    - มี method ชื่อ get_area() ที่คืนค่าพื้นที่ของสี่เหลี่ยม
    - มี method ชื่อ get_perimeter() ที่คืนค่ารอบรูปของสี่เหลี่ยม
"""

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    # Method to get the area
    def get_area(self):
        return self.length * self.width

    # Method to get the perimeter
    def get_perimeter(self):
        return 2 * (self.length + self.width)


rect = Rectangle(10, 5)
print(rect.get_area())       # Should print 50
print(rect.get_perimeter())  # Should print 30



""" 
ขอให้เขียนคลาส circle ที่ทำงานคล้ายคลึงกับคลาส rectangle พร้อมตัวอย่าง
"""
class Circle:

    def __init__(self, radius):
        self.radius = radius

    # Method to get the area
    def get_area(self):
        return 3.1416 * self.radius * self.radius

    # Method to get the perimeter
    def get_perimeter(self):
        return 2 * 3.1416 * self.radius


circle = Circle(10)
print(circle.get_area())       # Should print 314.16
print(circle.get_perimeter())  # Should print 62.832
 

