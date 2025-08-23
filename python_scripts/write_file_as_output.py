# WRITE CLEANSED FILE AS OUTPUT TO SPECIFIED PATH 
''' note: cleansed file represented as df'''

def output_file(df):
    # cleansed_file.to_csv("concert_tours_by_women_TEST.csv")- DO NOT DELETE!
    df.to_csv(r"C:\Users\Cessn\OneDrive\Desktop\sample_datasets\concert_tours_by_women\concert_tours_by_women_CLEANSED.csv")

print("Cleaned data saved!")

