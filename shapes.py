class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self, length, width):
        return length * width

    def perimeter(self, length, width):
        return 2 * (length + width)


class Square(Rectangle):
    pass
