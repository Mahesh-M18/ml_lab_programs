import numpy as np
import pandas as pd

# Generate sample data (linear with some noise)
np.random.seed(42)
X = np.linspace(0.1, 1.0, 30)                # 30 points between 0.1 and 1.0
Y = 2 * X + 0.3 + np.random.normal(0, 0.1, 30)  # linear relation + noise

# Create DataFrame
df = pd.DataFrame({"colA": X, "colB": Y})

# Save to CSV
df.to_csv("lwr.csv", index=False)

print("✅ lwr.csv file generated with 30 rows.")
print(df.head())   # Show first few rows
