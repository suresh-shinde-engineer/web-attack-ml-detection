import joblib, torch, time, argparse
from transformers import BertTokenizer, BertForSequenceClassification
from features import extract_features
import pandas as pd

LABELS = {0: "BENIGN", 1: "SQLI", 2: "XSS"}
rf  = joblib.load("models/rf_model.pkl")
tok = BertTokenizer.from_pretrained("models/bert_finetuned")
bert = BertForSequenceClassification.from_pretrained("models/bert_finetuned")
bert.eval()

def predict(payload: str):
    start = time.time()
    feat = extract_features(pd.Series([payload]))
    rf_prob  = rf.predict_proba(feat)[0]
    enc = tok(payload, return_tensors="pt", truncation=True, max_length=128, padding="max_length")
    with torch.no_grad():
        bert_prob = torch.softmax(bert(**enc).logits, dim=1).numpy()[0]
    final = 0.4 * rf_prob + 0.6 * bert_prob
    idx = final.argmax()
    ms  = round((time.time() - start) * 1000, 1)
    return {"label": LABELS[idx], "confidence": round(float(final[idx])*100,1),
            "rf_score": round(float(rf_prob[idx]),3),
            "bert_score": round(float(bert_prob[idx]),3), "ms": ms}

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--payload", type=str, required=True)
    r = predict(ap.parse_args().payload)
    icon = "🚨 ATTACK DETECTED" if r["label"] != "BENIGN" else "✅ BENIGN"
    print(f"\n{'━'*40}\n  {icon}\n  Type      : {r['label']}\n"
          f"  Confidence: {r['confidence']}%\n  RF Score  : {r['rf_score']}\n"
          f"  BERT Score: {r['bert_score']}\n  Inference : {r['ms']}ms\n{'━'*40}\n")
```

---

### 📄 `.gitignore`
```
venv/
__pycache__/
*.pyc
data/raw/
models/bert_finetuned/
models/*.pkl
results/logs/
.env
*.ipynb_checkpoints
```

---

## 🚀 How to Set Up Your GitHub Repo
```
1. Go to github.com → New Repository
2. Name it: web-attack-ml-detection
3. Set to Public (for ArXiv credibility)
4. Create the folder structure above
5. Paste each file content
6. Commit with message: "Initial research release - Suresh Shinde, Techno Experts"
