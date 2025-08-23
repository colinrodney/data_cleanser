# Function for filling / handling missing values within dataset

# Handle missing values (customize as needed) - MORE TESTING REQUIRED
def fill_missing(df):
    for col in df.columns:
        if df[col].dtype == 'float64' or df[col].dtype == 'int64':
            df[col].fillna(df[col].median(), inplace=True)
        else:
            df[col].fillna("MISSING", inplace=True)
    return df