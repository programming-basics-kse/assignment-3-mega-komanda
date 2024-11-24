class Info:
    def __init__(self, id0, name1, team6, NOC7, games8, year9, season10, city11, sport12, event13, medal14):
        self.id0 = id0
        self.name1 = name1
        self.team6 = team6
        self.NOC7 = NOC7
        self.games8 = games8
        self.year9 = year9
        self.season10 = season10
        self.city11 = city11
        self.sport12 = sport12
        self.event13 = event13
        self.medal14 = medal14

    def return_stat(self):
        return f"{self.name1} - {self.event13} - {self.medal14}"

    def medal_to_num(self):
        if self.medal14 == "Gold":
            return 1
        if self.medal14 == "Silver":
            return 2
        if self.medal14 == "Bronze":
            return 3
        return 0

    def __str__(self):
        return f"{self.id0}, {self.name1}, {self.team6}, {self.NOC7}, {self.games8}, {self.year9}, {self.season10}, {self.city11}, {self.sport12}, {self.event13}, {self.medal14}"