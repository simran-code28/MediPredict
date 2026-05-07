import pickle
import numpy as np
import os

# Base directory fix
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Load models
diabetes_model = pickle.load(open(os.path.join(BASE_DIR, "models/diabetes_model.pkl"), "rb"))
heart_model = pickle.load(open(os.path.join(BASE_DIR, "models/heart_model.pkl"), "rb"))
pcos_model = pickle.load(open(os.path.join(BASE_DIR, "models/pcos_model.pkl"), "rb"))

# ---------------- DIABETES ----------------
def predict_diabetes(data):
    data = np.array(data).reshape(1, -1)
    result = diabetes_model.predict(data)[0]

    if result == 1:
        return {
            "result": "Diabetes",
            "risk": "High",
            "advice": "Avoid sugar, eat low-carb diet, exercise daily, and consult a doctor."
        }
    else:
        return {
            "result": "No Diabetes",
            "risk": "Low",
            "advice": "Maintain a healthy diet and regular exercise."
        }

# ---------------- HEART ----------------
def predict_heart(data):
    data = np.array(data).reshape(1, -1)
    result = heart_model.predict(data)[0]

    if result == 1:
        return {
            "result": "Heart Disease",
            "risk": "High",
            "advice": "Avoid oily food, reduce stress, do cardio exercise, and consult a cardiologist."
        }
    else:
        return {
            "result": "No Heart Disease",
            "risk": "Low",
            "advice": "Heart condition looks stable. Maintain exercise and a balanced diet."
        }

# ---------------- PCOS ----------------
def predict_pcos(data):
    data = np.array(data).reshape(1, -1)
    result = pcos_model.predict(data)[0]

    if result == 1:
        return {
            "result": "PCOS",
            "risk": "High",
            "advice": "Follow low sugar diet, manage weight, exercise regularly, and consult a gynecologist."
        }
    else:
        return {
            "result": "No PCOS",
            "risk": "Low",
            "advice": "Normal condition. Maintain healthy lifestyle."
        }

# ---------------- FINAL COMBINED ----------------
def predict_all(diabetes_data, heart_data, pcos_data):
    return {
        "diabetes": predict_diabetes(diabetes_data),
        "heart": predict_heart(heart_data),
        "pcos": predict_pcos(pcos_data)
    }