import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import pandas as pd

# -----------------------------
# Option 1: Generate random data
# -----------------------------
np.random.seed(110)  # for reproducibility

# Parameters for two clusters
red_mean, red_std = 3, 0.8
blue_mean, blue_std = 7, 1

# Generate random data
red = np.random.normal(red_mean, red_std, 40)
blue = np.random.normal(blue_mean, blue_std, 40)
data_points = np.sort(np.concatenate((red, blue)))
y_dummy = np.zeros(len(data_points))  # y-values for plotting

# -----------------------------
# Option 2: Load data from CSV
# Uncomment to use CSV
# -----------------------------
# df = pd.read_csv('data.csv')  # assuming a single column of values
# data_points = df.iloc[:,0].values
# y_dummy = np.zeros(len(data_points))

# -----------------------------
# K-Means clustering
# -----------------------------
kmeans = KMeans(n_clusters=2, random_state=0)
kmeans_output = kmeans.fit(data_points.reshape(-1, 1))

# -----------------------------
# Elbow Method to find optimal K
# -----------------------------
Nc = range(1, 6)
kmeans_models = [KMeans(n_clusters=i, random_state=0).fit(data_points.reshape(-1,1)) for i in Nc]
score = [model.inertia_ for model in kmeans_models]

plt.plot(Nc, score)
plt.xlabel('Number of Clusters (K)')
plt.ylabel('Score')
plt.title('Elbow Method')
plt.show()

# -----------------------------
# Plot clustered data
# -----------------------------
plt.scatter(data_points, y_dummy, c=kmeans_output.labels_, cmap='viridis')
plt.xlabel('Data Points')
plt.ylabel('Dummy Y')
plt.title('K-Means Clustering (2 Clusters)')
plt.show()
