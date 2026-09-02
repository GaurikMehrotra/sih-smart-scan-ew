import pandas as pd

df = pd.read_csv("simulator/ew_dataset.csv")

df["prev_active"] = df["active"].shift(1)

df["prev_active"] = df["prev_active"].fillna(0)

print(df.head(10))

df.to_csv("ml/features.csv", index=False)

print("Feature dataset created!")