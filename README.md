# 🛡️ Web Attack ML Detection
### Machine Learning-Based Real-Time Detection of SQL Injection and XSS Attacks

> **Author:** Suresh Shinde — [Techno Experts](https://www.technoexperts.co/)
> **Paper:** Submitted to arXiv.org — cs.CR (Cryptography and Security), March 2026
> **License:** CC BY 4.0

---

## 📌 Overview

This repository contains the full implementation of the research paper:

> *"Machine Learning-Based Real-Time Detection of SQL Injection and XSS Attacks in Web Applications"*
> — Suresh Shinde, Techno Experts (2026)

The project proposes a **Hybrid Random Forest + Fine-Tuned BERT pipeline** for real-time web attack detection, achieving **98.7% accuracy** at **8.7ms inference time** — suitable for inline WAF deployment.

---

## 🗂️ Repository Structure

```
web-attack-ml-detection/
│
├── data/
│   ├── raw/                    # Raw downloaded datasets (not committed)
│   ├── processed/              # Cleaned, merged, balanced datasets
│   └── README_data.md          # Instructions to download datasets
│
├── notebooks/
│   ├── 01_EDA.ipynb            # Exploratory Data Analysis
│   ├── 02_Feature_Engineering.ipynb
│   ├── 03_Model_Training.ipynb
│   └── 04_Evaluation.ipynb
│
├── src/
│   ├── preprocess.py           # Data cleaning & SMOTE balancing
│   ├── features.py             # Feature extraction module
│   ├── train_rf.py             # Random Forest training
│   ├── train_bert.py           # BERT fine-tuning
│   ├── ensemble.py             # Hybrid ensemble prediction
│   ├── evaluate.py             # Metrics & visualizations
│   └── inference.py            # Real-time inference API
│
├── models/
│   ├── rf_model.pkl            # Saved Random Forest model
│   └── bert_finetuned/         # Saved BERT weights (HuggingFace format)
│
├── results/
│   ├── metrics_comparison.csv  # All model results
│   └── plots/                  # ROC curves, confusion matrices
│
├── requirements.txt
├── README.md
└── LICENSE
```

---

## 📊 Results Summary

| Model | Accuracy | Precision | Recall | F1 | AUC |
|---|---|---|---|---|---|
| Logistic Regression | 84.2% | 83.1% | 82.7% | 82.9% | 0.91 |
| Decision Tree | 88.6% | 87.9% | 88.1% | 88.0% | 0.93 |
| SVM | 91.3% | 90.8% | 91.0% | 90.9% | 0.95 |
| LSTM | 93.7% | 93.2% | 93.5% | 93.3% | 0.97 |
| XGBoost | 95.4% | 95.1% | 94.9% | 95.0% | 0.98 |
| Random Forest | 96.1% | 95.8% | 96.0% | 95.9% | 0.98 |
| BERT (Fine-Tuned) | 97.8% | 97.4% | 97.6% | 97.5% | 0.99 |
| **Hybrid RF+BERT** | **98.7%** | **97.9%** | **98.4%** | **98.1%** | **0.99** |

---

## ⚙️ Installation

```bash
# 1. Clone the repository
git clone https://github.com/suresh-shinde/web-attack-ml-detection.git
cd web-attack-ml-detection

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate       # Linux/Mac
venv\Scripts\activate          # Windows

# 3. Install dependencies
pip install -r requirements.txt
```

---

## 📥 Dataset Setup

Download the following free, public datasets and place them in `data/raw/`:

| Dataset | Link | File |
|---|---|---|
| CSIC 2010 | [Download](http://www.isi.csic.es/dataset/) | `csic_2010.csv` |
| HTTPD Logs | [Kaggle](https://www.kaggle.com/) | `httpd_logs.csv` |
| OWASP WebGoat | [OWASP](https://owasp.org/www-project-webgoat/) | `webgoat_logs.csv` |

Then run preprocessing:

```bash
python src/preprocess.py
```

---

## 🚀 Quick Start

### Train All Models
```bash
python src/train_rf.py
python src/train_bert.py
```

### Run Evaluation
```bash
python src/evaluate.py
```

### Real-Time Inference (Single Request)
```bash
python src/inference.py --payload "SELECT * FROM users WHERE id=1 OR 1=1--"
```

### Launch Inference API
```bash
uvicorn src.inference:app --host 0.0.0.0 --port 8000
```

---

## 🧪 Example Output

```bash
$ python src/inference.py --payload "SELECT * FROM users WHERE id=1 OR 1=1--"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  🚨 ATTACK DETECTED
  Type     : SQL Injection (SQLi)
  Confidence: 99.3%
  RF Score : 0.98
  BERT Score: 0.991
  Inference : 7.4ms
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## 📖 Citation

If you use this work in your research, please cite:

```bibtex
@article{shinde2026webattackml,
  title   = {Machine Learning-Based Real-Time Detection of SQL Injection
             and XSS Attacks in Web Applications},
  author  = {Suresh Shinde},
  journal = {arXiv preprint arXiv:2026.XXXXX},
  year    = {2026},
  url     = {https://arxiv.org/abs/2026.XXXXX}
}
```

---

## 🤝 Contact

**Suresh Shinde**
IT Solutions & Web Expert | Techno Experts
📧 suresh@technoexperts.co
🌐 [technoexperts.co](https://www.technoexperts.co/)
🔗 [linkedin.com/in/suresh-shinde](https://linkedin.com/in/suresh-shinde)

---

*© 2026 Suresh Shinde, [Techno Experts](https://www.technoexperts.co/). Licensed under CC BY 4.0*
