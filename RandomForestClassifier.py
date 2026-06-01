import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier


df = pd.read_csv('IPL.csv', low_memory=False)

# Get match IDs in chronological order
match_ids = df.drop_duplicates('match_id').sort_values('date')['match_id'].values
total_matches = len(match_ids)
print(f"Total matches: {total_matches}")

all_matches = []
Y = []
failed = []


for i in range(1007):
    # Load files
    bat = pd.read_csv(f'FinalFiles/Batsman_data{i + 1}.csv', engine='python', on_bad_lines='skip', encoding='latin1')
    bowl = pd.read_csv(f'FinalFiles/Bowler_data{i + 1}.csv', engine='python', on_bad_lines='skip', encoding='latin1')
    match = pd.read_csv(f'FinalFiles/Match_data{i + 1}.csv', engine='python', on_bad_lines='skip', encoding='latin1')

    # Keep numeric only
    bat = bat.select_dtypes(include=[np.number]).fillna(0)
    bowl = bowl.select_dtypes(include=[np.number]).fillna(0)
    match = match.select_dtypes(include=[np.number]).fillna(0)

    # Flatten
    bat_vector = bat.values.flatten()
    bowl_vector = bowl.values.flatten()
    match_vector = match.values.flatten()
    final_vector = np.concatenate([bat_vector, bowl_vector, match_vector])
    all_matches.append(final_vector)

    # Build Y - correct way
    match_data = df[df['match_id'] == match_ids[i]]
    batting_first = match_data[
        match_data['innings'] == 1
        ]['batting_team'].iloc[0]
    winner = match_data['match_won_by'].iloc[0]
    Y.append(1 if batting_first == winner else 0)
# except Exception as e:
#     print(f"Match {i+1} failed: {e}")
#     failed.append(i+1)
#     continue

print(f"Successfully loaded: {len(all_matches)} matches")
print(f"Failed: {len(failed)} matches")

# Pad all vectors to same size
max_size = max(len(v) for v in all_matches)
print(f"Max vector size: {max_size}")

all_matches_padded = []
for v in all_matches:
    padded = np.pad(v, (0, max_size - len(v)))
    all_matches_padded.append(padded)

X = np.array(all_matches_padded)
Y = np.array(Y)
# print(f"X shape: {X.shape}")
# print(f"Y shape: {Y.shape}")

# Train test split
X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, random_state=42
)
# Pipeline
pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('pca', PCA(n_components=0.95)),
    ('RandomForestClassifier', RandomForestClassifier(max_depth=2, random_state=42)),
])
pipe.fit(X_train, Y_train)

accuracy = pipe.score(X_test, Y_test)
print("Accuracy of XGBoost: {:.4f}", accuracy*100)