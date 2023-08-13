import math



class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def __str__(self):
        rec = "Rectangle(width=" + str(self.width) + ", height=" + str(self.height) + ")"
        return rec


    def set_width(self, width):
        self.width = width
        self.side = width
    def set_height(self, height):
        self.height = height
        self.side = height
    def get_area(self):
        area = self.width * self.height
        return area
    def get_perimeter(self):
        perimeter = 2 * self.width + 2* self.height
        return perimeter
    def get_diagonal(self):
        diagonal = (self.width ** 2 + self.height ** 2) ** .5
        return diagonal
    def get_picture(self):
        w =str(int(self.width)* "*")
        h = str(int(self.height) * ( w + "\n"))
        return h
    def get_amount_inside(self, shape):
        area_main = self.get_area()
        area_pass = shape.get_area()
        amount_passed = math.trunc(area_main / area_pass)
        return amount_passed



class Square(Rectangle):
    def __init__(self, side):
        self.side = side
        self.width = side
        self.height = side

    def __str__(self):
        squr = "Square(side=" + str(self.side)  + ")"
        return squr

    def set_side(self, side):
        self.side = side
        self.width = side
        self.height = side
