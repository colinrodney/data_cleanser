```python
# SMALL CHANGE - DISREGARD THIS CELL
```


```python
%pip install import-ipynb
%pip install openpyxl
%pip install xlrd

import import_ipynb
# import load_data
# import clean_column_names
# import write_file_as_output
# import normalize_strings
# import fill_missing_values
# import text_to_numeric
# import drop_columns
import pandas as pd
import os
import re
import numpy as np
from IPython.display import display

```

    Requirement already satisfied: import-ipynb in c:\users\cessn\miniconda3\lib\site-packages (0.2)
    Requirement already satisfied: IPython in c:\users\cessn\miniconda3\lib\site-packages (from import-ipynb) (9.2.0)
    Requirement already satisfied: nbformat in c:\users\cessn\miniconda3\lib\site-packages (from import-ipynb) (5.10.4)
    Requirement already satisfied: colorama in c:\users\cessn\miniconda3\lib\site-packages (from IPython->import-ipynb) (0.4.6)
    Requirement already satisfied: decorator in c:\users\cessn\miniconda3\lib\site-packages (from IPython->import-ipynb) (5.2.1)
    Requirement already satisfied: ipython-pygments-lexers in c:\users\cessn\miniconda3\lib\site-packages (from IPython->import-ipynb) (1.1.1)
    Requirement already satisfied: jedi>=0.16 in c:\users\cessn\miniconda3\lib\site-packages (from IPython->import-ipynb) (0.19.2)
    Requirement already satisfied: matplotlib-inline in c:\users\cessn\miniconda3\lib\site-packages (from IPython->import-ipynb) (0.1.7)
    Requirement already satisfied: prompt_toolkit<3.1.0,>=3.0.41 in c:\users\cessn\miniconda3\lib\site-packages (from IPython->import-ipynb) (3.0.51)
    Requirement already satisfied: pygments>=2.4.0 in c:\users\cessn\miniconda3\lib\site-packages (from IPython->import-ipynb) (2.19.1)
    Requirement already satisfied: stack_data in c:\users\cessn\miniconda3\lib\site-packages (from IPython->import-ipynb) (0.6.3)
    Requirement already satisfied: traitlets>=5.13.0 in c:\users\cessn\miniconda3\lib\site-packages (from IPython->import-ipynb) (5.14.3)
    Requirement already satisfied: fastjsonschema>=2.15 in c:\users\cessn\miniconda3\lib\site-packages (from nbformat->import-ipynb) (2.21.1)
    Requirement already satisfied: jsonschema>=2.6 in c:\users\cessn\miniconda3\lib\site-packages (from nbformat->import-ipynb) (4.23.0)
    Requirement already satisfied: jupyter-core!=5.0.*,>=4.12 in c:\users\cessn\miniconda3\lib\site-packages (from nbformat->import-ipynb) (5.7.2)
    Requirement already satisfied: parso<0.9.0,>=0.8.4 in c:\users\cessn\miniconda3\lib\site-packages (from jedi>=0.16->IPython->import-ipynb) (0.8.4)
    Requirement already satisfied: attrs>=22.2.0 in c:\users\cessn\miniconda3\lib\site-packages (from jsonschema>=2.6->nbformat->import-ipynb) (25.3.0)
    Requirement already satisfied: jsonschema-specifications>=2023.03.6 in c:\users\cessn\miniconda3\lib\site-packages (from jsonschema>=2.6->nbformat->import-ipynb) (2025.4.1)
    Requirement already satisfied: referencing>=0.28.4 in c:\users\cessn\miniconda3\lib\site-packages (from jsonschema>=2.6->nbformat->import-ipynb) (0.36.2)
    Requirement already satisfied: rpds-py>=0.7.1 in c:\users\cessn\miniconda3\lib\site-packages (from jsonschema>=2.6->nbformat->import-ipynb) (0.25.0)
    Requirement already satisfied: platformdirs>=2.5 in c:\users\cessn\miniconda3\lib\site-packages (from jupyter-core!=5.0.*,>=4.12->nbformat->import-ipynb) (4.3.7)
    Requirement already satisfied: pywin32>=300 in c:\users\cessn\miniconda3\lib\site-packages (from jupyter-core!=5.0.*,>=4.12->nbformat->import-ipynb) (310)
    Requirement already satisfied: wcwidth in c:\users\cessn\miniconda3\lib\site-packages (from prompt_toolkit<3.1.0,>=3.0.41->IPython->import-ipynb) (0.2.13)
    Requirement already satisfied: executing>=1.2.0 in c:\users\cessn\miniconda3\lib\site-packages (from stack_data->IPython->import-ipynb) (2.2.0)
    Requirement already satisfied: asttokens>=2.1.0 in c:\users\cessn\miniconda3\lib\site-packages (from stack_data->IPython->import-ipynb) (3.0.0)
    Requirement already satisfied: pure-eval in c:\users\cessn\miniconda3\lib\site-packages (from stack_data->IPython->import-ipynb) (0.2.3)
    Note: you may need to restart the kernel to use updated packages.
    Requirement already satisfied: openpyxl in c:\users\cessn\appdata\roaming\python\python313\site-packages (3.1.5)
    Requirement already satisfied: et-xmlfile in c:\users\cessn\appdata\roaming\python\python313\site-packages (from openpyxl) (2.0.0)
    Note: you may need to restart the kernel to use updated packages.
    Requirement already satisfied: xlrd in c:\users\cessn\miniconda3\lib\site-packages (2.0.2)
    Note: you may need to restart the kernel to use updated packages.
    


```python

```

# Data Cleansing Functions (THIS IS THE ACTUAL DATA CLEANER)


```python
# AUTOMATED DATA CLEANER

# Define input and output directories
input_folder = "raw_data"
output_folder = "cleaned_data"

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)


# DATA CLEANSING FUNCTIONS

# # SUMMARIZE DATA SET
def summarize_data(filename):
    duplicates = df_2.duplicated()
    num_duplicates = duplicates.sum()
    total_rows = len(df_2)
    percentage_duplicates = (num_duplicates / total_rows) * 100
    
    # x = os.listdir(input_folder)
    print(f"FILENAME: {filename}")
    
    print("DataFrame Information: '\n' ",)
    print(df_2.info(),"\n")
    print(f"Data Shape: (# of Rows, # of Columns): '\n' ", df_2.shape, "\n")
   
    # Show count of null values etc
    print("SUM OF NULL/ BLANK VALUES: '\n' ", df_2.isnull().sum(), "\n")

    with open(f"{filename}.txt", "a") as report_file:
      report_file.write(
          # f"test me" +'\n'
          # # f"Original DataFrame:\n{df}\n"
          # # f"Boolean Series indicating duplicates:'{duplicates}" + "\n\n"
    
          f"Pre-cleansing statistics: " + "\n"
          f"Number of duplicate rows: {num_duplicates}" +"\n"
          f"Total number of rows : {total_rows}" + "\n"
          # percentage_duplicates = (num_duplicates / total_rows) * 100
          f"Percentage of duplicate rows: {percentage_duplicates:.2f}%" + "\n"
          f"DATAFRAME INFO: {df_2.info}"
        
      )
      #open and read the file after the appending:
      with open(f"{filename}.txt") as report_file:
          print(report_file.read())


     
# NORMALIZE/ STANDARDIZE: COLUMN NAMES (ALL DATASETS)
# Clean column names
''' Captures all column names in DataFrame + Does following actions:
1. Strip whitespace (both left/right side of string)
2. Convert column names to all lowercase
3. Locates regex pattern specified (replaces any char that is NOT a letter or number with an underscore)
4. str.strip('_') removes any underscore characters at start/ end of string 
(https://www.w3schools.com/python/ref_string_strip.asp)
'''
def clean_column_names(df_2):
    df_2.columns = (
        df_2.columns.str.strip()
                  .str.lower()
                  .str.replace(r'[^a-z0-9]+', '_', regex=True)
                  # .str.strip('_')
    )
    return df_2



# NORMALIZE/ STANDARDIZE: EMAIL ADDRESSES (CRM DATASETS)
def cleanse_email_address(df_2):
    # df_2["email"].str.strip()
    # df_2.replace(r"[+AEA-]{1}", "@", regex=True)
    # return df_2
    df_2['email'] = df_2['email'].str.replace("+AEA-","@")
    # df_2['join_date'] = df_2['join_date'].str.replace("+AC0-","/") # STANDARDIZE DATES
    df_2['email']
    return df_2


def standardize_names(df_2):
    df_2['name'] = df_2['name'].str.lower()
    df_2['name'] = df_2['name'].str.title() # Capitalize first letter of each name
    return df_2


# FILL BLANKS/ NULLS
def fill_missing_values(df_2):
    df_2 = df_2.replace("nan", np.nan)
    # df_2["phone_number"] = df_2["phone_number"].replace("nan", np.nan)
    df_2["phone_number"] = df_2["phone_number"].fillna("NONE")
    df_2 = df_2.fillna("NONE_NEW")
    return df_2



# STANDARDIZE PHONE NUMBERS
phone_number_pattern = re.compile(r"[\+\s\(\)-.]")
def standardize_phone_numbers(df_2):

    # REMOVE ALL NON-DIGIT CHARS FROM PHONE NUMBERS
    df_2["phone_number"] = df_2["phone_number"].apply(lambda x: re.sub(r'[(),\s\.\-]', '', x))

    # REMOVE +1 FROM BEGINNING OF PHONE NUMBERS
    plus_one = r"^\+\d"
    plus_one_formatted = ""
    df_2["phone_number"] = df_2["phone_number"].apply(lambda x: re.sub(plus_one, plus_one_formatted, x))

    # INSERT HYPHENS INTO PHONE NUMBERS USING BACK REFERENCES IN FORMATTED / REPLACEMENT PATTERN
    search_pattern = r"(\d{3})(\d{3})(\d{4})"
    formatted_pattern = r"\1-\2-\3"
    df_2["phone_number"] = df_2["phone_number"].apply(lambda x: re.sub(search_pattern, formatted_pattern, x))

    return df_2


# STANDARDIZE CITY NAMES
def standardize_city_names(df_2):

    # TITLE CASE CITY NAMES (CAPITALIZE FIRST LETTER OF EACH CITY NAME)
    df_2["city"] = df_2["city"].apply(lambda x: re.sub(x, x.title(), x))
    return df_2
```


```python
# PROCESS EACH CSV IN FOLDER

for filename in os.listdir(input_folder):
    print("FILENAME:'\n'",filename)
    if filename.endswith(".csv"):
        file_path = os.path.join(input_folder, filename)
        print("FILEPATH: " '\n', file_path)
        try:
            df = pd.read_csv(file_path)
            df_2 = df.copy()

            # print("DATAFRAME BEFORE CLEANSING: '\n'")
            display(f"DATAFRAME BEFORE CLEANSING:", df_2)

            # GET INITIAL SUMMARY OF DATAFRAME
            summarize_data(filename)

            # # show_dirty_data()
            # print("DATASET PRE-CLEANSE: '\n' ")
            # df_2

            df_2 = clean_column_names(df_2)
            print(df_2.columns, "\n")
            
            df_2 = cleanse_email_address(df_2)
            print(df_2["email"], "\n")
            
            df_2 = standardize_names(df_2)
            print(df_2["name"], "\n")

            df_2 = fill_missing_values(df_2)
            # print(df_2["phone_number"], "\n")

            df_2 = standardize_phone_numbers(df_2)
            print(df_2["phone_number"], "\n")

            DF_2 = standardize_city_names(df_2)
            print(df_2["city"], "\n")
            
            output_path = os.path.join(output_folder, f"cleaned_{filename}")
            print("OUTPUT_PATH: " '\n', output_path)
            df_2.to_csv(output_path, index=False)

            display(f"DATAFRAME AFTER CLEANSING:", df_2)

            # # Report on data file:
            # with open(filename, "a") as report_file:
            #   report_file.write(
            #       # f"Original DataFrame:\n{df}\n"
            #         f"Boolean Series indicating duplicates:'{duplicates}" + "\n\n"
            
            #     f"Pre-cleansing statistics: " + "\n"
            #     f"Number of duplicate rows: {num_duplicates}" + "\n"
            #     f"Total number of rows : {total_rows}" + "\n"
            #     f"Percentage of duplicate rows: {percentage_duplicates:.2f}%" + "\n"
            #   )
            
            # #open and read the file after the appending:
            # with open("report_file.txt") as report_file:
            #   print(report_file.read())


            print(f"✅ Cleaned: {filename} → {output_path}")

        except Exception as e:
            print(f"❌ Failed to process {filename}: {e}")
```

    FILENAME:'
    ' messy_crm_dataset.csv
    FILEPATH: 
     raw_data\messy_crm_dataset.csv
    


    'DATAFRAME BEFORE CLEANSING:'



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>customer_id</th>
      <th>name</th>
      <th>email</th>
      <th>phone_number</th>
      <th>city</th>
      <th>registration_date</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>V9NI97D1</td>
      <td>Caitlin Braun</td>
      <td>caitlinbraun941@yahoo.com</td>
      <td>528-661-4506</td>
      <td>Robertsview</td>
      <td>2021-06-13</td>
    </tr>
    <tr>
      <th>1</th>
      <td>NNV7CWF1</td>
      <td>John Brown</td>
      <td>johnbrown577@yahoo.co</td>
      <td>485-2036208</td>
      <td>Combston</td>
      <td>2023-11-23</td>
    </tr>
    <tr>
      <th>2</th>
      <td>EOKPZD9O</td>
      <td>Barbara Walls</td>
      <td>barbarawalls@gmail.org</td>
      <td>541 570 3780</td>
      <td>New Mary</td>
      <td>2025-06-17</td>
    </tr>
    <tr>
      <th>3</th>
      <td>6WHZXW6T</td>
      <td>Lynn Coleman</td>
      <td>lynncoleman@yahoo.org</td>
      <td>(801) 750-9883</td>
      <td>Donnaburgh</td>
      <td>2024-01-30</td>
    </tr>
    <tr>
      <th>4</th>
      <td>RCES5GL5</td>
      <td>James Stevenson</td>
      <td>jamesstevenson@gmail.co</td>
      <td>(211)8584312</td>
      <td>North Morgan</td>
      <td>2022-12-07</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>495</th>
      <td>3PGQDUS8</td>
      <td>Jeffrey Jordan</td>
      <td>jeffreyjordan@gmail16.co</td>
      <td>+1 293 158 7271</td>
      <td>North Aprilfort</td>
      <td>2025-01-13</td>
    </tr>
    <tr>
      <th>496</th>
      <td>9SR0OI5O</td>
      <td>Jose Hanson</td>
      <td>josehanson898@hotmail10.us</td>
      <td>(867)6281917</td>
      <td>West Michael</td>
      <td>2023-12-21</td>
    </tr>
    <tr>
      <th>497</th>
      <td>FJORK5OJ</td>
      <td>Carlos Dean</td>
      <td>carlosdean@example.us</td>
      <td>136.343.5784</td>
      <td>east yvonnehaven</td>
      <td>2023-02-12</td>
    </tr>
    <tr>
      <th>498</th>
      <td>496H1X1O</td>
      <td>Jack White</td>
      <td>jackwhite@gmail.net</td>
      <td>(989) 954-9166</td>
      <td>south amanda</td>
      <td>2021-08-22</td>
    </tr>
    <tr>
      <th>499</th>
      <td>KD5IWG9I</td>
      <td>Hunter Robinson</td>
      <td>hunterrobinson@yahoo.co</td>
      <td>(912)5604540</td>
      <td>New Amandatown</td>
      <td>2022-08-12</td>
    </tr>
  </tbody>
</table>
<p>500 rows × 6 columns</p>
</div>


    FILENAME: messy_crm_dataset.csv
    DataFrame Information: '
    ' 
    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 500 entries, 0 to 499
    Data columns (total 6 columns):
     #   Column             Non-Null Count  Dtype 
    ---  ------             --------------  ----- 
     0   customer_id        500 non-null    object
     1   name               500 non-null    object
     2   email              475 non-null    object
     3   phone_number       482 non-null    object
     4   city               500 non-null    object
     5   registration_date  487 non-null    object
    dtypes: object(6)
    memory usage: 23.6+ KB
    None 
    
    Data Shape: (# of Rows, # of Columns): '
    '  (500, 6) 
    
    SUM OF NULL/ BLANK VALUES: '
    '  customer_id           0
    name                  0
    email                25
    phone_number         18
    city                  0
    registration_date    13
    dtype: int64 
    
    ❌ Failed to process messy_crm_dataset.csv: name 'x' is not defined
    FILENAME:'
    ' messy_crm_dataset_15000.csv
    FILEPATH: 
     raw_data\messy_crm_dataset_15000.csv
    


    'DATAFRAME BEFORE CLEANSING:'



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>customer_id</th>
      <th>name</th>
      <th>email</th>
      <th>phone_number</th>
      <th>city</th>
      <th>registration_date</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>3M0YEDY5</td>
      <td>Amber Bartlett</td>
      <td>amberbartlett@example.co</td>
      <td>(519) 438-7215</td>
      <td>West Kristin</td>
      <td>2020-11-27</td>
    </tr>
    <tr>
      <th>1</th>
      <td>6JD2QZKY</td>
      <td>Brian Robinson</td>
      <td>brianrobinson@hotmail11.net</td>
      <td>(886) 147-2230</td>
      <td>Estradaberg</td>
      <td>2023-05-07</td>
    </tr>
    <tr>
      <th>2</th>
      <td>9L07IA9E</td>
      <td>Bryce Li</td>
      <td>bryceli@yahoo.com</td>
      <td>642-1596202</td>
      <td>Lawrencefort</td>
      <td>2025-05-25</td>
    </tr>
    <tr>
      <th>3</th>
      <td>UK6MALLG</td>
      <td>Michael Kaiser</td>
      <td>michaelkaiser406@gmail.co</td>
      <td>520 828 6109</td>
      <td>East Collinville</td>
      <td>2021-11-21</td>
    </tr>
    <tr>
      <th>4</th>
      <td>3GOKY69M</td>
      <td>Donald Juarez</td>
      <td>donaldjuarez@gmail.us</td>
      <td>348-6125104</td>
      <td>New Michaelbury</td>
      <td>2024-08-04</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>14995</th>
      <td>O7J7QDLV</td>
      <td>Brian Fletcher</td>
      <td>brianfletcher@example1.co</td>
      <td>+1 782 915 2316</td>
      <td>Mcclurebury</td>
      <td>2024-03-20</td>
    </tr>
    <tr>
      <th>14996</th>
      <td>GB7DP26Z</td>
      <td>Kelly Hudson</td>
      <td>kellyhudson@outlook.org</td>
      <td>150.952.7357</td>
      <td>Lopezhaven</td>
      <td>2025-01-10</td>
    </tr>
    <tr>
      <th>14997</th>
      <td>WJ6RQIOA</td>
      <td>Thomas Vance</td>
      <td>thomasvance@hotmail.net</td>
      <td>518 468 8702</td>
      <td>Lake Emily</td>
      <td>2023-04-25</td>
    </tr>
    <tr>
      <th>14998</th>
      <td>4TAYRSDO</td>
      <td>Melvin Ortiz</td>
      <td>NaN</td>
      <td>(204)6745488</td>
      <td>South Matthewport</td>
      <td>2025-07-25</td>
    </tr>
    <tr>
      <th>14999</th>
      <td>LFA9OWA7</td>
      <td>Rhonda Cox</td>
      <td>rhondacox@outlook.net</td>
      <td>569 932 1509</td>
      <td>Marquezchester</td>
      <td>2025-08-08</td>
    </tr>
  </tbody>
</table>
<p>15000 rows × 6 columns</p>
</div>


    FILENAME: messy_crm_dataset_15000.csv
    DataFrame Information: '
    ' 
    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 15000 entries, 0 to 14999
    Data columns (total 6 columns):
     #   Column             Non-Null Count  Dtype 
    ---  ------             --------------  ----- 
     0   customer_id        15000 non-null  object
     1   name               15000 non-null  object
     2   email              14212 non-null  object
     3   phone_number       14583 non-null  object
     4   city               15000 non-null  object
     5   registration_date  14697 non-null  object
    dtypes: object(6)
    memory usage: 703.3+ KB
    None 
    
    Data Shape: (# of Rows, # of Columns): '
    '  (15000, 6) 
    
    SUM OF NULL/ BLANK VALUES: '
    '  customer_id            0
    name                   0
    email                788
    phone_number         417
    city                   0
    registration_date    303
    dtype: int64 
    
    ❌ Failed to process messy_crm_dataset_15000.csv: name 'x' is not defined
    


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```
