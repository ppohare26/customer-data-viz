import streamlit as st
import plotly.express as px
from util.helpers import create_sales_funnel

def render(df, cat_columns):
    st.header("Visual Explorations")

    chart_type = st.selectbox("Select Chart Type", ["Bar Chart", "Pie Chart", "Sales Funnel"])

    if chart_type in ["Bar Chart", "Pie Chart", "Sales Funnel"] and not cat_columns:
        st.warning("No categorical columns found in the dataset.")
        return

    col = st.selectbox("Select Column", cat_columns)

    if chart_type == "Bar Chart":
        count_data = df[col].value_counts().reset_index(name='Count')
        count_data.columns = [col, 'Count']
        fig = px.bar(count_data, x=col, y='Count',color=col, color_discrete_sequence=px.colors.qualitative.Pastel)
        st.plotly_chart(fig, use_container_width=True)

    elif chart_type == "Pie Chart":
        count_data = df[col].value_counts().reset_index(name='Count')
        count_data.columns = [col, 'Count']
        fig = px.pie(count_data, names=col, values='Count', title=f"Distribution of {col}", color=col, color_discrete_sequence=px.colors.sequential.RdBu)
        st.plotly_chart(fig, use_container_width=True)

    elif chart_type == "Sales Funnel":
        funnel_fig = create_sales_funnel(df, col)
        st.plotly_chart(funnel_fig, use_container_width=True)
