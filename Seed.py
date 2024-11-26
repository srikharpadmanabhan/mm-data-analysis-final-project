class Seed:
    def __init__(self, seed, seed_stats):
        self.seed = seed
        self.seed_stats = seed_stats
        
    def get_stat(self, stat_name: str):
        if stat_name in self.seed_stats:
            return self.seed_stats[stat_name]
        else:
            return None