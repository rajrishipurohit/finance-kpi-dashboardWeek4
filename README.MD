# 📊 Finance KPI Dashboard

A simple yet powerful **interactive finance KPI dashboard** built with **Python (pandas, matplotlib) and Streamlit**.
This project showcases my ability to combine **finance domain expertise** with **modern data tools** to create insightful, demo-ready apps.

---

## 🚀 Live Demo

🔗 [Click here to open the app](https://slekpi.streamlit.app)

---

## 📌 Features

* ✅ Monthly KPIs tracked: **Revenue, Total Invoices, Late Payment Rate**
* ✅ Derived metrics: **Month-over-Month % change**
* ✅ **Interactive dashboard** with:

  * Sidebar filters for month range & KPI selection
  * Auto-updating charts
  * Trend highlights (🟢 Growth / 🔴 Decline)
* ✅ Clean deployment on **Streamlit Community Cloud**

---

## 📂 Project Structure

```
finance-kpi-dashboardWeek4/
│
├── finance_dashboard_app.py       # Main Streamlit app
├── finance_kpi_enriched.csv       # Cleaned dataset with MoM calculations
├── requirements.txt               # Minimal dependencies
├── README.md                      # Project documentation
└── charts/                        # Saved PNGs of KPI charts (optional)
```

---

## ⚙️ Installation (Run Locally)

Clone the repo and install requirements:

```bash
git clone https://github.com/rajrishipurohit/finance-kpi-dashboardWeek4.git
cd finance-kpi-dashboardWeek4

# (Optional) Create virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the dashboard
streamlit run finance_dashboard_app.py
```

---
