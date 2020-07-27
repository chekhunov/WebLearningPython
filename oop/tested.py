

class Rectangle:
    default_color = "green"

    def __init__(self, width, height):
        self.width = width
        self.height = height


a = Rectangle.default_color
print(a)

rect = Rectangle(10,20)
print(rect.width)
print(rect.height)

Rectangle.default_color = "red"
print(Rectangle.default_color)

r1 = Rectangle(1,2)
r2 = Rectangle(10,20)
print(r1.default_color)
print(r2.default_color)

r1.default_color = "blue"
print(r1.default_color)
print(r2.default_color)
