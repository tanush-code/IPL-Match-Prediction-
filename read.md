# IPL Match Winner Prediction using Machine Learning

## Overview

This project predicts the winner of an Indian Premier League (IPL) match using historical match data and machine learning techniques.

The goal of the project is to analyze various match-related factors such as venue performance, recent team form, net run rate, and historical trends to classify whether a team is likely to win or lose a match.

This project was created as part of my machine learning learning journey and demonstrates the complete workflow of a classification problem, including data collection, feature engineering, preprocessing, dimensionality reduction, model training, and evaluation.

---

## Dataset

The dataset contains historical IPL match information collected from publicly available cricket records.

Features used include:

* Venue
* Venue batting-first win percentage
* Recent match performance
* Net Run Rate (NRR)
* Match results
* Team statistics
* Historical trends

The target variable is:

* Match Winner (Classification)

---

## Project Workflow

### 1. Data Collection

Historical IPL match data was gathered and organized into a structured CSV format.

### 2. Data Cleaning

* Missing values handled
* Duplicate entries removed
* Data consistency checks performed

### 3. Feature Engineering

Several cricket-specific features were created, including:

* Venue advantage metrics
* Batting-first win percentages
* Recent form indicators
* Net Run Rate statistics

### 4. Data Preprocessing

* Numerical features standardized
* Features prepared for dimensionality reduction

### 5. Dimensionality Reduction

Principal Component Analysis (PCA) was used to reduce feature dimensionality while retaining the majority of the variance present in the dataset.

### 6. Classification

Linear Discriminant Analysis (LDA) was applied for classification after PCA transformation.

### 7. Model Evaluation

The model was evaluated using:

* Train-Test Split
* K-Fold Cross Validation
* Accuracy Score
* Classification Metrics

---

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* PCA
* Linear Discriminant Analysis (LDA)

---

## Project Structure

```text
IPL-Match-Prediction/
│
├── IPL.csv
├── main.py
├── README.md
├── requirements.txt
│
└── results/
    ├── confusion_matrix.png
    └── evaluation_report.txt
```

---

## Results

The model successfully learns patterns from historical IPL matches and demonstrates how machine learning can be applied to sports analytics.

Performance was evaluated using cross-validation to ensure the model generalizes beyond the training data.

---

## Key Learnings

Through this project I learned:

* Data preprocessing techniques
* Feature engineering for sports datasets
* Principal Component Analysis (PCA)
* Linear Discriminant Analysis (LDA)
* Model evaluation and validation
* Building end-to-end machine learning pipelines

---

## Future Improvements

Potential improvements include:

* Adding player-level statistics
* Incorporating batsman vs bowler matchups
* Including toss impact analysis
* Using ensemble models such as Random Forest and XGBoost
* Building a web application for live match predictions

---

## Author

**Tanush Rathore**

First-Year B.Tech Student | Machine Learning & AI Enthusiast

Currently exploring Machine Learning, Deep Learning, PyTorch, and Sports Analytics through practical projects.
