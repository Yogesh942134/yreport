# 📊 yreport

**yreport** is a lightweight, dataset-agnostic **data health reporting library** for tabular datasets.  
It analyzes data quality, detects potential issues, and provides **honest, actionable diagnostics** without making unsafe assumptions.

Unlike heavy EDA tools, `yreport` is designed to be:
- Pipeline-friendly
- Explainable
- Configurable
- Production-aware

---

## 🚀 Why yreport?

Most EDA libraries:
- Generate large HTML reports
- Make aggressive assumptions (e.g. one-hot everything)
- Are hard to integrate into ML pipelines

**yreport focuses on decisions, not decoration.**

It helps answer:
- Is this dataset usable?
- Which columns are problematic?
- What should be fixed first?
- Where should I be careful before modeling?

---

## ✨ Features

- Weighted **Data Health Score (0–100)**
- Automatic column type detection
- Missing value diagnostics with confidence levels
- High-cardinality categorical detection
- Numeric skewness and outlier analysis
- Honest categorical handling (no forced one-hot / ordinal)
- User override support
- Non-contradictory recommendations
- JSON and Markdown export
- scikit-learn Pipeline integration
- Lightweight and fast

---

## 📦 Installation

### Install from source (recommended)

```bash
git clone https://github.com/your-username/yreport.git
cd yreport
pip install -e .
