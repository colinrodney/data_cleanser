# Import required packages/ libraries/ frameworks from requirements.txt
import pandas as pd
import os
import re

# Load Data ((ORIGINAL FILE)
def load_file(file_path):
    ext = os.path.splitext(file_path)[-1].lower() # converts filepath extension to lowercase
    # Handle .csv files
    if ext == '.csv':
        return pd.read_csv(file_path)

    # Handle excel spreadsheet files
    elif ext in ['.xls', '.xlsx']:
        return pd.read_excel(file_path)
    
    # All other files
    else:
        raise ValueError("Unsupported file type")

# file = load_file(r"example_import.csv") #THIS IS THE ORIGINAL DATAFRAME!
file = load_file(r'C:\Users\Cessn\OneDrive\Desktop\data_cleanser\example_import.csv')
# print(file)


# todo - Create pandas DataFram from file on filePath
"""
pd.read_csv expects a file path as its argument - above line of code will not work
because it is being passed a DataFrame/ Series object created by load file method and saved
to variable named 'file'

"""
# df = pd.read_csv(file) > WILL NOT WORK - Yields TypeError: argument of type 'method' is not iterable


# READ IN ORIGIANL FILE - THIS WORKS
df = pd.read_csv(r'C:\Users\Cessn\OneDrive\Desktop\data_cleanser\example_import.csv')
# print(df)



# ACTIONS BEFORE WRITING MODIFIED FILE

# Clean column names
def clean_column_names(df):
    df.columns = (
        df.columns.str.strip()
                  .str.lower()
                  .str.replace(r'[^a-z0-9]+', '_', regex=True)
                  .str.strip('_')
    )
    return df

updated_file = clean_column_names(df)
# print(clean_col_names)


# Convert dtae/time + email to strings
def convertToString(df):
    df['join_date'] = df['join_date'].astype(str)
    df["Email"] = df["Email"].astype(str) # convert all emaill addresses to strings
    return df
updated_file = convertToString(df)

# STRIP LEAD / TRAILING WHITESPACE
# Strip leading/trailing whitespace and fix casing
def normalize_strings(df):
    for col in df.select_dtypes(include='object'):
        df[col] = df[col].astype(str).str.strip()
    return df
updated_file = normalize_strings(df)


# TESTING

# WRITE info stored in variable updated_file as output via df.to_csv() method
df.to_csv("modified_csv1.csv") # DONE/ WORKING

# Read in modified CSV
modified_file = load_file(r'C:\Users\Cessn\OneDrive\Desktop\data_cleanser\modified_csv1.csv')
# print(modified_file)



 # ACTIONS AFTER MODIFIED FILE HAS BEEN WRITTEN:

# Remove blank rows & duplicate rows
# def remove_blanks_and_duplicates(df):
#     df.dropna(how='all', inplace=True)
#     df.drop_duplicates(inplace=True)
#     return df

# cleaned_blanks_and_dupes = remove_blanks_and_duplicates(df)
# print("'\n", cleaned_blanks_and_dupes)



# Normalize Dates

# def format_dates(df):
#     for col in df.columns:
#         # if df[col].dtype == 'float64' or df[col].dtype == 'int64':
#         #     df[col].fillna(df[col].median(), inplace=True)
#         # else:
#         #     df[col].fillna("MISSING", inplace=True)
#     # return df
#         print(col) # gets column name
#         #print(df[col]) # CLOSER
# format_dates(df)





# Test this - ITERATE OVER DATAFRAME
def testMe(df):
    for index, row in df.iterrows():
        # print(f"row_index: {index}, column: {index['Name']}")
        # print(df.loc[index]) # prints each row of dataFrame
        # print(row)
        #print(df.loc[:, 'join_date'])# gets single column
        # print(row['name']) - THIS WORKS (ABOVE LINE ALSO WORKS TO PRINT VALUES OF NAME COLUMN FROM ALL ROWS IN DF)
        x = df['email']
        print(x)
testMe(modified_file)




