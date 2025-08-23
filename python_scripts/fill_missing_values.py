 #Import numpy 
"""In som cases fillna() will not fill NaN values for several reasons:
1. 
NaN is not an actual NaN value - fillna() specifically targets numpy.nan (ints/ floats data types?)
or None (object data types)

If the "missing / NaN" values are represented as empty strings (" "), custom strings ("NA"),
or any other NON-NUMERIC PLACEHOLDERS fillna() will NOT recognize them and hence will NOT replace
them

SOLUTION:
Convert non-numeric placeholders to np.nan using the replace() before applying 
fillna().

CONSIDER running above fix as standard procedure on datasets especially
if columns of type "object" have values that appear to be numbers alongside
NaN values.

"""
import numpy as np
# Function for filling / handling missing values within dataset

# Handle missing values (customize as needed) - MORE TESTING REQUIRED
def fill_missing(df):
    for col in df.columns:
        # Column data type is either float OR integer
        if df[col].dtype == 'float64' or df[col].dtype == 'int64':
            df[col].fillna(df[col].median(), inplace=True)
        
        # Column data type is object (text/ numbers represented as text) and ALL OTHER data types
        else:
            df[col] = df[col].replace('nan', np.nan)
            # df[col].fillna("MISSING", inplace=True) > use this for worded text
            # df[col].fillna("", inplace=True) > use this for worded text
            df[col].fillna(0, inplace=True) # > use this for NUMBERS appearing as text
    return df