# This is the pyBoss Code

# Step 1: Declare the variables we need
line_count = 0
ID = []
fullname = []
splitname = ["",""]
olddate = []
splitdate = ["", "", ""]
oldstate = []
oldSSN = []
splitSSN = []
newrow =[]

us_states = {
	'Alabama': 'AL',
	'Alaska': 'AK',
	'Arizona': 'AZ',
	'Arkansas': 'AR',
	'California': 'CA',
	'Colorado': 'CO',
	'Connecticut': 'CT',
	'Delaware': 'DE',
	'District of Columbia': 'DC',
	'Florida': 'FL',
	'Georgia': 'GA',
	'Hawaii': 'HI',
	'Idaho': 'ID',
	'Illinois': 'IL',
	'Indiana': 'IN',
	'Iowa': 'IA',
	'Kansas': 'KS',
	'Kentucky': 'KY',
	'Louisiana': 'LA',
	'Maine': 'ME',
	'Maryland': 'MD',
	'Massachusetts': 'MA',
	'Michigan': 'MI',
	'Minnesota': 'MN',
	'Mississippi': 'MS',
	'Missouri': 'MO',
	'Montana': 'MT',
	'Nebraska': 'NE',
	'Nevada': 'NV',
	'New Hampshire': 'NH',
	'New Jersey': 'NJ',
	'New Mexico': 'NM',
	'New York': 'NY',
	'North Carolina': 'NC',
	'North Dakota': 'ND',
	'Ohio': 'OH',
	'Oklahoma': 'OK',
	'Oregon': 'OR',
	'Pennsylvania': 'PA',
	'Rhode Island': 'RI',
	'South Carolina': 'SC',
	'South Dakota': 'SD',
	'Tennessee': 'TN',
	'Texas': 'TX',
	'Utah': 'UT',
	'Vermont': 'VT',
	'Virginia': 'VA',
	'Washington': 'WA',
	'West Virginia': 'WV',
	'Wisconsin': 'WI',
	'Wyoming': 'WY'
}
# Step 2: Pull the data from the .csv file

import os
import csv
csvpath = os.path.join("C:/Users/paulk/Documents/python-challenge/PyBoss/Resources/employee_data.csv")

output_path = os.path.join("C:/Users/paulk/Documents/python-challenge/PyBoss/Resources/new_data.csv")
#open the csv file
with open(csvpath, newline='') as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter = ",")

    # Step 2: Execute "months" protocol
    for row in csvreader:
        ID.append(row[0])
        fullname.append(row[1])
        olddate.append(row[2])
        oldSSN.append(row[3])
        oldstate.append(row[4])
        line_count += 1
                    
    print(f"There are {line_count} distinct lines in this file.")
    
# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    csvwriter.writerow(['Emp ID', 'First Name', 'Last Name', 'DOB', 'SSN', 'State'])
    
    for i in range(1, line_count):
        newrow.append(ID[i])
        splitname = fullname[i].split()
        newrow.append(splitname[0])
        newrow.append(splitname[1])
        splitdate = olddate[i].split(sep="-")
        newrow.append(splitdate[1] + "/" + splitdate[2] + "/" + splitdate[0])
        splitSSN = oldSSN[i].split(sep="-")
        newrow.append("***-**-" + splitSSN[2])
        newrow.append(us_states[oldstate[i]])
        csvwriter.writerow(newrow)
        if i < 6:
            print(newrow)
        newrow = []
