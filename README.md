# IPL Match Win Predictor 🏏

Predicts IPL match winner by analyzing player-level 
several factors such as head-to-head matchup statistics, bowler stats in venue, Nrr, last 5 matches result were used 
rather than team history —
because mega auctions change 70-80% of team rosters, 
making team vs team history obsolete.

## The Core Insight
Traditional IPL predictors use team win history.
But after every mega auction, teams change completely.
This model uses **individual player matchup stats** instead.

## How It Works
- Extracts ball-by-ball H2H stats from 17 years of IPL data
- 1007 matches, 260,000+ deliveries analyzed
- Features: batsman vs bowler H2H, venue stats, 
  pitch type (batting/spin/pace/balanced), team form
- Automated data extraction pipeline using OOP (3 classes)
- Pipeline: StandardScaler → PCA → Models

## Models & Accuracy
| Model | Accuracy |
|---|---|
| Random Forest | 57% |
| Logistic Regression | 54.22% |
| XGBoost | 51% |

## Note
The extracted match data files (3000+ CSVs) are not 
included due to size. Run main.py to regenerate them
from IPL.csv (available on Kaggle).

## Tech Stack
Python, Pandas, NumPy, Scikit-learn

## Dataset
IPL ball-by-ball data 2008-2026 (Kaggle)
