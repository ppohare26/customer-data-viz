def clean_missing_values(df, cont_columns, cat_columns):
    #Replace missing values: mean for continuous, mode for categorical.
    df_cleaned = df.copy()
    summary = []

    for col in cont_columns:
        if df_cleaned[col].isnull().sum() > 0:
            df_cleaned[col].fillna(df_cleaned[col].mean(), inplace=True)
            summary.append(f"🔹 '{col}' (continuous) → filled with mean")

    for col in cat_columns:
        if df_cleaned[col].isnull().sum() > 0:
            df_cleaned[col].fillna(df_cleaned[col].mode()[0], inplace=True)
            summary.append(f"🔸 '{col}' (categorical) → filled with mode")

    return df_cleaned, summary

def remove_duplicates(df):
    #Remove duplicate rows and return number removed."""
    num_duplicates = df.duplicated().sum()
    df_cleaned = df.drop_duplicates()
    return df_cleaned, num_duplicates
