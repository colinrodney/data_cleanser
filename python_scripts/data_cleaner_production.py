import load_data
import clean_column_names
import write_file_as_output

file_toBe_cleansed = load_data.load_file(r'C:\Users\Cessn\OneDrive\Desktop\sample_datasets\concert_tours_by_women\concert_tours_by_women_ORIGINAL.csv')
print("FILE LOADED: \n\n ", file_toBe_cleansed, "\n")

cleansed_file = clean_column_names.clean_column_names(file_toBe_cleansed)
print(cleansed_file)

write_file_as_output.output_file(cleansed_file)


