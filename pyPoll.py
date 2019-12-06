# This is the pyPoll Code

# Step 1: Declare the variables we need
line_count = 0
vote_count = 0
khan_count = 0
correy_count = 0
li_count = 0
khan_pct = 0.00
correy_pct = 0.00
li_pct = 0.00
winner = " "
other_party = []
other_count = 0
other_pct = 0.00

# Step 2: Pull the data from the .csv file

import os
import csv
csvpath = os.path.join("C:/Users/paulk/Documents/python-challenge/PyPoll/Resources/election_data.csv")
#open the csv file
with open(csvpath, newline='') as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter = ",")

    # Step 2: Execute "months" protocol
    for row in csvreader:
        line_count += 1
        if line_count == 1:
            vote_count = 0
        elif str(row[2]) == "Khan":
            khan_count += 1
            vote_count += 1
        elif str(row[2]) == "Correy":
            correy_count += 1
            vote_count += 1
        elif str(row[2]) == "Li":
            li_count += 1  
            vote_count += 1       
        elif str(row[2]) in other_party:
            other_count += 1
            vote_count += 1     
        else:
            other_party.append(str(row[2]))
            other_count += 1
            vote_count += 1

    khan_pct = khan_count/vote_count
    correy_pct = correy_count/vote_count
    li_pct = li_count/vote_count
    other_pct = other_count/vote_count
    winner = max(li_count, correy_count, khan_count)

    if winner == li_count:
        print(f"Li has won the election.")
    if winner == khan_count:    
        print(f"Khan has won the election.")
    if winner == correy_count:
        print(f"Correy has won the election.")    

    print(f"There are {vote_count} total votes in this file.")
    print("Khan has {:4.2%} of the vote with {: d} total votes.".format(khan_pct, khan_count))
    print("Correy has {:4.2%} of the vote with {: d} total votes.".format(correy_pct, correy_count))
    print("Li has {:4.2%} of the vote with {: d} total votes.".format(li_pct, li_count))
    print("All other candidates received {:4.2%} of the vote with {: d} total votes".format(other_pct, other_count))
    print(f"The field of other candidates include {other_party}")

    output_path = os.path.join("C:/Users/paulk/Documents/python-challenge/PyPoll/Resources/election_data.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as txtfile:

    # Initialize csv.writer
    csvwriter = csv.writer(txtfile, delimiter=' ')

    # Write the rows
    txtfile.write(f" There are {vote_count} total votes in this file. \n ")
    txtfile.write("Khan has {:4.2%} of the vote with {: d} total votes. \n ".format(khan_pct, khan_count))
    txtfile.write("Correy has {:4.2%} of the vote with {: d} total votes. \n ".format(correy_pct,correy_count))
    txtfile.write("Li has {:4.2%} of the vote with {: d} total votes. \n ".format(li_pct, li_count))
    txtfile.write("All other candidates received {:4.2%} of the vote with {: d} total votes\n ".format(other_pct, other_count))
    txtfile.write(f"The field of other candidates include {other_party} \n ")