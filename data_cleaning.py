import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import seaborn as sns
import missingno as msno
from collections import Counter
import numpy as np

st.set_page_config(page_title="📊 Data Explorer Dashboard", layout="wide")
st.title("📊 Interactive Data Analysis Dashboard")

st.sidebar.header("Upload Dataset")
upload = st.sidebar.file_uploader("Choose a CSV file", type="csv")

# Helper functions
def find_cat_cont_columns(df):
    cont_columns, cat_columns = [], []
    for col in df.columns:
        if df[col].dtype == object or len(df[col].unique()) <= 25:
            cat_columns.append(col)
        else:
            cont_columns.append(col)
    return cont_columns, cat_columns

def create_sales_funnel(df, stage_col):
    stage_counts = df[stage_col].value_counts().reset_index()
    stage_counts.columns = ['Stage', 'Count']
    fig = go.Figure(go.Funnel(
        y=stage_counts['Stage'],
        x=stage_counts['Count'],
        textinfo="value+percent initial+percent previous"
    ))
    return fig


# Main Dashboard
if upload:
    df = pd.read_csv(upload)
    cont_columns, cat_columns = find_cat_cont_columns(df)
   
    

    # Data Cleaning: Handling missing values
    df_cleaned = df.copy()
    missing_summary = []

    

    # Fill missing values: mean for continuous, mode for categorical
    for col in cont_columns:
        if df_cleaned[col].isnull().sum() > 0:
            df_cleaned[col].fillna(df_cleaned[col].mean(), inplace=True)
            missing_summary.append(f"🔹 '{col}' (continuous) → filled with mean")

    for col in cat_columns:
        if df_cleaned[col].isnull().sum() > 0:
            df_cleaned[col].fillna(df_cleaned[col].mode()[0], inplace=True)
            missing_summary.append(f"🔸 '{col}' (categorical) → filled with mode")


    apply_cleaning = st.sidebar.checkbox("🧹 Clean Missing Values (Mean/Mode)", value=True)
    remove_duplicates = st.sidebar.checkbox("🧹 Remove Duplicate Rows", value=True)
    
    if apply_cleaning:
        df_used = df_cleaned
    else:
        df_used = df

    if remove_duplicates:
        num_duplicates = df_cleaned.duplicated().sum()
        df_cleaned.drop_duplicates(inplace=True)
    else:
        num_duplicates = df_cleaned.duplicated().sum()
        
    tabs = st.tabs(["📁 Overview", "📈 Visualizations", "📊 Feature Analysis", "📉 Relationships"])

    with tabs[0]:
        st.header("Dataset Overview")
        st.dataframe(df_used.head())

        st.markdown(f"**Shape:** {df_used.shape[0]} rows × {df_used.shape[1]} columns")
        st.markdown(f"**Missing Values:** {df_used.isnull().sum().sum()}")
        st.markdown(f"**Continuous Columns:** {len(cont_columns)}")
        st.write(cont_columns)
        st.markdown(f"**Categorical Columns:** {len(cat_columns)}")
        st.write(cat_columns)
        if missing_summary:
            st.subheader("🧼 Missing Values Treated")
            for msg in missing_summary:
                st.markdown(msg)
        else:
            st.subheader("✅ No Missing Values Detected")
        st.subheader("🧩 Duplicate Rows")
        if num_duplicates > 0:
            st.markdown(f"⚠️ Found and removed **{num_duplicates}** duplicate row(s).")
        else:
            st.markdown("✅ No duplicate rows found.")
            st.subheader("Sales Funnel Overview")
        
        st.subheader("Sales Funnel")
        funnel_col = st.selectbox("Select a Column for Sales Funnel", cat_columns, key="overview_funnel_selector")
        

        if funnel_col:
            funnel_fig = create_sales_funnel(df_used, funnel_col)
            st.plotly_chart(funnel_fig, use_container_width=True, key="overview_funnel_chart")



    with tabs[1]:
        st.header("Visual Explorations")

        chart_type = st.selectbox("Select Chart Type", ["Bar Chart", "Pie Chart", "Sales Funnel"])

        if chart_type in ["Bar Chart", "Pie Chart", "Sales Funnel"] and not cat_columns:
            st.warning("No categorical columns found in the dataset.")
        else:
            if chart_type == "Bar Chart":
                col = st.selectbox("Select Categorical Column", cat_columns)
                count_data = df_used[col].value_counts().reset_index(name='Count')
                count_data.columns = [col, 'Count']
                fig = px.bar(count_data, x=col, y='Count', labels={col: col, 'Count': 'Count'})
                st.plotly_chart(fig, use_container_width=True)

            elif chart_type == "Pie Chart":
                col = st.selectbox("Select Categorical Column", cat_columns)
                count_data = df_used[col].value_counts().reset_index(name='Count')
                count_data.columns = [col, 'Count']
                fig = px.pie(count_data, names=col, values='Count', title=f"Distribution of {col}")
                st.plotly_chart(fig, use_container_width=True)

            elif chart_type == "Sales Funnel":
                col = st.selectbox("Select Column for Funnel", cat_columns)
                funnel_fig = create_sales_funnel(df_used, col)
                st.plotly_chart(funnel_fig, use_container_width=True)

    with tabs[2]:
        st.header("Analyze Features")

        feature = st.selectbox("Select a Feature", df_used.columns)
        st.write(df_used[feature].describe())
        if feature in cont_columns:
            fig = px.histogram(df_used, x=feature, nbins=30)
        

        else:
            value_counts = df_used[feature].value_counts().reset_index()
            value_counts.columns = [feature, 'Count']
            fig = px.bar(value_counts, x=feature, y='Count')
        st.plotly_chart(fig, use_container_width=True, key=f"{feature}_bar")


    with tabs[3]:
        st.header("Explore Relationships Between Features")

        if len(cont_columns) < 2:
            st.warning("Need at least two continuous columns to plot relationships.")
        else:
            x_axis = st.selectbox("X Axis", cont_columns)
            y_axis = st.selectbox("Y Axis", cont_columns, index=1)
            color = st.selectbox("Color By (optional)", [None] + cat_columns)

            fig = px.scatter(df_used, x=x_axis, y=y_axis, color=color)
            st.plotly_chart(fig, use_container_width=True)
else:
    st.warning("Please upload a CSV file to proceed.")
