import streamlit as st
import pandas as pd
import plotly.express as px
from google import genai
from google.genai import errors

# 1. Page Configuration
st.set_page_config(page_title="11.11 Analytics Dashboard", layout="wide")
st.title("🛍️ 11.11 Sale Performance Dashboard")

# 2. Load Summary Data
@st.cache_data
def load_data():
    rev_cat = pd.read_csv("results/1_revenue_by_category.csv")
    ord_hour = pd.read_csv("results/2_orders_per_hour.csv")
    metrics_reg = pd.read_csv("results/3_metrics_by_region.csv")
    canc_pm = pd.read_csv("results/4_cancellation_rate.csv")
    aov_df = pd.read_csv("results/5_average_order_value.csv")
    return rev_cat, ord_hour, metrics_reg, canc_pm, aov_df

try:
    rev_cat, ord_hour, metrics_reg, canc_pm, aov_df = load_data()
except Exception as e:
    st.error(f"Error loading summary files from results/: {e}")
    st.stop()

# Extract Key Metrics
total_revenue = aov_df['total_delivered_revenue'].iloc[0]
total_orders = metrics_reg['total_orders'].sum()
avg_cancellation = (canc_pm['cancelled_orders'].sum() / total_orders) * 100
aov_val = aov_df['average_order_value'].iloc[0]
top_category = rev_cat.iloc[0]['category']
top_category_rev = rev_cat.iloc[0]['total_revenue']
highest_canc_pm = canc_pm.iloc[0]['payment_method']
highest_canc_rate = canc_pm.iloc[0]['cancellation_rate_pct']

# Top Metrics Row
c1, c2, c3, c4 = st.columns(4)
c1.metric("Delivered Revenue", f"₱{total_revenue:,.2f}")
c2.metric("Total Orders", f"{total_orders:,.0f}")
c3.metric("Cancellation Rate", f"{avg_cancellation:.2f}%")
c4.metric("AOV", f"₱{aov_val:,.2f}")

st.divider()

# ---------------------------------------------------------
# TASK F: GENERATIVE AI BRIEFING SECTION
# ---------------------------------------------------------
st.subheader("🤖 AI Executive Briefing")

if st.button("Generate Briefing", type="primary"):
    # Check if API key exists in secrets
    if "GEMINI_API_KEY" not in st.secrets:
        st.error("⚠️ GEMINI_API_KEY is not configured in Streamlit secrets.")
    else:
        with st.spinner("Analyzing performance metrics with Gemini..."):
            try:
                # Initialize Gemini client using key from Streamlit secrets
                client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

                # Strictly grounded prompt using only passed numbers
                prompt = f"""
You are an executive e-commerce analyst briefing a store owner on their 11.11 sale performance.
You MUST rely strictly on the provided dataset summary numbers below and make NO assumptions or extrapolations beyond this data.

Summary Data:
- Total Delivered Revenue: ₱{total_revenue:,.2f}
- Total Orders Placed: {total_orders:,}
- Average Order Value (AOV): ₱{aov_val:,.2f}
- Overall Cancellation Rate: {avg_cancellation:.2f}%
- Top Performing Category: {top_category} with ₱{top_category_rev:,.2f} in delivered revenue
- Highest Cancellation Payment Method: {highest_canc_pm} with a cancellation rate of {highest_canc_rate:.2f}%

Task:
Write a concise briefing that is EXACTLY 5 sentences long:
1. State the overall revenue and order volume achieved during the sale.
2. Mention the top-performing category and its revenue contribution.
3. Highlight the average order value and overall cancellation performance.
4. Call out the payment method with the highest cancellation rate.
5. Provide exactly ONE strategic recommendation for next year's sale based strictly on these numbers.
"""

                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=prompt
                )

                st.success("Briefing Generated Successfully!")
                st.info(response.text)

            except errors.APIError as e:
                st.error(f"Gemini API Error: {e.message}")
            except Exception as e:
                st.error(f"Failed to generate briefing: {str(e)}")

st.divider()

# Dashboard Visualizations
st.subheader("📊 Sales Analytics")
selected_region = st.selectbox("Select Region Filter:", ["All Regions"] + list(metrics_reg['region'].unique()))
filtered_reg = metrics_reg if selected_region == "All Regions" else metrics_reg[metrics_reg['region'] == selected_region]

fig_region = px.bar(filtered_reg, x="region", y="delivered_revenue", title="Revenue by Region", color="delivered_revenue")
st.plotly_chart(fig_region, use_container_width=True)

fig_cat = px.bar(rev_cat, x="category", y="total_revenue", title="Revenue by Category", color="total_revenue")
st.plotly_chart(fig_cat, use_container_width=True)

fig_hour = px.line(ord_hour, x="hour", y="order_count", markers=True, title="Orders per Hour")
st.plotly_chart(fig_hour, use_container_width=True)
