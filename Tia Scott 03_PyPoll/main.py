import pandas as pd
import os
import csv

#CSV Path
ELECTION_CSV = os.path.join ("Resources", "election_data.csv")
OUTPUT_PATH = os.path.join("Analysis", "analysis.txt")

#List
total_votes = 0
candidate_list= []
votes_for_candidate = {}
winnercount = 0
results = {}

#Read csv
with open(ELECTION_CSV) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #skip the header row
    header = next(csvreader)

    for row in csvreader:
        #add voter id
        votes = str(row[0])

        #add candidate
        candidate_name = row[2]

        #total number of votes cast
        total_votes += 1

        #tie candidates to thier votes, if you find another candidate not listed append and start at 0
        if candidate_name not in candidate_list:
            candidate_list.append(candidate_name)
            votes_for_candidate[candidate_name] = 0
        
        votes_for_candidate[candidate_name] += 1

    #calculate vote, percentage and winner by looping through candidates
    for candidate in votes_for_candidate:
        candidate_votes = votes_for_candidate.get(candidate)
        candidate_percentage = round((candidate_votes/total_votes)*100, 3)
        results[candidate] = {'Percentage': str(candidate_percentage)+"%", 'Votes': candidate_votes}
        
        if candidate_votes > winnercount:
            winnercount = candidate_votes
            winning_candidate = candidate

# Store the results and format for txt/terminal 
output = [
"Election Results\n-----------------------",
"Total Votes: "+str(total_votes),
"-----------------------",
candidate_list[0]+": "+results[candidate_list[0]]['Percentage']+" ("+str(results[candidate_list[0]]['Votes'])+")",
candidate_list[1]+": "+results[candidate_list[1]]['Percentage']+" ("+str(results[candidate_list[1]]['Votes'])+")",
candidate_list[2]+": "+results[candidate_list[2]]['Percentage']+" ("+str(results[candidate_list[2]]['Votes'])+")",
"-----------------------",
"Winner: "+winning_candidate,
"-----------------------"
]
#writing to txt 
with open(OUTPUT_PATH, 'w') as output_file:
    #tell the output to end a line at the end of the line
    for line in output:
        output_file.write(line + "\n")

for terminal in output:
    print(terminal)
