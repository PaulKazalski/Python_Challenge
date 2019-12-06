# This program executes the entire pyBank Requirements
#   (1) Read the .csv file
#   (2) Tally the total months
#   (3) Calculate net profits
#   (4) Calculate average change in profits
#   (5) Calculate the greatest increase and decrease in profts.
#   (6) Display the results in the terminal and a .txt file.

# VARIABLE DECLARATION
# Used for (1)
csvpath = " "
# Used for (2) through (5)
line_count = 0
# Used for (2)
previous_month = " "
present_month = " "
month_count = 0
# Used for (3)
profit = " "
monthly_profit = 0
total_profit = 0
# Used for (4)
first_profit = 0
last_profit = 0
average_change = 0
# Used for (5)
profit_change = 0
greatest_change = 0
greatest_date = " "
least_change = 0
least_date = " "
previous_profit = 0

# Step 2: Pull the data from the .csv file

import os
import csv
csvpath = os.path.join("C:/Users/paulk/Documents/python-challenge/PyBank/Resources/budget_data.csv")
#open the csv file
with open(csvpath, newline='') as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter = ",")

    # For each reader, define the line number, and assign 
    # the date and profit to a variable
    for row in csvreader:
        line_count += 1
        present_month = str(row[0])
        profit = row[1]
        # The top line is the header - no calculations here
        if line_count == 1:
            print(present_month)
        # The first line of values is slightly different than the others
        # The first profit is stored throughout the program
        # Profit change cannot be calculated yet.   
        elif line_count == 2:
            month_count += 1
            monthly_profit = int(profit)
            first_profit = int(profit)
            total_profit = total_profit + monthly_profit    
        else:
            monthly_profit = int(profit)
            total_profit = total_profit + monthly_profit
            month_count += 1
            previous_month = present_month
            profit_change = monthly_profit - previous_profit
            if profit_change > greatest_change:
                greatest_change = profit_change
                greatest_date = row[0]
            elif profit_change < least_change:
                least_change = profit_change   
                least_date = row[0] 
            previous_profit = monthly_profit
    
    last_profit = int(profit)
    average_change = (last_profit - first_profit)/(month_count - 1)
    print(f"There are {month_count} distinct months in this file.")
    print(f"The total profit over this period is ${total_profit}.00 ")
    print(f"The average change in profits is {average_change}")
    print(f"The greatest decline in profits was {least_change} on {least_date}")
    print(f"The greatest increase in profits was {greatest_change} on {greatest_date}")

    # Specify the file to write to
output_path = os.path.join("C:/Users/paulk/Documents/python-challenge/PyBank/Resources/budget_summary.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as txtfile:
    # Write the rows
    txtfile.write(f" There are {month_count} distinct months in this file. \n ")
    txtfile.write(f"The total profit over this period is ${total_profit}.00 \n ")
    txtfile.write(f"The average change in profits is {average_change} \n ")
    txtfile.write(f"The greatest decline in profits was {least_change} on {least_date} \n ")
    txtfile.write(f"The greatest increase in profits was {greatest_change} on {greatest_date}")