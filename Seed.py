class Seed:
    def __init__(self, seed, seed_stats):
        self.seed = seed
        self.seed_stats = seed_stats
        
    def get_stats(self):
        return self.seed_stats
    
    def __str__(self):
        return f"For Seed {self.seed}, the ratings are as follows:\n\t{self.seed_stats}"