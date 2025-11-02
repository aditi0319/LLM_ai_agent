import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib
import os

# Load CSV
data = pd.read_csv("app/data/processed/appointy_dataset.csv", encoding="latin1")



# Features & labels
X = data["query"]
y = data["category"]

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# TF-IDF Vectorizer
vectorizer = TfidfVectorizer(stop_words="english")
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Model
model = LogisticRegression(max_iter=1000)
model.fit(X_train_vec, y_train)

# Save
os.makedirs("app/models", exist_ok=True)
joblib.dump(model, "app/models/classifier.pkl")
joblib.dump(vectorizer, "app/models/vectorizer.pkl")

print("✅ Model training complete and files saved.")
