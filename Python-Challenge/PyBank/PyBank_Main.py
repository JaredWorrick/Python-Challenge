#Import modules
import os
import csv

# Path to collect data 
budget_data_csv = os.path.join('Resources', 'budget_data.csv')
    
#Variables
total_months = []
total_profits = []
mprofit_change = []

with open('budget_data.csv') as csvfile:  
    csvreader = csv.reader(csvfile,delimiter= ',')
    print(csvreader)
    header = next(csvreader)

    for row in csvreader:

        total_months.append(row[0])
        total_profits.append(int(row[1]))
    
    for i in range(len(total_profits)-1):
        mprofit_change.append(total_profits[i+ 1]- total_profits[i])
#Max and min of the monthly profits
miv = max(mprofit_change)
mdv = min(mprofit_change)
#Index max and min to correlate to the proper months w/ months list
mim = mprofit_change.index(max(mprofit_change)) + 1
mdm = mprofit_change.index(min(mprofit_change)) + 1 
#Print statements
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(total_profits)}")
print(f"Average Change: ${round(sum(mprofit_change)/len(mprofit_change),2)}")
print(f"Greatest Increase in Profits: {total_months[mim]} (${(str(miv))})")
print(f"Greatest Decrease in Profits: {total_months[mdm]} (${(str(mdv))})")

#txt file
import sys
file = open('PyBank_Analysis.txt', 'a')
sys.stdout = file
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(total_profits)}")
print(f"Average Change: ${round(sum(mprofit_change)/len(mprofit_change),2)}")
print(f"Greatest Increase in Profits: {total_months[mim]} (${(str(miv))})")
print(f"Greatest Decrease in Profits: {total_months[mdm]} (${(str(mdv))})")
