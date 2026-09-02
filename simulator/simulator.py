import pandas as pd
import random

data = []

for time_step in range(1, 101):
    for band in range(1, 11):
        active = random.randint(0, 1)

        data.append({
            "time": time_step,
            "band": band,
            "active": active
        })

df = pd.DataFrame(data)

df.to_csv("simulator/dataset.csv", index=False)

print("Dataset created successfully!")
print(df.head())