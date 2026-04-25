import joblib

# Modell laden
model = joblib.load("spam_detection_model.joblib")

# Beispiel: Vorhersage
sample_input = ["This is a test SMS"]
prediction = model.predict(sample_input)

print("Prediction:", prediction)