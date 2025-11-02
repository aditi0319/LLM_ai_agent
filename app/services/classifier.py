import joblib
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pandas as pd

class TicketClassifier:
    def __init__(self):
        model_path = "app/models/classifier.pkl"
        vectorizer_path = "app/models/vectorizer.pkl"

        if os.path.exists(model_path) and os.path.exists(vectorizer_path):
            self.model = joblib.load(model_path)
            self.vectorizer = joblib.load(vectorizer_path)
        else:
            raise RuntimeError("Model or vectorizer not found. Train the model first.")

    def predict(self, text: str):
        X = self.vectorizer.transform([text])
        pred = self.model.predict(X)[0]
        return pred
