# Finance KPI Dashboard - Starter Script
# Run this in VS Code on your Mac after installing pandas & matplotlib
# pip install pandas matplotlib

import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("finance_kpi_sample.csv")
print("Data Loaded:")
print(df)

# Plot Total Invoices
plt.figure(figsize=(8,5))
plt.plot(df["Month"], df["Total_Invoices"], marker='o')
plt.title("Total Invoices per Month")
plt.xlabel("Month")
plt.ylabel("Invoices")
plt.grid(True)
plt.savefig("chart_invoices.png", dpi=150)   # SAVE as PNG

plt.show()

# Plot Revenue
plt.figure(figsize=(8,5))
plt.bar(df["Month"], df["Revenue_in_Million"], color='green')
plt.title("Monthly Revenue (in Million)")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.savefig("chart_invoices 2nd wala.png", dpi=250)   # SAVE as PNG

plt.show()

# Save cleaned data (optional)
df.to_csv("finance_kpi_cleaned.csv", index=False)
print("Cleaned data saved as finance_kpi_cleaned.csv")
