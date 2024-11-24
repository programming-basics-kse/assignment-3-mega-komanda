class Info:
    def __init__(self, id, name, team, NOC, games, year, season, city, sport, event, medal):
        self.id = id
        self.name = name
        self.team = team
        self.NOC = NOC
        self.games = games
        self.year = year
        self.season = season
        self.city = city
        self.sport = sport
        self.event = event
        self.medal = medal

    def return_stat(self):
        return f"{self.name} - {self.event} - {self.medal}"

    def medal_to_num(self):
        if self.medal == "Gold":
            return 1
        if self.medal == "Silver":
            return 2
        if self.medal == "Bronze":
            return 3
        return 0

    def __str__(self):
        return f"{self.id}, {self.name}, {self.team}, {self.NOC}, {self.games}, {self.year}, {self.season}, {self.city}, {self.sport}, {self.event}, {self.medal}"
