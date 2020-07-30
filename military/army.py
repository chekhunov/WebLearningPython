from military.squad import Squad

DEFAULT_COUNT_OFFICERS = 1


class Army:
    troop_types = ["Медицина", "Ремонтные", "Ракетные", "Разведка"]
    total_soldiers = 0
    total_officers = 0
    general_name = "Gukov"
    squads = []

    def __init__(self, name_army):
        self.name_army = name_army

    def tread_on(self):
        print("Attack")

    def fall_back(self):
        print("Back")

    def add_new_recruits(self, squad_name: str, recruits_count: int):
        if not self.squads:
            raise Exception("No squad")

        for squad in self.squads:
            if squad["name"] == squad_name:
                squad["soldiers_count"] += recruits_count
                self.__sum_soldiers(recruits_count)
                break

    def set_new_commander_of_squad(self, squad_name: str, commander_name: str):
        if not self.squads:
            raise Exception("No squad")

        for squad in self.squads:
            if squad["name"] == squad_name:
                squad["commander_name"] = commander_name
                break

    def __sum_soldiers(self, new_soldiers: int):
        self.total_soldiers += new_soldiers

    def __sum_officers(self, new_officers: int):
        self.total_officers += new_officers

    def add_squad(self, squad_name: str, commander_name: str, soldiers_count: int, location: str,
                  armament: str, type_troop: str):
        if type_troop not in self.troop_types:
            raise ValueError("wrong type")

        squad = Squad(squad_name)
        squad.commander_name = commander_name
        squad.soldiers_count = soldiers_count
        squad.location = location
        squad.armament = armament

        squad = {"name": squad.squad_name,
                 "commander_name": squad.commander_name,
                 "soldiers_count": squad.soldiers_count,
                 "armament": squad.armament,
                 "location": squad.location,
                 "type_troop": type_troop}

        self.squads.append(squad)
        self.__sum_officers(DEFAULT_COUNT_OFFICERS)
        self.__sum_soldiers(soldiers_count)


army = Army("Nato")

print(army.name_army)
print(army.squads)
print(army.total_officers)
print(army.total_soldiers)
print(army.general_name)
print("---------------------------")
army.add_squad("Alfa", "Filatov", 100, "Стрелковое оружие", "Kharkov", "Медицина")
print(army.name_army)
print(army.squads)
print(army.total_officers)
print(army.total_soldiers)
print(army.general_name)
print("---------------------------")

army.add_new_recruits("Alfa", 50)
print(army.name_army)
print(army.squads)
print(army.total_officers)
print(army.total_soldiers)
print(army.general_name)
print("---------------------------")

army.add_squad("SS", "Shultz", 2,"Пистолеты", "Berlin", "Разведка")
print(army.name_army)
print(army.squads)
print(army.total_officers)
print(army.total_soldiers)
print(army.general_name)
print("---------------------------")

army.set_new_commander_of_squad("SS", "Gitler")
print(army.name_army)
print(army.squads)
print(army.total_officers)
print(army.total_soldiers)
print(army.general_name)
print("---------------------------")

army.general_name = "Grisha"
