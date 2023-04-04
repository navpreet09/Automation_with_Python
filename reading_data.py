# import dependencies
import csv
import os

# Assign a variable to load a file from a path.
file_to_load= "Resources/election_results.csv"
# Assign a variable to save the file to a path.
file_to_save= "analysis/analysis.txt"

# Open the election results and read the file.
with open(file_to_load) as election_data:
# Read the file object with the reader function.
    file_reader= csv.reader(election_data)


# skipping the first row/header row
    header_row= next(file_reader)
# Print the header row.
    print(header_row)

# Print each row in the CSV file.
    for item in file_reader:
        print(item)
   