# Clean column names
''' Captures all column names in DataFrame + Does following actions:
1. Strip whitespace (both left/right side of string)
2. Convert column names to all lowercase
3. Locates regex pattern specified (replaces any char that is NOT a letter or number with an underscore)
4. str.strip('_') removes any underscore characters at start/ end of string 
(https://www.w3schools.com/python/ref_string_strip.asp)
'''
def clean_column_names(df):
    df.columns = (
        df.columns.str.strip()
                  .str.lower()
                  .str.replace(r'[^a-z0-9]+', '_', regex=True)
                  .str.strip('_')
    )
    return df