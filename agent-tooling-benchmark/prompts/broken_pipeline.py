# broken_pipeline.py — 4 bugs from real geospatial ML project
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score, f1_score, classification_report

# Load H3 grid data
df = pd.read_parquet('london_h3_grid.parquet')

# Create binary target for cafe presence
df['target'] = (df['n_cafe'] > 0).astype(int)

# Bug 1: Target leakage — using n_cafe-derived features AND n_cafe itself
#         n_cafe is included in features (it IS the target source)
feature_cols = ['population', 'age_16_to_34_perc', 'level4_perc',
                'property_crime_log1p', 'closeness_centrality',
                'n_cafe', 'n_restaurant', 'n_pub']  # n_cafe = leakage!

X = df[feature_cols].fillna(0)
y = df['target']

# Bug 2: No filtering of zero-population hexagons (parks, cemeteries, rivers)
#         These are non-viable locations that add noise
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Bug 3: Evaluating AUC on training data, reporting as test performance
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
train_proba = model.predict_proba(X_train)[:, 1]
auc = roc_auc_score(y_train, train_proba)  # Should be y_test!
print(f"Test AUC: {auc:.4f}")

# Bug 4: Using default 0.5 threshold on imbalanced spatial data
#         (cafe hexagons are minority class ~25-30%)
test_preds = model.predict(X_test)  # default threshold = 0.5
f1 = f1_score(y_test, test_preds)
print(f"Test F1: {f1:.4f}")
print(classification_report(y_test, test_preds))
