import pandas as pd

df = pd.read_excel(
    "supermarket.xlsx",
    skiprows=7
    )
df = df.drop(columns=["Unnamed: 0"])


print(df.head())
print(df.columns)
print(df.shape)
# ---- BASIC METRICS ----

total_revenue = df["Total (USD)"].sum()
total_tax = df["Tax (USD)"].sum()
total_orders = df["Order No"].nunique()


print("Total Revenue (USD):", round(total_revenue, 2))
print("Total Tax Collected (USD):", round(total_tax, 2))
print("Total Orders:", total_orders)
customer_sales = (
    df.groupby("Customer Name")["Total (USD)"]
    .sum()
    .sort_values(ascending=False)
)
print("top customer revenue name ")
print(customer_sales.head())
# DATE WISE SALES

df["Order Date"] = pd.to_datetime(df["Order Date"])

date_sales = (
    df.groupby("Order Date")["Total (USD)"]
    .sum()
    .sort_values(ascending=False)
)

print("Top 5 Sales Days:")
print(date_sales.head())
import matplotlib.pyplot as plt

# Date-wise sales (agar pehle se nahi hai)
date_sales = df.groupby("Order Date")["Total (USD)"].sum()

# Line graph
plt.figure()
date_sales.plot()
plt.title("Date-wise Sales Trend")
plt.xlabel("Order Date")
plt.ylabel("Total Sales (USD)")
plt.show()
import matplotlib.pyplot as plt

# Top 5 customers
top_customers = (
    df.groupby("Customer Name")["Total (USD)"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
)

plt.figure()
top_customers.plot(kind="bar")
plt.title("Top 5 Customers by Revenue")
plt.xlabel("Customer Name")
plt.ylabel("Total Revenue (USD)")
plt.xticks(rotation=45)
plt.show()
plt.figure()
top_customers.plot(kind="pie", autopct="%1.1f%%")
plt.title("Revenue Contribution by Top 5 Customers")
plt.ylabel("")   # side ka label hatane ke liye
plt.show()




