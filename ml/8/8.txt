# 1. Import required libraries
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import numpy as np

# 2. Load Iris dataset
iris = load_iris()
X = iris.data        # Features
y = iris.target      # Labels
print("Feature Names:", iris.feature_names)
print("Target Names:", iris.target_names)

# 3. Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# 4. Create KNN classifier
knn = KNeighborsClassifier(n_neighbors=3)  # You can change k
knn.fit(X_train, y_train)

# 5. Predict on test data
predictions = knn.predict(X_test)

# 6. Calculate accuracy
accuracy = knn.score(X_test, y_test)
print("\nAccuracy:", accuracy*100)

# 7. Print predictions and actual labels
print("\nPredicted Labels: ", predictions)
print("Actual Labels:    ", y_test)

# 8. Identify correct and wrong predictions
correct = np.sum(predictions == y_test)
wrong = np.sum(predictions != y_test)
print("\nNumber of Correct Predictions:", correct)
print("Number of Wrong Predictions:  ", wrong)

