import pandas as pd

df = pd.read_csv('IPL.csv',low_memory=False)

def GrabTheData(team,year,month,date):
    all_matches = df.drop_duplicates('match_id')[['match_id','batting_team','bowling_team','year','month','day','match_won_by']].sort_values('day')

    past_matches = all_matches[(all_matches['bowling_team'] == team) | (all_matches['batting_team'] == team) &
                                ((all_matches['year'] == year) & (all_matches['month'] <= month) & (all_matches['day'] < date))].tail(5)
    n = 0
    if len(past_matches) == 0:
        return 0.5
    wins = len(past_matches[past_matches['match_won_by'] == team])
    print(wins)
