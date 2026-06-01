import pandas as pd


class MatchExtraction:

    def data_extraction(self, venue,last5matches,last5matches2,location):

        venue_batting_first_win_pct = {

            # BATTING FRIENDLY
            'M Chinnaswamy Stadium': 0.44,
            'Wankhede Stadium': 0.44,
            'Rajiv Gandhi International Stadium': 0.46,
            'Dr DY Patil Sports Academy': 0.46,
            'Sawai Mansingh Stadium': 0.40,
            'Maharashtra Cricket Association Stadium': 0.57,
            'Brabourne Stadium': 0.54,
            'Subrata Roy Sahara Stadium': 0.62,
            'Sharjah Cricket Stadium': 0.36,
            'Dubai International Cricket Stadium': 0.46,
            'Sheikh Zayed Stadium': 0.38,
            'Zayed Cricket Stadium, Abu Dhabi': 0.38,
            'OUTsurance Oval': 0.50,

            # SPIN FRIENDLY
            'MA Chidambaram Stadium': 0.51,

            # PACE FRIENDLY
            'Punjab Cricket Association Stadium, Mohali': 0.46,
            'Himachal Pradesh Cricket Association Stadium, Dharamsala': 0.62,
            'Maharaja Yadavindra Singh International Cricket Stadium, New Chandigarh': 0.42,

            # BALANCED
            'Eden Gardens': 0.45,
            'Arun Jaitley Stadium': 0.49,
            'Narendra Modi Stadium': 0.50,
            'BRSABV Ekana Cricket Stadium': 0.38,
            'Holkar Cricket Stadium': 0.11,
            'Barabati Stadium': 0.57,
            'Vidarbha Cricket Association Stadium': 0.67,
            'Nehru Stadium': 0.60,
            'ACA-VDCA Stadium': 0.48,
            'Shaheed Veer Narayan Singh International Stadium': 0.33,
            'JSCA International Stadium Complex': 0.29,
            'Barsapara Cricket Stadium': 0.50,
            'Saurashtra Cricket Association Stadium': 0.30,
            'Green Park': 0.00,

            # SOUTH AFRICA VENUES
            'New Wanderers Stadium': 0.38,
            'Kingsmead': 0.53,
            'SuperSport Park': 0.33,
            'Buffalo Park': 0.67,
            'De Beers Diamond Oval': 0.33,
            "St George's Park": 0.43,
            'Newlands': 0.57,
        }
        Winning_pct =venue_batting_first_win_pct.get(venue, 0)
        Match_data = {
            "Win Predictions": venue_batting_first_win_pct.get(venue, 0.5),
            "Result Of last Five Matches team1": last5matches,
            "result Of Last Five Matches team2": last5matches2,
        }

        result_df = pd.DataFrame([Match_data])

        result_df.to_csv(
            location,
            mode="a",
            index=False,
            header=False
        )