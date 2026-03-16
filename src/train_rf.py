import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from features import extract_features
import joblib

df_train = pd.read_csv("data/processed/train.csv")
df_test  = pd.read_csv("data/processed/test.csv")

X_train = extract_features(df_train["payload"])
X_test  = extract_features(df_test["payload"])
y_train, y_test = df_train["label"], df_test["label"]

rf = RandomForestClassifier(n_estimators=200, random_state=42, n_jobs=-1)
rf.fit(X_train, y_train)
preds = rf.predict(X_test)
print(classification_report(y_test, preds))

joblib.dump(rf, "models/rf_model.pkl")
print("✅ Random Forest saved to models/rf_model.pkl")
