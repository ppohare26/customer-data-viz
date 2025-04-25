import pandas as pd
import plotly.graph_objects as go

def find_cat_cont_columns(df):
    #Split columns into categorical and continuous based on data type and cardinality.
    cont_columns, cat_columns = [], []
    for col in df.columns:
        if df[col].dtype == object or len(df[col].unique()) <= 25:
            cat_columns.append(col)
        else:
            cont_columns.append(col)
    return cont_columns, cat_columns

def create_sales_funnel(df, stage_col):
    #Create a sales funnel chart from a categorical stage column.
    stage_counts = df[stage_col].value_counts().reset_index()
    stage_counts.columns = ['Stage', 'Count']
    fig = go.Figure(go.Funnel(
        y=stage_counts['Stage'],
        x=stage_counts['Count'],
        textinfo="value+percent initial+percent previous"
    ))
    return fig
