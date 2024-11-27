class Seed:
    def __init__(self, seed, seed_stats, historical_seed_performance):
        self.seed = seed
        self.seed_stats = seed_stats
        self.historical_seed_performance = historical_seed_performance
        
    def get_stat(self, stat_name: str):
        if stat_name in self.seed_stats:
            return self.seed_stats[stat_name]
        else:
            return None