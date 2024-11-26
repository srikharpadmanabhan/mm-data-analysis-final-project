from Seed import Seed

class Team:
    def __init__(self, team_name, seed: Seed, year, team_stats):
        
        self.team_name = team_name
        self.seed = seed
        self.year = year
        self.team_stats = team_stats
        
    def get_team_stat(self, stat_name: str):
        
        if stat_name in self.team_stats:
            return self.team_stats[stat_name]
        else:
            return None
    
    def get_seed_stat(self, stat_name: str):
        return self.seed.get_stat(stat_name)
        