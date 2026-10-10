# 📋 11.11 Sales Analytics Project Execution Plan

## 1. Project Overview & Objectives
This project implements an end-to-end Big Data analytics pipeline and executive dashboard evaluating e-commerce performance during an 11.11 Mega Sale event. The system generates 1,000,000 synthetic transaction records with intentional anomalies, cleans and aggregates the data at scale using PySpark, serves lightweight analytics outputs via Streamlit, and provides automated C-suite briefings utilizing the Google Gemini API.

---

## 2. Technical Stack Architecture

| Layer | Tool / Library | Purpose |
| :--- | :--- | :--- |
| **Data Generation** | `pyspark.sql`, `random` | Generate 1M raw transactions with injected data quality issues. |
| **Processing & Cleaning** | PySpark DataFrames | Distributed filtering, null handling, metric aggregation. |
| **Storage & Export** | CSV / Parquet | Intermediate analytical results stored under `results/`. |
| **Visualization & App** | Streamlit, Plotly Express | Interactive, mobile-responsive analytics dashboard (`app.py`). |
| **Generative AI** | Google GenAI SDK (`google-genai`) | Automated executive summary generation (`gemini-2.5-flash`). |
| **Version Control & Hosting**| GitHub, Streamlit Community Cloud | Continuous integration and public deployment. |

---

## 3. End-to-End Pipeline Workflow

```
[Raw Data Gen (1M Rows)]
          │
          ▼
[PySpark Data Cleaning] ──► Handle Nulls, Duplicate Removal, Invalid Range Filters
          │
          ▼
[PySpark Scale Aggregations]
          ├── Revenue by Category
          ├── Hourly Order Volumes (Peak Detection)
          ├── Regional Metrics
          ├── Payment Cancellation Rates
          └── Average Order Value (AOV)
          │
          ▼
[CSV Export to results/]
          │
          ▼
[Streamlit Dashboard (app.py)] ◄── Secrets Management (GEMINI_API_KEY)
          │
          ├── Responsive Plotly Charts & Metrics
          └── Gemini AI Executive Briefing Integration
```

---

## 4. Phase Breakdown & Deliverables

### Phase 1: Data Generation & Ingestion (Task A)
- Generate 1,000,000 records simulating 11.11 peak sales traffic.
- Inject synthetic errors: missing values, uncalibrated timestamps, negative price/quantity anomalies.
- Save raw data as `1111_sale_orders.csv`.

### Phase 2: PySpark Data Cleaning (Task B)
- Deduplicate record IDs.
- Filter out negative item prices and invalid order quantities.
- Impute or handle null customer geographic metadata.
- Parse timestamps into structured hour/day components.

### Phase 3: Scale Analytics & Aggregations (Tasks C & D)
- Calculate total delivered revenue by category.
- Detect peak traffic hours (12:00 AM - 1:00 AM & 8:00 PM - 10:00 PM spikes).
- Analyze regional fulfillment efficiency and cancellation rates across payment methods (COD vs. Digital).
- Export aggregated summary files to `results/`:
  1. `1_revenue_by_category.csv`
  2. `2_orders_per_hour.csv`
  3. `3_metrics_by_region.csv`
  4. `4_cancellation_rate.csv`
  5. `5_average_order_value.csv`

### Phase 4: Web Application & Visualization (Task E)
- Construct a responsive Streamlit dashboard (`app.py`).
- Implement KPI metric cards for Revenue, Order Volume, AOV, and Cancellation Rate.
- Render interactive Plotly Express charts (Category Revenue Bar, Hourly Orders Line Chart).
- Add dynamic regional filtering capability.

### Phase 5: Generative AI Briefing Integration (Task F)
- Integrate `google-genai` SDK using Streamlit Secrets (`GEMINI_API_KEY`).
- Prompt engineer `gemini-2.5-flash` to restrict insights strictly to provided summary metrics.
- Produce a structured 5-sentence executive briefing ending with a concrete operational recommendation.
- Implement error handling and rule-based fallbacks for API resilience.

### Phase 6: Cloud Deployment & Secrets Configuration (Task G)
- Host code, summary datasets, and requirements on GitHub.
- Connect GitHub repository to Streamlit Community Cloud.
- Configure encrypted API key access under App Secrets settings.

### Phase 7: Reflection & Ethics Analysis (Task H)
- Document compliance guidelines under the Philippine Data Privacy Act of 2012 (DPA).
- Address ethical implications of Cash on Delivery (COD) restrictions on unbanked consumers.
- Evaluate Big Data characteristics (Volume & Velocity) and emerging IoT integrations in e-commerce fulfillment.

---

## 5. Repository Structure
```
sales_analytics_elijah/
├── .streamlit/
│   └── secrets.toml          # Local secrets config (git-ignored)
├── results/
│   ├── 1_revenue_by_category.csv
│   ├── 2_orders_per_hour.csv
│   ├── 3_metrics_by_region.csv
│   ├── 4_cancellation_rate.csv
│   └── 5_average_order_value.csv
├── app.py                     # Main Streamlit dashboard script
├── requirements.txt           # Python library dependencies
├── README.md                  # Project overview & Gemini prompt documentation
├── REFLECTION.md              # Task H ethics, privacy, and big data reflection
└── PLAN.md                    # System architecture and project plan
```