from Team import Team


class Game:
    def __init__(self, year, team1: Team, team2: Team, score_differential):
        
        self.year = year
        self.team1 = team1
        self.team2 = team2
        self.score_differential = score_differential

    