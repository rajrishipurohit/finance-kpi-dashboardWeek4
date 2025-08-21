# Finance KPI Dashboard - Week 2 Upgrade
# Run inside your venv
# pip install pandas matplotlib

import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("finance_kpi_sample.csv")
print("Data Loaded:")
print(df)

# --- Extra KPIs ---
# Late Payment %
df["Late_Payment_Rate_%"] = (df["Late_Payments"] / df["Total_Invoices"] * 100).round(1)

# Month-over-Month Growth %
df["Revenue_MoM_%"] = (df["Revenue_in_Million"].pct_change() * 100).round(1)
df["Invoices_MoM_%"] = (df["Total_Invoices"].pct_change() * 100).round(1)

# Save enriched dataset
df.to_csv("finance_kpi_enriched.csv", index=False)
print("Enriched data saved as finance_kpi_enriched.csv")

# --- Charts ---

# 1. Total Invoices
plt.figure(figsize=(8,5))
plt.plot(df["Month"], df["Total_Invoices"], marker='o')
plt.title("Total Invoices per Month")
plt.xlabel("Month")
plt.ylabel("Invoices")
plt.grid(True)
plt.savefig("chart_invoices.png", dpi=150)
plt.show()

# 2. Revenue
plt.figure(figsize=(8,5))
plt.bar(df["Month"], df["Revenue_in_Million"], color='green')
plt.title("Monthly Revenue (in Million)")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.savefig("chart_revenue.png", dpi=150)
plt.show()

# 3. Late Payment %
plt.figure(figsize=(8,5))
plt.bar(df["Month"], df["Late_Payment_Rate_%"], color='red')
plt.title("Late Payment Rate (%)")
plt.xlabel("Month")
plt.ylabel("Rate (%)")
plt.savefig("chart_late_rate.png", dpi=150)
plt.show()
