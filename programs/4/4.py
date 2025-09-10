import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report

# Load dataset
data = pd.read_csv("ann_data.csv")
X = data[["Feature1", "Feature2"]]
y = data["Label"]

# Split into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=0)

# Scale features (important for neural networks)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Train model
model = MLPClassifier(hidden_layer_sizes=(4,), max_iter=1000, random_state=42)
model.fit(X_train, y_train)

# Predictions
pred = model.predict(X_test)

# Results
print("Predictions:", pred)
print("Actual     :", y_test.values)
print("Accuracy   :", accuracy_score(y_test, pred))
print("\nClassification Report:\n", classification_report(y_test, pred))
