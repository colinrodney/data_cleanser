# Import required packages/ libraries/ frameworks from requirements.txt
import pandas as pd
import os
import re

# Load Data
def load_file(file_path):

    # converts filepath extension to lowercase
    ext = os.path.splitext(file_path)[-1].lower()

    # Handle .csv files
    """pd.read_csv expects a file path as its argument - above line of code will not work
    because it is being passed a DataFrame/ Series object created by load file method and saved
    to variable named 'file'
    """
    if ext == '.csv':
        return pd.read_csv(file_path)

    # Handle excel spreadsheet files
    elif ext in ['.xls', '.xlsx']:
        return pd.read_excel(file_path)
    
    # All other files
    else:
        raise ValueError("Unsupported file type")

# Create pandas DataFrame from ORIGINAL file on filePath
df = pd.read_csv(r'C:\Users\Cessn\OneDrive\Desktop\data_cleanser\concert_tours_by_women_TEST.csv')
print(df.info())

# file = load_file(r"example_import.csv")
# THIS WORKS BUT MIGHT BE REDUNDANT
file_toBe_cleansed = load_file(r'C:\Users\Cessn\OneDrive\Desktop\data_cleanser\concert_tours_by_women_TEST.csv')
# Will this work > cleansed_file = df?
# print(file)



# df = pd.read_csv(file) > WILL NOT WORK - Yields TypeError: argument of type 'method' is not iterable (DO NOT DELETE!)
# df.columns reference = https://www.geeksforgeeks.org/python/python-pandas-dataframe-columns/


# DATA CLEANSING FUNCTIONS

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
                  .str.replace(r'[^a-z0-9]+', '', regex=True)
                  .str.strip('_')
    )
    return df

# CALL FUNCTION
# cleansed_file = clean_column_names(df)
# print(clean_col_names)


# Remove blank rows & duplicate rows
def remove_blanks_and_duplicates(df):

    # https://www.w3schools.com/python/pandas/ref_df_dropna.asp
    # https://www.w3schools.com/python/pandas/pandas_ref_dataframe.asp
    df.dropna(how='all', inplace=True) 
    df.drop_duplicates(inplace=True)
    return df

# CALL FUNCTION
# cleansed_file = remove_blanks_and_duplicates(df)
# print("'\n", cleaned_blanks_and_dupes)


# # Strip leading/trailing whitespace and fix casing
def normalize_strings(df):

    '''Note: df.select_dtypes returns a subset of columns
    in DataFrame based on column data type (dtype)
    SOURCE: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.select_dtypes.html'''

    for col in df.select_dtypes(include='object'):
        df[col] = df[col].astype(str).str.strip()
        #df[col] = df[col].str.replace(r'\W', '', regex=True) # remove all non-digit chars

        # regex pattern removes any characters that are not letters and/or numbers
        # works to remove replacement character (black diamond w/ white question mark in excel)
        df[col] = df[col].str.replace(r'[^a-zA-Z0-9]', '', regex=True)
    return df

# CALL FUNCTION
# cleansed_file = normalize_strings(df)


# CALL FUNCTION
# cleansed_file = remove_dollarSign(df)



# # Handle missing values (customize as needed) - MORE TESTING REQUIRED
def fill_missing(df):
    for col in df.columns:
        if df[col].dtype == 'float64' or df[col].dtype == 'int64':
            df[col].fillna(df[col].median(), inplace=True)
        else:
            df[col].fillna("MISSING", inplace=True)
    return df

# CALL FUNCTION
# cleansed_file = fill_missing(df)

# Standardize Dates - Work ONLY w/ any year/date/month or date/ time columns in dataset
def normalizeDates(df):
    if  "years" in df.columns:
        print("Years COLUMN IN DF = True")
        # df["years"] = pd.to_datetime(df["years"]) #DO NOT DELETE
        #df["years"] = df["years"].dt.strftime('%Y'+'-'+'%Y') #DO NOT DELETE
        

        #SPLIT Years column in to year_start and year_end

        # df["years"] = df["years"].astype(str)
        
        # # print(df['years'].str.contains(r'((\d{4})(\d{4}))', regex=True))
        # # print(df['years'].str.replace(r'((\d{4})(\d{4}))', "testMe", regex=True)) - DO NOT DELETE
        # df['years'] = df['years'].str.replace(r'((\d{4})(\d{4}))', "someString", regex=True) #- DO NOT DELETE
        # # df['years'] = df['years'].re.sub(r'((\d{4})(\d{4}))', r'((\d{4}) (\d{4}))') #- DO NOT DELETE
            
        #return df

    # for col in df.select_dtypes(include="object"): # loop
    # #     #  print(col)
    # #     #  print(df.loc["year_s"])

                # Check if value matches regex pattern
        yearRegexPattern = re.compile(r'((\d{4})(\d{4}))')
        searchText = '20232024'

        # mo = matching object
        mo = yearRegexPattern.search(searchText)

        #capture matching objects groups
        x = mo.group(1)
        print("X is: ", type(x))
        y = mo.group(2)
        print("Y is: ", type(y))
        z = mo.group(3)
        print("Z s: ", type(z))

        # normalizedYearx = f"{x}"
        normalizedYeary = f"{y}"
        normalizedYearz= f"{z}"
        

    # # #     # #df[col] = df[col].str.replace(r'\W', '', regex=True) # remove all non-digit chars

    # # #     # # regex pattern removes any characters that are not letters and/or numbers
    # # #     # # works to remove replacement character (black diamond w/ white question mark in excel)
    # #         df[col] = df[col].str.replace(yearRegexPattern, normalizedYearx + normalizedYeary, regex=True)
            # return df

    #     #Regex pattern to be searched in string
    # unformattedDate = (r'((\d{4})(\d{4}))')
        
    # Compiles regular expression PATTERN to be tested/matched into regex object
    # this optimizes pattern for repeated use/ reusability
    #     yearRegexPattern = re.compile(r'((\d{4})(\d{4}))')

    #     # mo = matching object
    #     mo = yearRegexPattern.search('20232024')

    #     #capture matching objects groups
    #     x = mo.group(1)
    #     y = mo.group(2)

    #     normalizedYearx = f"{x}"
    #     normalizedYeary = f"{y}"
        

    # #     # #df[col] = df[col].str.replace(r'\W', '', regex=True) # remove all non-digit chars

    # #     # # regex pattern removes any characters that are not letters and/or numbers
    # #     # # works to remove replacement character (black diamond w/ white question mark in excel)
        df['years'] = df['years'].str.replace(yearRegexPattern, normalizedYeary+ normalizedYearz, regex=True)


        return df
cleansed_file = normalizeDates(df)
# print(cleansed_file)



   


# WRITE CLEANSED FILE AS OUTPUT
cleansed_file.to_csv("concert_tours_by_women_TEST_NEW.csv")
print(f"Cleaned data saved!")

# # Run full cleaning pipeline
# def clean_data(file_path, output_path):
#     df = load_file(file_path)
#     print(f"Loaded {len(df)} rows and {len(df.columns)} columns.")

#     df = clean_column_names(df)
#     df = remove_blanks_and_duplicates(df)
#     df = normalize_strings(df)
#     df = fill_missing(df)

#     df.to_csv(output_path, index=False)
#     print(f"Cleaned data saved to: {output_path}")


# # Example usage
# if __name__ == "__main__":
#     input_file = "example_input.csv"
#     output_file = "cleaned_output.csv"
#     clean_data(input_file, output_file)
