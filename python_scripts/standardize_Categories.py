# STANDARDIZE CATEGORIES

# Standardize Dates - Work ONLY w/ any year/date/month or date/ time columns in dataset
def standardizeCategories(df):
    # Dictionary of product keys and replacement values
    products_Dict = {
        # "PRODUCT_NAME":, :"STANDARDIZED REPLACEMENT TEXT"
        "28in4Kgamingmonitor": "Monitor: Gaming-28 in - 4K",
        "28inches4Kgamingmonitor": "Monitor: Gaming-28 in - 4K",
        "Acer Nitro V Gaming Laptop": "Computer: Laptop",
    }

    for col in df.select_dtypes(include="object"):
        if "PRODUCT_NAME" in df.columns:
            # df["PRODUCT_NAME_CLEANSED"]= df["PRODUCT_NAME_CLEANSED"].replace({"27in4Kgamingmonitor": "Monitor: Gaming-28 in - 4K",})
            
            # df = df.replace({"27in4Kgamingmonitor": "Monitor: Gaming-28 in - 4K",}) - THIS WORKS ON ENTIRE DATAFRAME NOT JUST SPECIFIC COLUMNS
            df["PRODUCT_NAME_CLEANSED"]= df["PRODUCT_NAME_CLEANSED"].replace({"NintendoSwitch": "Gaming Console: Nintendo Switch",
                                                                             "SonyPlayStation5Bundle": "Bundle: Sony Playstation 5",})

            """ NOTES: non-dictionary like objects to replace multiple string values within a DataFrame OR Series will not work 
            in future releases of Pandas
            
            Suggested to pass dictionary object direct to .replace() method for multiple replacements
            DO NOT reference a previously created dictionary as shown w/ products_Dict as this may work now , but not in future Pandas
            updates!"""
            
            # return df.loc[:, "PRODUCT_NAME"]
            
        # return False
        return df


# Call Function
cleansed_file = standardizeCategories(df)
print(cleansed_file)