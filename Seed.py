class Seed:
    
    SEED_FIELDS = ['(Seed) PAKE', '(Seed) 538 Mean', '(Seed) 538 Median', '(Seed) 538 Range']
    
    def __init__(self, seed: int, seed_stats: dict):
        self.seed = seed
        self.stats = {}
        
        for field in Seed.SEED_FIELDS:
            self.stats[field] = seed_stats.get(field,None)
        
        
    def get_stats(self):
        return self.stats
    
    def __str__(self):
        return f"For Seed {self.seed}, the ratings are as follows:\n\t{self.stats}"