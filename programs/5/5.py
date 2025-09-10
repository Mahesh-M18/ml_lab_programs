import pandas as pd
from sklearn.datasets import fetch_20newsgroups
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, precision_score, recall_score, classification_report

# -----------------------------
# Load dataset (20 Newsgroups)
# -----------------------------
categories = ['alt.atheism', 'comp.graphics', 'sci.space', 'rec.sport.baseball']  # pick a few categories
newsgroups = fetch_20newsgroups(subset='all', categories=categories, remove=('headers', 'footers', 'quotes'))

# Convert into DataFrame for convenience
data = pd.DataFrame({
    "text": newsgroups.data,
    "label": [newsgroups.target_names[i] for i in newsgroups.target]
})

# -----------------------------
# Features and Labels
# -----------------------------
X = data['text']
y = data['label']

# Convert text to numerical vectors (Bag of Words)
vectorizer = CountVectorizer(stop_words='english', max_features=5000)
X_vectors = vectorizer.fit_transform(X)

# Split into train/test sets
X_train, X_test, y_train, y_test = train_test_split(X_vectors, y, test_size=0.3, random_state=42)

# -----------------------------
# Train Naive Bayes Model
# -----------------------------
model = MultinomialNB()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# -----------------------------
# Evaluation
# -----------------------------
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average='weighted')
recall = recall_score(y_test, y_pred, average='weighted')

print("✅ Accuracy:", accuracy)
print("✅ Precision:", precision)
print("✅ Recall:", recall)
print("\nClassification Report:\n", classification_report(y_test, y_pred))
