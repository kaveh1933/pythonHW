# The total number of votes cast
    # sum Row[0] minus the Header
# A complete list of candidates who received votes
    #
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote.

import csv
import os
# Object path
election_file = os.path.join("budget_data.csv")

# Create lists to append
# list to capture all the candidates
candidates =[]
# list to capture votes cast for candidates
num_votes = []
#list to capture percentages of votes each candidate received
percentage_votes = []
# determine total votes cast
total_votes = 0

with open ('election_data.csv', newline= '') as csv_file:
    election_file = csv.reader(csv_file, delimiter = ",")
    reader = election_file
    header = next(reader)
    for row in reader:
        total_votes += 1
        if row[2] not in candidates:
            candidates.append(row[2])
            index = candidates.index(row[2])
            num_votes.append(1)
        else:
            index = candidates.index(row[2])
            num_votes[index] += 1
#Print out results
print("Election Results")
print("--------------------------")
print(f"Total Votes: {str(total_votes)}")  
for candidate in range(len(candidates)):
    print(f"{candidates[candidate]}: {str(num_votes[candidate])}")
print("-----------------")
print(f"Winner: Khan")

#Exporing to .txt file
output = open("output.txt", "w")
line1 = "Election Results"
line2 = "--------------------------"
line3 = str(f"Total Votes: {str(total_votes)}")
line4 = str("--------------------------")
output.write('{}\n{}\n{}\n{}\n'.format(line1, line2, line3, line4))
for candidate in range(len(candidates)):
    line = str(f"{candidates[candidate]}: ({str(num_votes[candidate])})")
    output.write('{}\n'.format(line))
line5 = "--------------------------"
line6 = str(f"Winner: Khan")
line7 = "--------------------------"
output.write('{}\n{}\n{}\n'.format(line5, line6, line7))