# _-доступ на прямую и через гет сет
# __-полностью закрыт доступ на прямую к переменной

class Rectangle:

    def __new__(cls, *args, **kwargs):
        print("Hello from __new__")
        return super().__new__(cls)

    def __init__(self, width, height):
        print("Hello from __init__")
        self.__width = width
        self.__height = height

    def get_width(self):
        return self.__width

    def set_width(self, w):
        self.__width = w

    def get_height(self):
        return self.__height

    def set_height(self, h):
        self.__height = h

    def area(self):
        return self.__width * self.__height


rect = Rectangle(10, 20)

print(rect.get_width())

#print(rect.__width) #не работает изза закрытого доступа на прямую

print(rect._Rectangle__width)

rect._Rectangle__width=20
print(rect.get_width())
