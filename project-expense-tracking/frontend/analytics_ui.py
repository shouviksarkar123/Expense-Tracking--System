import streamlit as st
from datetime import datetime
import requests
import pandas as pd

API_URL = "http://localhost:8000"

def analytics_tab():
    col1, col2 = st.columns(2)
    with col1:
        start_date = st.date_input("Start Date", datetime(2024, 8, 1))

    with col2:
        end_date = st.date_input("End Date", datetime(2024, 8, 5))

    if st.button("Get Analytics"):
        payload = {
            "start_date": start_date.strftime("%Y-%m-%d"),
            "end_date": end_date.strftime("%Y-%m-%d")
        }

        response = requests.post(f"{API_URL}/analytics/", json=payload).json()

        # ✔ Extract breakdown safely
        breakdown = response.get("breakdown", {})

        if not breakdown:
            st.warning("No expense data found in this date range.")
            return

        # ✔ Build proper DataFrame
        data = {
            "Category": list(breakdown.keys()),
            "Total": [breakdown[c]["total"] for c in breakdown],
            "Percentage": [breakdown[c]["percentage"] for c in breakdown]
        }

        df = pd.DataFrame(data).sort_values("Percentage", ascending=False)

        st.title("Expense Breakdown By Category")

        # ✔ Bar chart
        st.bar_chart(df.set_index("Category")["Percentage"], use_container_width=True)

        # ✔ Format values
        df["Total"] = df["Total"].map("{:.2f}".format)
        df["Percentage"] = df["Percentage"].map("{:.2f}".format)

        st.table(df)
