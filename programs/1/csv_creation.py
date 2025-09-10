import pandas as pd

# Define the training examples
data = [
    ["Sunny", "Warm", "Normal", "Strong", "Warm", "Same", "Yes"],
    ["Sunny", "Warm", "High", "Strong", "Warm", "Same", "Yes"],
    ["Rainy", "Cold", "High", "Strong", "Warm", "Change", "No"],
    ["Sunny", "Warm", "High", "Strong", "Cool", "Change", "Yes"]
]

# Define the column headers
headers = ['Sky', 'Temp', 'Humidity', 'Wind', 'Water', 'Forecast', 'EnjoySport']

# Create DataFrame and write to CSV
df = pd.DataFrame(data, columns=headers)
df.to_csv("Weather.csv", index=False)