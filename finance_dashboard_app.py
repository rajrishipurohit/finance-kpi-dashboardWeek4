# Finance KPI Dashboard - Interactive (Streamlit)
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Finance KPI Dashboard", layout="wide")


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
st.sidebar.metric("👥 Total Visitors", count)

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

# Show visitor stats
st.sidebar.subheader("👥 Visitors Analytics <Feature just gone>")

# Insights
st.subheader("Key Insights")
latest = df.iloc[-1]
previous = df.iloc[-2]
st.write(f"📌 Last Month Revenue: **{latest['Revenue_in_Million']}M**")
st.write(f"📌 MoM Revenue Change: **{latest['Revenue_MoM_%']}%**")
st.write(f"📌 Late Payment Rate: **{latest['Late_Payment_Rate_%']}%**")
st.write("Hello World, that's where life starts, that's where the magic happens")