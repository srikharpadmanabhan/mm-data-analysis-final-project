from Conference import Conference
from Seed import Seed


class Team:
    
    # declare static variable to indicate which fields to add for the init function
    STATS_538_FIELDS = ["(Team) 538 Power Rating", "(Team) 538 Power Rank"]
    RESUME_FIELDS = ['(Resumes) NET RPI', '(Resumes) RESUME', '(Resumes) WAB RANK', '(Resumes) ELO', '(Resumes) B POWER', '(Resumes) Q1 W', '(Resumes) Q2 W', '(Resumes) Q3 Q4 L', '(Resumes) PLUS 500', '(Resumes) R SCORE']
    SHOOTING_SPLITS_FIELDS = ['(Shooting Splits) DUNKS FG%', '(Shooting Splits) DUNKS SHARE', '(Shooting Splits) DUNKS FG%D', '(Shooting Splits) DUNKS D SHARE', '(Shooting Splits) CLOSE TWOS FG%', '(Shooting Splits) CLOSE TWOS SHARE', '(Shooting Splits) CLOSE TWOS FG%D', '(Shooting Splits) CLOSE TWOS D SHARE', '(Shooting Splits) FARTHER TWOS FG%', '(Shooting Splits) FARTHER TWOS SHARE', '(Shooting Splits) FARTHER TWOS FG%D', '(Shooting Splits) FARTHER TWOS D SHARE', '(Shooting Splits) THREES FG%', '(Shooting Splits) THREES SHARE', '(Shooting Splits) THREES FG%D', '(Shooting Splits) THREES D SHARE']
    KENPOM_FIELDS = ['(Team) K TEMPO RANK', '(Team) KADJ T RANK', '(Team) KO RANK', '(Team) KADJ O RANK', '(Team) KD RANK', '(Team) KADJ D RANK', '(Team) KADJ EM RANK', '(Team) BADJ EM RANK', '(Team) BADJ O RANK', '(Team) BADJ D RANK', '(Team) BARTHAG RANK', '(Team) EFG% RANK', '(Team) EFGD% RANK', '(Team) FTR RANK', '(Team) FTRD RANK', '(Team) TOV% RANK', '(Team) TOV%D RANK', '(Team) OREB% RANK', '(Team) DREB% RANK', '(Team) OP OREB% RANK', '(Team) OP DREB% RANK', '(Team) RAW T RANK', '(Team) 2PT% RANK', '(Team) 2PT%D RANK', '(Team) 3PT% RANK', '(Team) 3PT%D RANK', '(Team) BLK% RANK', '(Team) BLKED% RANK', '(Team) AST% RANK', '(Team) OP AST% RANK', '(Team) 2PTR RANK', '(Team) 3PTR RANK', '(Team) 2PTRD RANK', '(Team) 3PTRD RANK', '(Team) BADJT RANK', '(Team) AVG HGT RANK', '(Team) EFF HGT RANK', '(Team) EXP RANK', '(Team) TALENT RANK', '(Team) FT% RANK', '(Team) OP FT% RANK', '(Team) PPPO RANK', '(Team) PPPD RANK', '(Team) ELITE SOS RANK']
    HISTORIC_TEAM_FIELDS = ['(Historic Team) 538 Rating size', '(Historic Team) 538 Rating mean', '(Historic Team) 538 Rating median', '(Historic Team) 538 Rating range']
    # Construct Team and the stats dictionary from the various accumulated stats
    def __init__(self, team_name, seed: Seed, conference: Conference, year, team_stats_538, resume_stats, shooting_splits_stats, kenpom_stats, historic_team_stats):
        
        self.team_name = team_name
        self.seed = seed
        self.conference = conference
        self.year = year
        
        self.stats = {}
        
        for field in Team.STATS_538_FIELDS:
            self.stats[field] = team_stats_538.get(field,None)
        
        for field in Team.KENPOM_FIELDS:
            self.stats[field] = kenpom_stats.get(field,None)
        
        for field in Team.SHOOTING_SPLITS_FIELDS:
            self.stats[field] = shooting_splits_stats.get(field,None)
            
        for field in Team.RESUME_FIELDS:
            self.stats[field] = resume_stats.get(field,None)
        
        for field in Team.HISTORIC_TEAM_FIELDS:
            self.stats[field] = historic_team_stats.get(field,None)
        
    """
    This function retrieves all stats for the team including the conference and seed stats. We also add the name of the team 
    """
    def get_all_stats(self):
        
        name_dict = {
            "Name": self.team_name
        }
        
        
        merged_stats = {**name_dict,**self.stats, **self.seed.stats, **self.conference.stats}
        
        return merged_stats
        
        
    # For debugging purposes to ensure that the seed retrieves the right data within the team
    def get_seed_stat(self, stat_name: str):
        return self.seed.get_stat(stat_name)

    # To string function that will allow us to get the stats for a team just by printing it.
    # Useful for debugging purposes
    def __str__(self):
        return f"{self.team_name} in {self.year} playing in the {self.conference.conference_name} with the following stats: {self.stats}"
        