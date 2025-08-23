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
df = pd.read_csv(r'C:\Users\Cessn\OneDrive\Desktop\sample_datasets\concert_tours_by_women\concert_tours_by_women_ORIGINAL.csv')
print("FILE READ: \n\n ", df.info())

# file = load_file(r"example_import.csv")
# THIS WORKS BUT MIGHT BE REDUNDANT
file_toBe_cleansed = load_file(r'C:\Users\Cessn\OneDrive\Desktop\sample_datasets\concert_tours_by_women\concert_tours_by_women_ORIGINAL.csv')
print("FILE LOADED: \n\n ", file_toBe_cleansed)

# Will this work > cleansed_file = df?
# print(file)