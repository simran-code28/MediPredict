import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load dataset
df = pd.read_csv("data/pcos.csv", encoding='ISO-8859-1', on_bad_lines='skip')
# 🔥 Clean column names (VERY IMPORTANT)
df.columns = df.columns.str.strip()

# 🔥 Remove unwanted columns if present
if 'Sl. No' in df.columns:
    df = df.drop('Sl. No', axis=1)

# 🔥 Convert Yes/No to 1/0 if needed
df = df.replace({'Y': 1, 'N': 0})

# 🔥 Handle missing values
df = df.fillna(df.mean(numeric_only=True))

# 🔥 Target
y = df["PCOS"]
X = df.drop("PCOS", axis=1)

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save model
pickle.dump(model, open("models/pcos_model.pkl", "wb"))

print("PCOS Model Trained & Saved ✅")
print("Columns:", df.columns)