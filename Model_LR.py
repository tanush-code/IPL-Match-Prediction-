import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold, cross_val_score

df = pd.read_csv('IPL.csv')

all_matches = []
y = []


for i in range(1008):
    bat = pd.read_csv(f'BatsmanData/Batsman_data{i+1}.csv',header = None)
    bowl = pd.read_excel(f'BowlerData/Bowler_data{i+1}.xlsx', header = None)
    match = pd.read_excel(f'MatchData/Match_data{i+1}.xlsx', header= None)

    # Keep only numeric columns
    bat = bat.select_dtypes(include=[np.number])
    bowl = bowl.select_dtypes(include=[np.number])
    match = match.select_dtypes(include=[np.number])

    # Fill remaining NaN with 0
    bat = bat.fillna(0)
    bowl = bowl.fillna(0)
    match = match.fillna(0)

    bat_vector = bat.values.flatten()
    bowl_vector = bowl.values.flatten()
    match_vector = match.values.flatten()
    Final_vector = np.concatenate([bat_vector, bowl_vector, match_vector])
    all_matches.append(Final_vector)
    Y.append(1 if df["batting_team"] == df["match_won_by"] else 0)
X = np.array(all_matches)

all_matches = df.drop_duplicates('match_id')[
    ['match_id', 'batting_team', 'bowling_team',
     'year', 'month', 'day', 'match_won_by']
].sort_values(['year', 'month', 'day'])

for _, row in all_matches.iterrows():

    if row['match_won_by'] == row['batting_team']:
        y.append(1)
    else:
        y.append(0)
pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('pca', PCA(n_components=20)),
    ('lda', LinearDiscriminantAnalysis()),
    ('model', LogisticRegression())
])

KFold = KFold(n_splits=10, shuffle=True, random_state=42)

scores = cross_val_score(pipe, X, Y, cv=KFold, scoring='accuracy')

print(scores)
print(scores.mean())
