import streamlit as st
import pandas as pd
import plotly.express as px

# Configure page layout
st.set_page_config(page_title="Sales Dashboard", layout="wide")

st.title("📊 Sales Data Visualization")

# Sample dataset
data = {
    "Category": ["Electronics", "Clothing", "Home & Kitchen", "Books", "Toys"],
    "Sales": [45000, 28000, 32000, 15000, 18000],
    "Profit": [12000, 7500, 8900, 4200, 3100]
}
df = pd.DataFrame(data)

# Sidebar interactive filter
selected_metric = st.sidebar.selectbox(
    "Select metric to visualize:",
    options=["Sales", "Profit"]
)

# Display charts side by side
col1, col2 = st.columns(2)

with col1:
    st.subheader(f"{selected_metric} by Category (Bar Chart)")
    fig_bar = px.bar(
        df,
        x="Category",
        y=selected_metric,
        color="Category",
        text_auto=True,
        title=f"Total {selected_metric} per Category"
    )
    fig_bar.update_layout(showlegend=False)
    st.plotly_chart(fig_bar, use_container_width=True)

with col2:
    st.subheader(f"Share of {selected_metric} (Pie Chart)")
    fig_pie = px.pie(
        df,
        names="Category",
        values=selected_metric,
        title=f"{selected_metric} Distribution",
        hole=0.3  # Set to 0 for a solid pie chart or keep for a donut chart
    )
    fig_pie.update_traces(textposition="inside", textinfo="percent+label")
    st.plotly_chart(fig_pie, use_container_width=True)

# Raw data table
with st.expander("View Raw Data"):
    st.dataframe(df)
