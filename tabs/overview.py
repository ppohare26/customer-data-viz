import streamlit as st
from util.helpers import create_sales_funnel

def render(df, cont_columns, cat_columns, missing_summary, num_duplicates):
    st.header("Dataset Overview")
    st.dataframe(df.head())
    st.markdown(f"**Shape:** {df.shape[0]} rows × {df.shape[1]} columns")
    st.markdown(f"**Missing Values:** {df.isnull().sum().sum()}")
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

    st.subheader("Sales Funnel")
    funnel_col = st.selectbox("Select a Column for Sales Funnel", cat_columns, key="overview_funnel_selector")
    if funnel_col:
        funnel_fig = create_sales_funnel(df, funnel_col)
        st.plotly_chart(funnel_fig, use_container_width=True, key="overview_funnel_chart")
