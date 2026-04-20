import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score

from app.utils.feature_extractor import extract_features


# -----------------------------
# CONFIG
# -----------------------------
DATA_PATH = "data/processed/final_dataset.csv"
MODEL_PATH = "models/url_model.pkl"


# -----------------------------
# LOAD DATA
# -----------------------------
df = pd.read_csv(DATA_PATH)

if "url" not in df.columns:
    raise ValueError("Dataset must contain 'url' column")


# -----------------------------
# FEATURE ENGINEERING
# -----------------------------
def build_feature_matrix(df: pd.DataFrame):
    features = df["url"].apply(extract_features)
    feature_df = pd.DataFrame(features.tolist(), columns=[
        "url_length",
        "dots",
        "digits",
        "special_chars",
        "subdomains",
        "entropy",
        "suspicious_keywords"
    ])
    return feature_df


X = build_feature_matrix(df)

# Ensure label column exists
if "label" not in df.columns:
    raise ValueError("Dataset must contain 'label' column")

y = df["label"]


# -----------------------------
# SPLIT DATA
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


# -----------------------------
# MODEL
# -----------------------------
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)


# -----------------------------
# EVALUATION
# -----------------------------
y_pred = model.predict(X_test)

print("\n📊 MODEL PERFORMANCE")
print("----------------------------")
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))


# -----------------------------
# SAVE MODEL
# -----------------------------
joblib.dump(model, MODEL_PATH)

print(f"\n✅ Model saved to {MODEL_PATH}")