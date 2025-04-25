import streamlit as st
import pandas as pd
from util.helpers import find_cat_cont_columns
from util.cleaning import clean_missing_values, remove_duplicates
from tabs import overview, visualization, feature, relationship

st.set_page_config(page_title="📊 Data Explorer Dashboard", layout="wide")
st.title("📊  Data Analysis Dashboard")

upload = st.sidebar.file_uploader("Upload CSV", type="csv")

if upload:
    df = pd.read_csv(upload)
    cont_columns, cat_columns = find_cat_cont_columns(df)
    
    # Sidebar options
    apply_cleaning = st.sidebar.checkbox("🧹 Clean Missing Values", value=True)
    drop_duplicates = st.sidebar.checkbox("🧹 Remove Duplicates", value=True)

    # Clean data
    df_cleaned, missing_summary = clean_missing_values(df, cont_columns, cat_columns) if apply_cleaning else (df, [])
    df_cleaned, num_duplicates = remove_duplicates(df_cleaned) if drop_duplicates else (df_cleaned, df_cleaned.duplicated().sum())
    
    df_used = df_cleaned
    
    # Create Tabs
    tabs = st.tabs(["📁 Overview", "📈 Visualizations", "📊 Feature Analysis", "📉 Relationships"])

    with tabs[0]:
        overview.render(df_used, cont_columns, cat_columns, missing_summary, num_duplicates)

    with tabs[1]:
        visualization.render(df_used, cat_columns)

    with tabs[2]:
        feature.render(df_used, cont_columns)

    with tabs[3]:
        relationship.render(df_used, cont_columns, cat_columns)

else:
    st.warning("📂 Please upload a CSV file to begin.")
