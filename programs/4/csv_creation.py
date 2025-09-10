import pandas as pd
import numpy as np

# Create some sample data
np.random.seed(42)  # for reproducibility
feature1 = np.random.randint(0, 10, 20)   # 20 random integers between 0–9
feature2 = np.random.randint(0, 10, 20)   # 20 random integers between 0–9

# Simple label rule (you can change as needed)
label = (feature1 + feature2 > 10).astype(int)

# Build dataframe
data = pd.DataFrame({
    "Feature1": feature1,
    "Feature2": feature2,
    "Label": label
})

# Save to CSV
data.to_csv("ann_data.csv", index=False)

print("✅ ann_data.csv file created successfully!")
print(data)
