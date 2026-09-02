import pandas as pd

data = []

hopper_bands = [3, 5, 8]

for time_step in range(1, 101):

    # E1 Periodic Radar
    active = 1 if time_step % 5 == 0 else 0

    data.append({
        "time": time_step,
        "emitter_id": "E1",
        "emitter_type": "periodic",
        "band": 1,
        "active": active
    })

    # E2 Burst Communication
    active = 1 if (20 <= time_step <= 30 or 60 <= time_step <= 70) else 0

    data.append({
        "time": time_step,
        "emitter_id": "E2",
        "emitter_type": "burst",
        "band": 2,
        "active": active
    })

    # E3 Frequency Hopper
    band = hopper_bands[time_step % 3]

    data.append({
        "time": time_step,
        "emitter_id": "E3",
        "emitter_type": "hopper",
        "band": band,
        "active": 1
    })

df = pd.DataFrame(data)

df.to_csv("simulator/ew_dataset.csv", index=False)

print(df.head(20))
print()
print("Rows:", len(df))