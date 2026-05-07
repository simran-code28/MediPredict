import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.predict import predict_all

# sample inputs
diabetes_sample = [6,148,72,35,0,33.6,0.627,50]
heart_sample = [63,1,3,145,233,1,0,150,0,2.3,0,0,1]

result = predict_all(diabetes_sample, heart_sample)

print(result)