# Import the os and csv modules
import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')
text_path = "Analysis/output.txt"

# Lists to store data
Ballot_ID = []
County = []
Candidate = []
Candidate_Unique = []

# Initial Values
Total_Votes = 0
Winner_Count = 0

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    csv_header = next(csvreader)    

    for row in csvreader:
        Total_Votes += 1
        Ballot_ID.append(row[0])
        County.append(row[1])
        Candidate.append(row[2])

    for n in Candidate:
        if n not in Candidate_Unique:
            Candidate_Unique.append(n)

# Determine count and percentage for each candidate
Candidate_1_Count = Candidate.count(Candidate_Unique[0])
Candidate_1_Percentage = format((int(Candidate_1_Count) / Total_Votes) * 100, ".3f")

Candidate_2_Count = Candidate.count(Candidate_Unique[1])
Candidate_2_Percentage = format((int(Candidate_2_Count) / Total_Votes) * 100, ".3f")

Candidate_3_Count = Candidate.count(Candidate_Unique[2])
Candidate_3_Percentage = format((int(Candidate_3_Count) / Total_Votes) * 100, ".3f")

Candidate_Count = [Candidate_1_Count, Candidate_2_Count, Candidate_3_Count]

# Determine the winner
for n in range(len(Candidate_Count)):
    if int(Candidate_Count[n]) > Winner_Count:
        Winner = Candidate_Unique[n]
        Winner_Count = int(Candidate_Count[n])

# Print results to Terminal
print(f'Total Votes: {Total_Votes}')
print(f'{Candidate_Unique[0]}: {Candidate_1_Percentage}% ({Candidate_1_Count})')
print(f'{Candidate_Unique[1]}: {Candidate_2_Percentage}% ({Candidate_2_Count})')
print(f'{Candidate_Unique[2]}: {Candidate_3_Percentage}% ({Candidate_3_Count})')
print(f'Winner: {Winner}')

# Export text file with results
with open(text_path, 'w') as file:
    file.write('Election Results\n\n')
    file.write('-----------------------------------------------\n\n')
    file.write('Total Votes: ' + str(Total_Votes) + '\n\n')
    file.write('-----------------------------------------------\n\n')
    file.write(str(Candidate_Unique[0]) + ': ' + str(Candidate_1_Percentage) + '% ' + '(' + str(Candidate_1_Count) + ')' + '\n')
    file.write(str(Candidate_Unique[1]) + ': ' + str(Candidate_2_Percentage) + '% ' + '(' + str(Candidate_2_Count) + ')' + '\n')
    file.write(str(Candidate_Unique[2]) + ': ' + str(Candidate_3_Percentage) + '% ' + '(' + str(Candidate_3_Count) + ')' + '\n\n')
    file.write('-----------------------------------------------\n\n')
    file.write('Winner: ' + str(Winner) + '\n\n')
    file.write('-----------------------------------------------\n')