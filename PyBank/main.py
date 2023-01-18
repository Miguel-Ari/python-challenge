# Import the os and csv modules
import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')
text_path = "Analysis/output.txt"

# Lists to store data
Date = []
Profit_Losses = []
PL_Change = []

# Initial values
Total_Months = 0
Total = 0
Max_Change = 0
Min_Change = 0

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    csv_header = next(csvreader)

    for row in csvreader:        
        Date.append(row[0])        
        Profit_Losses.append(row[1])
        Total_Months += 1
        Total += int(row[1])
    
    Change_Previous = int(Profit_Losses[0])

    for n in range(1, len(Profit_Losses)):
        Change = int(Profit_Losses[n]) - Change_Previous
        Change_Previous = int(Profit_Losses[n])
        PL_Change.append(Change)

    for n in range(len(PL_Change)):
        if int(PL_Change[n]) > Max_Change:
            Max_Change = int(PL_Change[n])
            Date_Max_Change = Date[n+1]
        if int(PL_Change[n]) < Min_Change:
            Min_Change = int(PL_Change[n])
            Date_Min_Change = Date[n+1]

Average_Change = format((sum(PL_Change) / len(PL_Change)), ".2f")

# Print results to Terminal
print(f'Total Months: {Total_Months}')
print(f'Total: ${Total}')
print(f'Average Change: ${Average_Change}')
print(f'Greatest Increase in Profits: {Date_Max_Change} (${Max_Change})')
print(f'Greatest Decrease in Profits: {Date_Min_Change} (${Min_Change})')

# Export text file with results
with open(text_path, 'w') as file:
    file.write('Financial Analysis\n\n')
    file.write('-----------------------------------------------\n\n')
    file.write('Total Months: ' + str(Total_Months) + '\n')
    file.write('Total: $' + str(Total) + '\n')
    file.write('Average Change: $' + str(Average_Change) + '\n')
    file.write('Greatest Increase in Profits: ' + str(Date_Max_Change) + ' $' + '(' + str(Max_Change) + ')' + '\n')
    file.write('Greatest Decrease in Profits: ' + str(Date_Min_Change) + ' $' + '(' + str(Min_Change) + ')' + '\n')