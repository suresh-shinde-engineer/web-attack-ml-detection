import pandas as pd
from imblearn.over_sampling import SMOTE
from sklearn.model_selection import train_test_split
import joblib, os

def load_and_merge():
    df1 = pd.read_csv("data/raw/csic_2010.csv")
    df2 = pd.read_csv("data/raw/httpd_logs.csv")
    df3 = pd.read_csv("data/raw/webgoat_logs.csv")
    df = pd.concat([df1, df2, df3], ignore_index=True)
    df.drop_duplicates(inplace=True)
    df.dropna(subset=["payload", "label"], inplace=True)
    return df

def balance(X, y):
    sm = SMOTE(random_state=42)
    return sm.fit_resample(X, y)

if __name__ == "__main__":
    df = load_and_merge()
    os.makedirs("data/processed", exist_ok=True)
    train, test = train_test_split(df, test_size=0.2, stratify=df["label"])
    train.to_csv("data/processed/train.csv", index=False)
    test.to_csv("data/processed/test.csv", index=False)
    print(f"✅ Preprocessing done. Train: {len(train)} | Test: {len(test)}")
