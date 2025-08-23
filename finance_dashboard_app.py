# ============================================================
# Finance KPI Dashboard - Interactive (Streamlit)
# Author: Raj Rishi Purohit
# ============================================================

# ---- Imports ----
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os
import json
import requests

# ---- Page Config ----
st.set_page_config(page_title="Finance KPI Dashboard", layout="wide")

# ============================================================
# SECTION 1: Visitor Tracking
# ============================================================

VISITOR_FILE = "visitor_data.json"

# Initialize visitor data if not exists
if not os.path.exists(VISITOR_FILE):
    with open(VISITOR_FILE, "w") as f:
        json.dump({"count": 0, "countries": {}}, f)

# Load visitor data
with open(VISITOR_FILE, "r") as f:
    visitor_data = json.load(f)

# Increment total visits
visitor_data["count"] += 1

# Detect visitor country (⚠️ On Streamlit Cloud, may show US for everyone)
def get_user_country():
    try:
        res = requests.get("https://ipapi.co/json/")
        info = res.json()
        return info.get("country_name", "Unknown")
    except:
        return "Unknown"

country = get_user_country()

# Update country count
if country in visitor_data["countries"]:
    visitor_data["countries"][country] += 1
else:
    visitor_data["countries"][country] = 1

# Save updated visitor data
with open(VISITOR_FILE, "w") as f:
    json.dump(visitor_data, f)

# ---- Sidebar: Visitor Stats ----
st.sidebar.header("📈 Visitor Analytics")
st.sidebar.metric("👥 Total Visitors", visitor_data["total_visits"])
st.sidebar.subheader("🌍 Visitors by Country")
for c, visits in visitor_data["countries"].items():
    st.sidebar.write(f"{c}: {visits}")

# ============================================================
# SECTION 2: Finance KPI Dashboard
# ============================================================

# ---- Load Data ----
df = pd.read_csv("finance_kpi_enriched.csv")

# ---- Page Title ----
st.title("📊 Finance KPI Dashboard: Local Finance Services (LFS)")

# ---- Toggle Raw Data ----
if st.checkbox("Show Raw Data"):
    st.dataframe(df)

# ---- Chart 1: Invoices ----
st.subheader("Total Invoices per Month")
st.line_chart(df.set_index("Month")["Total_Invoices"])

# ---- Chart 2: Revenue ----
st.subheader("Monthly Revenue (in Million)")
st.bar_chart(df.set_index("Month")["Revenue_in_Million"])

# ---- Chart 3: Late Payment % ----
st.subheader("Late Payment Rate (%)")
st.bar_chart(df.set_index("Month")["Late_Payment_Rate_%"])

# ---- Key Insights ----
st.subheader("Key Insights")
latest = df.iloc[-1]
previous = df.iloc[-2]
st.write(f"📌 Last Month Revenue: **{latest['Revenue_in_Million']}M**")
st.write(f"📌 MoM Revenue Change: **{latest['Revenue_MoM_%']}%**")
st.write(f"📌 Late Payment Rate: **{latest['Late_Payment_Rate_%']}%**")

# ---- Footer ----
st.markdown("---")
st.caption("Developed by Raj Rishi Purohit | Visit my [GitHub](https://github.com/rajrishipurohit)")