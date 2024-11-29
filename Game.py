from Team import Team


class Game:
    def __init__(self, year, team1: Team, team2: Team, score_differential):
        
        self.year = year
        self.team1 = team1
        self.team2 = team2
        self.score_differential = score_differential
    
    def get_game_stats_dict(self):
        game_stats_dict = {
            "year": self.year
        }
        
        for key, val in self.team1.get_all_stats().items():
            game_stats_dict["TEAM 1 " + key] = val
            
        for key, val in self.team2.get_all_stats().items():
            game_stats_dict["TEAM 2 " + key] = val
            
        # Add score differential to the list
        game_stats_dict["Margin of Victory/Defeat"] = self.score_differential
        
        return game_stats_dict
        
        
    
    def __str__(self):
        return f"Team 1 : {self.team1}\nTeam 2: {self.team2}\nScore Differential: {self.score_differential}"

    