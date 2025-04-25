import streamlit as st
import plotly.express as px

def render(df, cont_columns, cat_columns):
    st.header("Explore Relationships Between Features")

    if len(cont_columns) < 2:
        st.warning("Need at least two continuous columns to plot relationships.")
        return

    x_axis = st.selectbox("X Axis", cont_columns)
    y_axis = st.selectbox("Y Axis", cont_columns, index=1)
    color = st.selectbox("Color By (optional)", [None] + cat_columns)

    fig = px.scatter(df, x=x_axis, y=y_axis, color=color)
    st.plotly_chart(fig, use_container_width=True)
