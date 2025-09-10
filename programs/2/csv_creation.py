import pandas as pd

# Properly structured data
data = [
    ["Sunny", "Warm", "Normal", "Strong", "Warm", "Same", "Yes"],
    ["Sunny", "Warm", "High", "Strong", "Warm", "Same", "Yes"],
    ["Rainy", "Cold", "High", "Strong", "Warm", "Change", "No"],
    ["Sunny", "Warm", "High", "Strong", "Cool", "Change", "Yes"]
]

# Corresponding headers
headers = ["Sky", "Air", "Humidity", "Wind", "Water", "Forecast", "EnjoySport"]

# Create DataFrame and save to CSV
df = pd.DataFrame(data, columns=headers)
df.to_csv("Weather.csv", index=False)