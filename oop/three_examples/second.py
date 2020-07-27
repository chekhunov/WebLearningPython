class Door:
    def __init__(self, color, loop, length, width):
        self.__color = color
        self.__loop = loop
        self.__length = length
        self.__width = width

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, c):
        self.__color = c

    @property
    def loop(self):
        return self.__loop

    @loop.setter
    def loop(self, lo):
        self.__loop = lo

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, le):
        self.__length = le

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, w):
        self.__width = w

    def info(self):
        print("Door")
        print("Color: " + self.__color)
        print("Loop: " + str(self.__loop))
        print("Length: " + str(self.__length))
        print("Width: " + str(self.__width))


class Glass(Door):
    def __init__(self, color, loop, length, width, glass):
        super().__init__(color, loop, length, width)
        self.__glass = glass

    @property
    def glass(self):
        return self.__glass

    @glass.setter
    def glass(self, gl):
        self.__glass = gl

    def info(self):
        print("Glass")
        print("Color: " + self.color)
        print("Loop: " + str(self.loop))
        print("Length: " + str(self.length))
        print("Width: " + str(self.width))
        print("Width: " + self.__glass)


dor = Door("green", 2, 1, 2.1)
dor.info()

glass_door = Glass("green", 2, 1, 2.1, "satin")
glass_door.info()
