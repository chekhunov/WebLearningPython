class Computer:
    def __init__(self, processor, hdd, memory):
        self.__processor = processor
        self.__hdd = hdd
        self.__memory = memory

    @property
    def processor(self):
        return self.__processor

    @processor.setter
    def processor(self, pr):
        self.__processor = pr

    @property
    def hdd(self):
        return self.__hdd

    @hdd.setter
    def hdd(self, hd):
        self.__hdd = hd

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, mem):
        self.__memory = mem

    def info(self):
        print("Computer")
        print("Processor: " + self.__processor)
        print("Hdd: " + self.__hdd)
        print("Memory: " + self.__memory)


class Laptop(Computer):
    def __init__(self, processor, hdd, memory, screen_diagonal):
        super().__init__(processor, hdd, memory)
        self.__screen_diagonal = screen_diagonal

    @property
    def screen_diagonal(self):
        return self.__screen_diagonal

    @screen_diagonal.setter
    def screen_diagonal(self, sd):
        self.__screen_diagonal = sd

    def info(self):
        print("Laptop")
        print("Processor: " + self.processor)
        print("Hdd: " + self.hdd)
        print("Memory: " + self.memory)
        print("Screen_diagonal: " + str(self.__screen_diagonal))


comp = Computer("Intel", "250gb", "8gb")
comp.info()

laptop = Laptop("Intel", "250gb", "8gb", 15.5)
laptop.info()


