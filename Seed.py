"""
This is a class definition for Seed. It will hold 4 stats all from 538. 
This is to get the historic performance of the seed in our data for the team
"""

class Seed:
    
    SEED_FIELDS = ['(Seed) PAKE', '(Seed) 538 Mean', '(Seed) 538 Median', '(Seed) 538 Range']
    
    def __init__(self, seed: int, seed_stats: dict):
        self.seed = seed
        self.stats = {}
        
        for field in Seed.SEED_FIELDS:
            self.stats[field] = seed_stats.get(field,None)
        
        
    def get_stats(self):
        return self.stats
    
    # To string for debugging with print statements
    def __str__(self):
        return f"For Seed {self.seed}, the ratings are as follows:\n\t{self.stats}"