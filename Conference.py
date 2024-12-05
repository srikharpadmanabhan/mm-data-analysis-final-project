
"""
This is the class definition for a conference, it will hold the conference name and some stats defined as
CONFERENCE_FIELDS. Useful to hold conference data in the Team class.
"""
class Conference:
    CONFERENCE_FIELDS = ['(Conference) BADJ EM', '(Conference) BADJ O', '(Conference) BADJ D', '(Conference) BARTHAG', '(Conference) G', '(Conference) WIN%', '(Conference) EFG%', '(Conference) EFGD%', '(Conference) FTR', '(Conference) FTRD', '(Conference) TOV%', '(Conference) TOV%D', '(Conference) OREB%', '(Conference) DREB%', '(Conference) OP OREB%', '(Conference) OP DREB%', '(Conference) RAW T', '(Conference) 2PT%', '(Conference) 2PT%D', '(Conference) 3PT%', '(Conference) 3PT%D', '(Conference) BLK%', '(Conference) BLKED%', '(Conference) AST%', '(Conference) OP AST %', '(Conference) 2PTR', '(Conference) 3PTR', '(Conference) 2PTRD', '(Conference) 3PTRD', '(Conference) BADJ T', '(Conference) AVG HGT', '(Conference) EFF HGT', '(Conference) EXP', '(Conference) TALENT', '(Conference) FT%', '(Conference) OP FT%', '(Conference) PPPO', '(Conference) PPPD', '(Conference) ELITE SOS', '(Conference) WAB']
    
    def __init__(self, conference_name: str, conference_stats):
        self.conference_name = conference_name
        self.stats = {}
        
        
        for field in Conference.CONFERENCE_FIELDS:
            self.stats[field] = conference_stats.get(field,None)
    
    # Return stats_dict to be used by Team to accumulate the necessary stats
    def get_stats_dict(self):
        return self.stats
    
    # Method to print conference for debugging
    def __str__(self):
        return f"Conference(name='{self.conference_name}', stats={self.stats})"