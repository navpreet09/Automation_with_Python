# import dependencies
import csv
import os

# Assign a variable to load a file from a path.
file_to_load= "Resources/election_results.csv"
# Assign a variable to save the file to a path.
file_to_save= "analysis/writing_data.txt"

# Initialize a total vote counter
total_votes=0
# Declaring an empty list
candidate_option=[]
candidate_votes={}
candidate_percentage={}
# Open the election results and read the file.
with open(file_to_load) as election_data:
# Read the file object with the reader function.
    file_reader= csv.reader(election_data)

# skipping the first row/header row
    header_row= next(file_reader)
# reading csv file by skipping header
    for row in file_reader:
        candidate_name= row[2]
        if candidate_name not in candidate_option:
            candidate_option.append(candidate_name)
            candidate_votes[candidate_name]=0
        candidate_votes[candidate_name]+=1
        total_votes+=1
winner = ""
winning_vote_count=0
winning_percentage=0

for item in candidate_votes:
    print(f"\n{item}: {candidate_votes[item]/total_votes*100:.2f}% ({candidate_votes[item]:,})\n")
    if candidate_votes[item]> winning_vote_count:
        winning_vote_count= candidate_votes[item]
        winner= item
    winning_percentage= winning_vote_count/total_votes*100
print('--------------------------------------\n')
print(f"Winner: {winner}")
print(f'Winning Vote Count: {winning_vote_count:,}')
print(f'Winning Percentage: {winning_percentage:.2f}%\n')
print('---------------------------------------')  
        
    