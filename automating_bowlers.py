import pandas as pd

df = pd.read_csv('IPL.csv',low_memory=False)

class MatchExtraction:
    def data_extraction(self,venue,bowler,location):
        all_rows = []
        bowlers = bowler
        for j in range(len(bowlers)):
            row = {}

            filtered_data = df[
                (df['bowler'] == bowlers[j]) &
                (df['venue'] == venue)  # standardized name
                ]

            total_balls = filtered_data.shape[0]
            total_runs_conceded = filtered_data['runs_bowler'].sum()
            wickets = filtered_data[
                filtered_data['striker_out'] == True
                ].shape[0]

            bowling_avg = round(total_runs_conceded / total_balls, 2) if total_balls > 0 else 0
            economy = round((total_runs_conceded / total_balls) * 6, 2) if total_balls > 0 else 0

            row[f'balls'] = total_balls
            row[f'runs_conceded'] = total_runs_conceded
            row[f'wickets'] = wickets
            row[f'bowling_avg'] = bowling_avg
            row[f'economy'] = economy
            row['h2h'] = 1 if total_balls > 0 else 0
            all_rows.append(row)

        result = pd.DataFrame(all_rows, index=bowlers)
        result.to_csv(location)
