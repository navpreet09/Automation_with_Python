# import dependencies
import csv
import os

file_to_load= "Resources/test.csv"
file_to_save= "analysis/analysis.txt"

with open(file_to_load) as any:
    file_reader= csv.reader(any)
    header_row= next(file_reader)
    # print(header_row)
    for item in file_reader:
        print(item)
   