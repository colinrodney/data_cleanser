import load_data
import clean_column_names
import write_file_as_output
import normalize_strings

file_toBe_cleansed = load_data.load_file(r'C:\Users\Cessn\OneDrive\Desktop\sample_datasets\concert_tours_by_women\concert_tours_by_women_ORIGINAL.csv')
print("FILE LOADED: \n\n ", file_toBe_cleansed, "\n")

cleansed_file = clean_column_names.clean_column_names(file_toBe_cleansed)
print("CLEANSED FILE: \n" ,cleansed_file, "\n")

cleansed_file = normalize_strings.normalize_strings(file_toBe_cleansed)
print("CLEANSED FILE w/ strings normalized: \n" ,cleansed_file ,"\n")

write_file_as_output.output_file(cleansed_file)


