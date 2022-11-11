#Import modules
import os
import csv

#Path to collect data
election_data_csv = os.path.join('Resources', 'election_data.csv')

#Variables
total_votes = 0
charles_votes = 0
diana_votes = 0
raymon_votes = 0
#Pull the data from the CSV
with open('election_data.csv') as elections:
   csvreader = csv.reader(elections,delimiter= ",")
   print(csvreader)
   header = next(csvreader)

   for row in csvreader:
    
    total_votes +=1
    if row[2] == "Charles Casper Stockham":
        charles_votes +=1
    elif row[2] == "Diana DeGette":
        diana_votes +=1
    elif row[2] == "Raymon Anthony Doane":
        raymon_votes +=1
candidates = ["Charles Casper Stockham", "Diana DeGette", "Raymon Anthony Doane"]
votes = [charles_votes, diana_votes, raymon_votes]
#Count the votes
dict_candidates_votes = dict(zip(candidates, votes))
key_winner = max(dict_candidates_votes, key=dict_candidates_votes.get)
#Percentages
charles_perc = (charles_votes/total_votes)*100
diana_perc = (diana_votes/total_votes)*100
raymon_perc = (raymon_votes/total_votes)*100
#Print statements
print(f"Election Results")
print(f"-------------------------")
print(f"Total Votes: {total_votes}")
print(f"-------------------------")
print(f"Charles Casper Stockham: {charles_perc:.3f}%({charles_votes})")
print(f"Diana DeGette: {diana_perc:.3f}%({diana_votes})")
print(f"Raymon Anthony Doane: {raymon_perc:.3f}%({raymon_votes})")
print(f"-------------------------")
print(f"Winner: {key_winner}")
print(f"-------------------------")

#txt file
import sys
file = open('PyPoll_Analysis.txt', 'a')
sys.stdout = file
print(f"Election Results")
print(f"-------------------------")
print(f"Total Votes: {total_votes}")
print(f"-------------------------")
print(f"Charles Casper Stockham: {charles_perc:.3f}%({charles_votes})")
print(f"Diana DeGette: {diana_perc:.3f}%({diana_votes})")
print(f"Raymon Anthony Doane: {raymon_perc:.3f}%({raymon_votes})")
print(f"-------------------------")
print(f"Winner: {key_winner}")
print(f"-------------------------")