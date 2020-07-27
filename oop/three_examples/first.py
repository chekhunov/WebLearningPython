class Car:
    def __init__(self, color, weight):
        self.__color = color
        self.__weight = weight

    @property
    def color(self):
        return self.__color

    @property
    def weight(self):
        return self.__weight

    @color.setter
    def color(self, c):
        self.__color = c

    @weight.setter
    def weight(self, w):
        self.__weight = w

    def info(self):
        print("Car")
        print("Color: " + self.__color)
        print("Weight: " + self.__weight)


class Larry(Car):
    def __init__(self, color, weight, wheel):
        super().__init__(color, weight)
        self.__wheel = wheel

    @property
    def wheel(self):
        return self.__wheel

    @wheel.setter
    def wheel(self, w):
        if w > 0:
            self.__wheel = w
        else:
            raise ValueError

    def info(self):
        print("Larry")
        print("Color: " + self.color)
        print("Weight: " + self.weight)
        print("Wheel: " + str(self.wheel))


car = Car("black", "3t")
car.info()

larry = Larry("yellow", "2t", 6)
larry.info()
