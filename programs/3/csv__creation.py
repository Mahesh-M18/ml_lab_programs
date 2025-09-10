import pandas as pd

# Data for playtennis.csv
data = {
    "Outlook":    [0, 0, 1, 2, 2, 2, 1, 0, 0, 2, 0, 1, 1, 2, 0, 1],
    "Temperature":[0, 0, 0, 1, 2, 2, 2, 1, 2, 1, 1, 1, 0, 1, 1, 1],
    "Humidity":   [0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1],
    "Wind":       [0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1],
    "Class":      [0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1]
}

# Create dataframe
df = pd.DataFrame(data)

# Save as CSV
df.to_csv("playtennis.csv", index=False)

print("✅ playtennis.csv file created successfully!")
