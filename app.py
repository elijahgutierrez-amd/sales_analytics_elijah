import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="11.11 Analytics", layout="wide")
st.title("🛍️ 11.11 Sale Performance Dashboard")

@st.cache_data
def load_data():
    rev_cat = pd.read_csv("results/1_revenue_by_category.csv")
    ord_hour = pd.read_csv("results/2_orders_per_hour.csv")
    metrics_reg = pd.read_csv("results/3_metrics_by_region.csv")
    canc_pm = pd.read_csv("results/4_cancellation_rate.csv")
    aov_df = pd.read_csv("results/5_average_order_value.csv")
    return rev_cat, ord_hour, metrics_reg, canc_pm, aov_df

rev_cat, ord_hour, metrics_reg, canc_pm, aov_df = load_data()

# Metrics
total_revenue = aov_df['total_delivered_revenue'].iloc[0]
total_orders = metrics_reg['total_orders'].sum()
avg_cancellation = (canc_pm['cancelled_orders'].sum() / total_orders) * 100
aov_val = aov_df['average_order_value'].iloc[0]

c1, c2, c3, c4 = st.columns(4)
c1.metric("Delivered Revenue", f"₱{total_revenue:,.2f}")
c2.metric("Total Orders", f"{total_orders:,.0f}")
c3.metric("Cancellation Rate", f"{avg_cancellation:.2f}%")
c4.metric("AOV", f"₱{aov_val:,.2f}")

st.divider()

# Region Filter
selected_region = st.selectbox("Select Region Filter:", ["All Regions"] + list(metrics_reg['region'].unique()))
filtered_reg = metrics_reg if selected_region == "All Regions" else metrics_reg[metrics_reg['region'] == selected_region]

fig_region = px.bar(filtered_reg, x="region", y="delivered_revenue", title="Revenue by Region", color="delivered_revenue")
st.plotly_chart(fig_region, use_container_width=True)

# Charts
fig_cat = px.bar(rev_cat, x="category", y="total_revenue", title="Revenue by Category", color="total_revenue")
st.plotly_chart(fig_cat, use_container_width=True)

fig_hour = px.line(ord_hour, x="hour", y="order_count", markers=True, title="Orders per Hour")
st.plotly_chart(fig_hour, use_container_width=True)
