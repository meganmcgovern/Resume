#Import dependecies

import os
import csv


#Create lists

total_months = []
total_profit = []
profit_change = []

#Import file
csvpath = os.path.join('budget_data.csv')

#Read file into Python
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #Skip Header
    csv_header = next(csvreader)

    #go through rows in file
    for row in csvreader:

        #Add the months and rev to lists
        total_months.append(row[0])
        total_profit.append(int(row[1]))

    #go through rows to find monthly change
    for i in range(len(total_profit)-1):

        #Get difference in months and add it to monthly profit change
        profit_change.append(total_profit[i+1]-total_profit[i])

max_increase = max(profit_change)
max_decrease = min(profit_change)

max_month_increase = profit_change.index(max(profit_change)) + 1
max_month_decrease = profit_change.index(min(profit_change)) + 1


#Print all data

print("Financial Analysis")
print("--------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total Profit: ${sum(total_profit)}")
print(f"Average Change: ${round(sum(profit_change)/len(profit_change),2)}")
print(f"Greatest Profit Increase: {total_months[max_month_increase]} $({(str(max_increase))})")
print(f"Greatest Profit Decrease: {total_months[max_month_decrease]} $({(str(max_decrease))})")

#Create output file

output_path = os.path.join("new_py_bank_final2.txt")

with open(output_path, 'w', newline='') as txtfile:

#Write data to new file
    txtfile.write("Financial Analysis")
    txtfile.write("\n")
    txtfile.write("------------")
    txtfile.write("\n")
    txtfile.write(f"Total Months: {len(total_months)}")
    txtfile.write("\n")
    txtfile.write(f"Average Change: ${round(sum(profit_change)/len(profit_change),2)}")
    txtfile.write("\n")
    txtfile.write(f"Greatest Profit Increase: {total_months[max_month_increase]} $({(str(max_increase))})")
    txtfile.write("\n")
    txtfile.write(f"Greatest Profit Decrease: {total_months[max_month_decrease]} $({(str(max_decrease))})")

