import streamlit as st
import plotly.express as px

def render(df, cont_columns):
    st.header("Analyze Features")
    feature = st.selectbox("Select a Feature", df.columns)
    st.write(df[feature].describe())

    if feature in cont_columns:
        fig = px.histogram(df, x=feature, nbins=30, color_discrete_sequence=['#FF5733', '#33FF57', '#3357FF'])
    else:
        value_counts = df[feature].value_counts().reset_index()
        value_counts.columns = [feature, 'Count']
        fig = px.bar(value_counts, x=feature, y='Count', color_discrete_sequence=px.colors.qualitative.Bold)

    st.plotly_chart(fig, use_container_width=True, key=f"{feature}_bar")
