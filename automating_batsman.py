import pandas as pd
df = pd.read_csv('IPL.csv',low_memory=False)

class data_extraction():
    def Function(self,venue,batsman_list, bowler_list, batsman_list2, bowler_list2,location):
        # Batsman stats ki file kaise banegi

        pitch_type = {
            # BATTING FRIENDLY
            'M Chinnaswamy Stadium': 'batting',
            'M. Chinnaswamy Stadium': 'batting',
            'M.Chinnaswamy Stadium': 'batting',  # ✅ added
            'Chinnaswamy Stadium': 'batting',
            'M Chinnaswamy Stadium': 'batting',
            'Royal Challengers Bangalore Stadium': 'batting',
            'Wankhede Stadium': 'batting',
            'Wankhede Stadium, Mumbai': 'batting',
            'Rajiv Gandhi International Stadium': 'batting',
            'Rajiv Gandhi International Stadium, Uppal': 'batting',
            'Rajiv Gandhi International Stadium, Uppal, Hyderabad': 'batting',  # ✅ added
            'Rajiv Gandhi Intl. Cricket Stadium': 'batting',
            'Dr DY Patil Sports Academy': 'batting',
            'Dr DY Patil Sports Academy, Mumbai': 'batting',
            'Sawai Mansingh Stadium': 'batting',
            'Sawai Mansingh Stadium, Jaipur': 'batting',
            'Maharashtra Cricket Association Stadium': 'batting',
            'Maharashtra Cricket Association Stadium, Pune': 'batting',
            'Brabourne Stadium': 'batting',
            'Brabourne Stadium, Mumbai': 'batting',
            'Subrata Roy Sahara Stadium': 'batting',
            'Sharjah Cricket Stadium': 'batting',
            'Dubai International Cricket Stadium': 'batting',
            'Sheikh Zayed Stadium': 'batting',
            'Zayed Cricket Stadium, Abu Dhabi': 'batting',  # ✅ added
            'OUTsurance Oval': 'batting',  # ✅ added

            # SPIN FRIENDLY
            'MA Chidambaram Stadium': 'spin',
            'MA Chidambaram Stadium, Chepauk': 'spin',
            'MA Chidambaram Stadium, Chepauk, Chennai': 'spin',  # ✅ added
            'M.A. Chidambaram Stadium': 'spin',
            'Chepauk Stadium': 'spin',

            # PACE FRIENDLY
            'Punjab Cricket Association IS Bindra Stadium': 'pace',
            'Punjab Cricket Association IS Bindra Stadium, Mohali': 'pace',  # ✅ added
            'Punjab Cricket Association IS Bindra Stadium, Mohali, Chandigarh': 'pace',  # ✅ added
            'Punjab Cricket Association Stadium': 'pace',
            'Punjab Cricket Association Stadium, Mohali': 'pace',  # ✅ added
            'PCA Stadium, Mohali': 'pace',
            'IS Bindra Stadium': 'pace',
            'HPCA Stadium': 'pace',
            'HPCA Stadium, Dharamsala': 'pace',
            'Himachal Pradesh Cricket Association Stadium': 'pace',
            'Himachal Pradesh Cricket Association Stadium, Dharamsala': 'pace',
            'Maharaja Yadavindra Singh International Cricket Stadium, Mullanpur': 'pace',
            'Maharaja Yadavindra Singh International Cricket Stadium, New Chandigarh': 'pace',

            # BALANCED
            'Eden Gardens': 'balanced',
            'Eden Gardens, Kolkata': 'balanced',
            'Arun Jaitley Stadium': 'balanced',
            'Arun Jaitley Stadium, Delhi': 'balanced',
            'Feroz Shah Kotla': 'balanced',
            'Narendra Modi Stadium': 'balanced',
            'Narendra Modi Stadium, Ahmedabad': 'balanced',
            'Sardar Patel Stadium': 'balanced',
            'Sardar Patel Stadium, Motera': 'balanced',  # ✅ added
            'BRSABV Ekana Cricket Stadium': 'balanced',
            'BRSABV Ekana Cricket Stadium, Lucknow': 'balanced',
            'Bharat Ratna Shri Atal Bihari Vajpayee Ekana Cricket Stadium, Lucknow': 'balanced',  # ✅ added
            'Bharat Ratna Shri Atal Bihari Vajpayee International Cricket Stadium': 'balanced',
            'Holkar Cricket Stadium': 'balanced',
            'Holkar Cricket Stadium, Indore': 'balanced',
            'Barabati Stadium': 'balanced',
            'Green Park': 'balanced',
            'Nehru Stadium': 'balanced',
            'Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium': 'balanced',
            'Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium, Visakhapatnam': 'balanced',
            'ACA-VDCA Stadium': 'balanced',
            'Vidarbha Cricket Association Stadium': 'balanced',
            'Vidarbha Cricket Association Stadium, Jamtha': 'balanced',
            'Shaheed Veer Narayan Singh International Stadium': 'balanced',
            'Barsapara Cricket Stadium': 'balanced',
            'Barsapara Cricket Stadium, Guwahati': 'balanced',
            'Saurashtra Cricket Association Stadium': 'balanced',
            'Saurashtra Cricket Association Stadium, Rajkot': 'balanced',
            'JSCA International Stadium Complex': 'balanced',
            'New Wanderers Stadium': 'balanced',
            'Kingsmead': 'balanced',
            'SuperSport Park': 'balanced',
            'Buffalo Park': 'balanced',
            'De Beers Diamond Oval': 'balanced',
            'St George\'s Park': 'balanced',
            'Newlands': 'balanced',
            'M Chinnaswamy Stadium, Bengaluru ': 'batting'
        }

        venue_name = venue
        match_pitch_type = pitch_type[venue_name]
        same_kind_of_venue = []
        for name, pitchtype in pitch_type.items():
            if pitchtype == match_pitch_type:
                same_kind_of_venue.append(name)

        batsmen = batsman_list
        bowlers = bowler_list2

        rows = []

        for j in range(len(batsmen)):
            row = {}
            for i in range(len(bowlers)):
                filtered = df[
                    (df['batter'] == batsmen[j]) &
                    (df['bowler'] == bowlers[i])
                    ]
                outs = df[
                    (df['batter'] == batsmen[j]) &
                    (df['bowler'] == bowlers[i]) &
                    (df['striker_out'] == True)
                    ]
                row[f'{bowlers[i]}_balls'] = filtered.shape[0]
                row[f'{bowlers[i]}_runs'] = filtered["runs_batter"].sum()
                row[f'{bowlers[i]}_outs'] = outs.shape[0]
                row[f'{bowlers[i]}_h2h'] = 1 if filtered.shape[0]> 0 else 0

            batsman_incondition = df[
                (df['batter'] == batsmen[j]) &
                (df['venue'] == venue_name)
                ]
            batsman_incondition_wicket = df[
                (df['batter'] == batsmen[j]) &
                (df['venue'] == venue_name) &
                (df['striker_out'] == True)
                ]
            row[f'runs_instadium'] = batsman_incondition['runs_batter'].sum()
            row[f'outs_instadium'] = batsman_incondition_wicket.shape[0]
            row[f'balls_instadium'] = batsman_incondition.shape[0]
            row[f'h2h_instadium'] = 1 if batsman_incondition.shape[0] > 0 else 0
            rows.append(row)
            batsman_inpitch = df[(df['batter'] == batsmen[j]) &
                                 (df['venue'].isin(same_kind_of_venue))]
            batsman_inpitch_out = df[(df['batter'] == batsmen[j]) &
                                     (df['venue'].isin(same_kind_of_venue)) &
                                     (df['striker_out'] == True)]
            row[f'runs_inpitch'] = batsman_inpitch['runs_batter'].sum()
            row[f'outs_inpitch'] = batsman_incondition_wicket.shape[0]
            row[f'balls_inpitch'] = batsman_incondition.shape[0]
            row[f'h2h_inpitch'] = 1 if batsman_incondition.shape[0] > 0 else 0


        result_df = pd.DataFrame(rows, index=batsmen)
        result_df.to_csv(location, mode='a')

        # ALL of this in ONE cell
        batsmen2 = batsman_list2
        bowlers2 = bowler_list

        rows = []

        for j in range(len(batsmen2)):
            row = {}
            for i in range(len(bowlers2)):
                filtered = df[
                    (df['batter'] == batsmen2[j]) &
                    (df['bowler'] == bowlers2[i])
                    ]
                outs = df[
                    (df['batter'] == batsmen2[j]) &
                    (df['bowler'] == bowlers2[i]) &
                    (df['striker_out'] == True)
                    ]
                row[f'{bowlers2[i]}_balls'] = filtered.shape[0]
                row[f'{bowlers2[i]}_runs'] = filtered["runs_batter"].sum()
                row[f'{bowlers2[i]}_outs'] = outs.shape[0]
                row[f'{bowlers2[i]}_h2h'] = 1 if filtered.shape[0] > 0 else 0

            batsman_incondition = df[
                (df['batter'] == batsmen2[j]) &
                (df['venue'] == venue)
                ]
            batsman_incondition_wicket = df[
                (df['batter'] == batsmen2[j]) &
                (df['venue'] == venue) &
                (df['striker_out'] == True)
                ]
            row[f'runs_invenue'] = batsman_incondition['runs_batter'].sum()
            row[f'outs_invenue'] = batsman_incondition_wicket.shape[0]
            row[f'balls_invenue'] = batsman_incondition.shape[0]
            row[f'h2h_invenue'] = 1 if batsman_incondition.shape[0] > 0 else 0

            batsman_inpitch = df[(df['batter'] == batsmen2[j]) &
                                 (df['venue'].isin(same_kind_of_venue))]
            batsman_inpitch_out = df[(df['batter'] == batsmen2[j]) &
                                     (df['venue'].isin(same_kind_of_venue)) &
                                     (df['striker_out'] == True)]
            row[f'runs_inpitch'] = batsman_inpitch['runs_batter'].sum()
            row[f'outs_inpitch'] = batsman_incondition_wicket.shape[0]
            row[f'balls_inpitch'] = batsman_incondition.shape[0]
            row[f'h2h_inpitch'] = 1 if batsman_incondition.shape[0] > 0 else 0
            rows.append(row)

        result_df = pd.DataFrame(rows, index=batsmen2)
        result_df.to_csv(location, mode='a')