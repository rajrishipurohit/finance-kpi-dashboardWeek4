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
        json.dump({"total_visits": 0, "countries": {}}, f)

# Load visitor data
with open(VISITOR_FILE, "r") as f:
    visitor_data = json.load(f)

# ---- Backward compatibility fix ----
# (handles old "count" key from previous versions)
if "total_visits" not in visitor_data:
    if "count" in visitor_data:
        visitor_data["total_visits"] = visitor_data["count"]
        del visitor_data["count"]
    else:
        visitor_data["total_visits"] = 0

if "countries" not in visitor_data:
    visitor_data["countries"] = {}

# Increment total visits
visitor_data["total_visits"] += 1

# Detect visitor country (⚠️ On Streamlit Cloud may always show US)
def get_user_country():
    try:
        res = requests.get("https://ipapi.co/json/")
        info = res.json()
        return info.get("country_name", "Unknown")
    except:
        return "Unknown"

country = get_user_country()

# Update country count
visitor_data["countries"][country] = visitor_data["countries"].get(country, 0) + 1

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
st.title("📊 Finance KPI Dashboard: Local Finance Services")

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
st.caption("Hello World, that's where life starts, that's where the magic happens 🚀")
st.caption("Developed by Raj Rishi Purohit")