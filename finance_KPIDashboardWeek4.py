# Finance KPI Dashboard - Interactive with Filters
import streamlit as st
import pandas as pd

# Load Data
df = pd.read_csv("finance_kpi_enriched.csv")

# Page Title
st.title("📊 Finance KPI Dashboard (v2 with Filters)")

# --- Sidebar ---
st.sidebar.header("Filters")

# Month Range Filter
months = df["Month"].tolist()
start, end = st.sidebar.select_slider(
    "Select Month Range",
    options=months,
    value=(months[0], months[-1])
)

# Filter dataset based on range
start_idx = df.index[df["Month"] == start][0]
end_idx = df.index[df["Month"] == end][0]
df_filtered = df.loc[start_idx:end_idx]

# KPI Selector
kpi_choice = st.sidebar.radio(
    "Choose KPI to view:",
    ["Revenue_in_Million", "Total_Invoices", "Late_Payment_Rate_%"]
)

# --- Main Area ---
st.subheader(f"KPI: {kpi_choice}")
st.line_chart(df_filtered.set_index("Month")[kpi_choice])

# --- Key Insights ---
st.subheader("Key Insights")

latest = df_filtered.iloc[-1]
previous = df_filtered.iloc[-2] if len(df_filtered) > 1 else latest

rev_change = latest["Revenue_MoM_%"]

if rev_change > 0:
    trend = f"🟢 Revenue grew by {rev_change}% MoM"
elif rev_change < 0:
    trend = f"🔴 Revenue dropped by {abs(rev_change)}% MoM"
else:
    trend = "Revenue stayed flat"

st.write(f"📌 Last Month Revenue: **{latest['Revenue_in_Million']}M**")
st.write(f"📌 {trend}")
st.write(f"📌 Late Payment Rate: **{latest['Late_Payment_Rate_%']}%**")
