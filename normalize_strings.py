# remove all non-digit chars > df[col] = df[col].str.replace(r'\W', '', regex=True)

# # Strip leading/trailing whitespace and fix casing
def normalize_strings(df):

    '''Note: df.select_dtypes returns a subset of columns
    in DataFrame based on column data type (dtype)
    SOURCE: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.select_dtypes.html'''

    for col in df.select_dtypes(include='object'):
        df[col] = df[col].astype(str).str.strip()

        # regex pattern removes ANY characters that are not letters and/or numbers
        # works to remove replacement character (black diamond w/ white question mark in excel)
        df[col] = df[col].str.replace(r'[^a-zA-Z0-9]', '', regex=True)
    return df