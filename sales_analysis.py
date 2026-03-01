import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(page_title="Sales Dashboard", layout="wide")

st.title("📊 Sales Data Analysis Dashboard")

# -----------------------------
# Load Dataset
# -----------------------------
df = pd.read_csv("sales_data.csv")

# Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"])

# Calculate Total Sales
df["Total_Sales"] = df["Quantity"] * df["Price"]

# -----------------------------
# Sidebar Filters
# -----------------------------
st.sidebar.header("Filter Options")

selected_region = st.sidebar.multiselect(
    "Select Region",
    options=df["Region"].unique(),
    default=df["Region"].unique()
)

selected_category = st.sidebar.multiselect(
    "Select Category",
    options=df["Category"].unique(),
    default=df["Category"].unique()
)

filtered_df = df[
    (df["Region"].isin(selected_region)) &
    (df["Category"].isin(selected_category))
]

# -----------------------------
# KPI Metrics
# -----------------------------
total_revenue = filtered_df["Total_Sales"].sum()
total_orders = filtered_df["Quantity"].sum()

col1, col2 = st.columns(2)

col1.metric("💰 Total Revenue", f"${total_revenue:,.2f}")
col2.metric("📦 Total Quantity Sold", total_orders)

# -----------------------------
# Category-wise Sales
# -----------------------------
st.subheader("Category-wise Sales")

category_sales = filtered_df.groupby("Category")["Total_Sales"].sum()

fig1, ax1 = plt.subplots()
category_sales.plot(kind="bar", ax=ax1)
ax1.set_ylabel("Total Sales")
st.pyplot(fig1)

# -----------------------------
# Region-wise Sales
# -----------------------------
st.subheader("Region-wise Sales Distribution")

region_sales = filtered_df.groupby("Region")["Total_Sales"].sum()

fig2, ax2 = plt.subplots()
region_sales.plot(kind="pie", autopct="%1.1f%%", ax=ax2)
ax2.set_ylabel("")
st.pyplot(fig2)

# -----------------------------
# -----------------------------
# Monthly Sales Trend
# -----------------------------
st.subheader("📈 Monthly Sales Trend")

# Convert to month period
filtered_df["Month"] = filtered_df["Date"].dt.to_period("M")

monthly_sales = filtered_df.groupby("Month")["Total_Sales"].sum()

fig3, ax3 = plt.subplots()
monthly_sales.plot(ax=ax3)

ax3.set_ylabel("Total Sales")
ax3.set_xlabel("Month")

st.pyplot(fig3)
# -----------------------------
# Raw Data Option
# -----------------------------
if st.checkbox("Show Raw Data"):
    st.dataframe(filtered_df)
