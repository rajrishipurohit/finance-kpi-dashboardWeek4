# Finance KPI Dashboard - Interactive (Streamlit)
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os
import requests
import json

st.set_page_config(page_title="Finance KPI Dashboard", layout="wide")


# Code for visitor location and the respective counts from that country

# ---- Visitor Data File ----
counter_file = "visitor_data.json"

# Initialize file if not exists
if not os.path.exists(counter_file):
    with open(counter_file, "w") as f:
        json.dump({"count": 0, "countries": {}}, f)

# Read current data
with open(counter_file, "r") as f:
    data = json.load(f)

# Increment total visitor count
data["count"] += 1

# ---- Country Detection ----
def get_user_country():
    try:
        res = requests.get("https://ipapi.co/json/")
        info = res.json()
        return info.get("country_name", "Unknown")
    except:
        return "Unknown"

country = get_user_country()

# Update country visit count
if country in data["countries"]:
    data["countries"][country] += 1
else:
    data["countries"][country] = 1

# Save updated data
with open(counter_file, "w") as f:
    json.dump(data, f)

# ---- Show in Sidebar ----
st.sidebar.metric("👥 Total Visitors", data["count"])
st.sidebar.subheader("🌍 Visitors by Country")

for c, visits in data["countries"].items():
    st.sidebar.write(f"{c}: {visits}")

# Code for the counter:
import os
# Path to store visitor count (Streamlit Cloud keeps it while app is running)
counter_file = "visitor_count.txt"

# Initialize file if not exists
if not os.path.exists(counter_file):
    with open(counter_file, "w") as f:
        f.write("0")

# Read current count
with open(counter_file, "r") as f:
    count = int(f.read())

# Increment count
count += 1

# Save updated count
with open(counter_file, "w") as f:
    f.write(str(count))

# Display on sidebar
st.sidebar.metric("👥 Total Visitors", count, "New Feature ;)")

# Load Data
df = pd.read_csv("finance_kpi_enriched.csv")

# Page Title
st.title("📊 Finance KPI Dashboard")

# Show raw data (toggle)
if st.checkbox("Show Raw Data"):
    st.dataframe(df)

# Chart 1: Invoices
st.subheader("Total Invoices per Month")
st.line_chart(df.set_index("Month")["Total_Invoices"])

# Chart 2: Revenue
st.subheader("Monthly Revenue (in Million)")
st.bar_chart(df.set_index("Month")["Revenue_in_Million"])

# Chart 3: Late Payment %
st.subheader("Late Payment Rate (%)")
st.bar_chart(df.set_index("Month")["Late_Payment_Rate_%"])

# Insights
st.subheader("Key Insights")
latest = df.iloc[-1]
previous = df.iloc[-2]
st.write(f"📌 Last Month Revenue: **{latest['Revenue_in_Million']}M**")
st.write(f"📌 MoM Revenue Change: **{latest['Revenue_MoM_%']}%**")
st.write(f"📌 Late Payment Rate: **{latest['Late_Payment_Rate_%']}%**")
st.write("Hello World, that's where life starts, that's where the magic happens")