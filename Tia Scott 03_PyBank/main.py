import pandas as pd
import os
import csv

#CSV Path
BUDGET_CSV_PATH = os.path.join("Resources", "budget_data.csv")
OUTPUT_PATH = os.path.join("Analysis", "analysis.txt")

#List 
total_months = 0
total_pl = 0
previous_pl = 0
sum_of_chg_pl = 0
change_in_pl = 0
greatest_increase = {"date": "", "amount": 0}
greatest_decrease = {"date": "", "amount": 0}
is_first_month = True

#Read CSV
with open(BUDGET_CSV_PATH) as csvfile:
    csvreader = csv.reader(csvfile)
    #Store the header as a variable and skip the first row
    header = next(csvreader)

    for row in csvreader:
        total_months += 1
        date = row[0]

        #pl total
        current_pl = int(row[1])
        
        #total of pl
        total_pl += current_pl

        #if its the first month, skip calculation, otherwise, calculate
        if is_first_month:
            is_first_month = False
        else: 
            change_in_pl = current_pl - previous_pl
            sum_of_chg_pl += change_in_pl
        
        #prepare for next month
        previous_pl = current_pl

        #find greatest increase / decrease
        if change_in_pl > greatest_increase["amount"]:
            greatest_increase["date"] = date
            greatest_increase["amount"] = change_in_pl
        if change_in_pl < greatest_decrease["amount"]:
            greatest_decrease["date"] = date
            greatest_decrease["amount"] = change_in_pl

avg_change = sum_of_chg_pl / (total_months -1) 

#final output
output = "Financial Analysis\n"
output += "------------------------------\n"
output += f"Total Months: {total_months}\n"
output += f"Total: ${total_pl}\n"
output += f"Average Change ${round(avg_change, 2)}\n"
output += f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})\n"
output += f"Greatest Increase in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})\n"
                                                        
#writing to txt 
with open(OUTPUT_PATH, 'w') as output_file:
    output_file.write(output)

print(output)

      
