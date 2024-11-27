class Conference:
    def __init__(self, conference_name: str, conference_stats):
        self.conference_name = conference_name
        self.conference_stats = conference_stats
    
    def get_stats_dict(self):
        return self.conference_stats
    
    # Metehod to print conference for debugging
    def __str__(self):
        return f"Conference(name='{self.conference_name}', stats={self.conference_stats})"