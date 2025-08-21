# Finance KPI Dashboard - Interactive (Streamlit)
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

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
st.write("Hello World")