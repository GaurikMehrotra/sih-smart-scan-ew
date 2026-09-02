import pandas as pd
from xgboost import XGBClassifier

# Load data
df = pd.read_csv("ml/features.csv")

X = df[["time", "band", "prev_active"]]
y = df["active"]

# Train model
model = XGBClassifier()
model.fit(X, y)

# Example scan candidates
candidates = pd.DataFrame([
    {"time": 101, "band": 1, "prev_active": 1},
    {"time": 101, "band": 2, "prev_active": 0},
    {"time": 101, "band": 3, "prev_active": 1},
])

# Predict probabilities
probs = model.predict_proba(candidates)[:, 1]

candidates["probability"] = probs

# Sort highest first
candidates = candidates.sort_values(
    by="probability",
    ascending=False
)

print(candidates)