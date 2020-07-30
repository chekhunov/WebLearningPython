class Squad:
    __commander_name = ""
    __soldiers_count = 0
    __location = ""
    __armament = ""  # вооружение

    def __init__(self, squad_name):
        self.__squad_name = squad_name

    @property
    def commander_name(self):
        return self.__commander_name

    @property
    def squad_name(self):
        return self.__squad_name

    @property
    def soldiers_count(self):
        return self.__soldiers_count

    @property
    def location(self):
        return self.__location

    @property
    def armament(self):
        return self.__armament

    @squad_name.setter
    def squad_name(self, sc):
        self.__squad_name = sc

    @soldiers_count.setter
    def soldiers_count(self, sol_count):
        self.__soldiers_count = sol_count

    @commander_name.setter
    def commander_name(self, com_name):
        self.__commander_name = com_name

    @location.setter
    def location(self, lc):
        self.__location = lc

    @armament.setter
    def armament(self, arm):
        self.__armament = arm
