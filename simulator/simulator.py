import pandas as pd

data = []

for time_step in range(1, 101):

    for band in range(1, 11):

        active = 0

        # Band 1 -> Periodic Emitter
        if band == 1:
            if time_step % 5 == 0:
                active = 1

        # Band 2 -> Burst Emitter
        elif band == 2:
            if 20 <= time_step <= 30:
                active = 1
            elif 60 <= time_step <= 70:
                active = 1

        # Band 3 -> Frequency Hopper
        elif band == 3:
            if time_step % 4 == 0:
                active = 1

        data.append({
            "time": time_step,
            "band": band,
            "active": active
        })

df = pd.DataFrame(data)

df.to_csv("simulator/dataset.csv", index=False)

print("Dataset generated successfully!")
print(df.head())