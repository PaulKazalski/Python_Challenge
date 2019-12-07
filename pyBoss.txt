# This is the pyBoss Code

#Import the OS and the CSV libraries
import os
import csv
# This changes the directory path nomenclature to a relative one
# (i.e. with repsect to the .py file)
os.chdir(os.path.dirname(os.path.abspath(__file__)))


# Step 1: Declare the variables we need
# This variable tells us what line we're on
line_count = 0
# This list gives us the ID column
ID = []
# This list gives us the original name column, as a full name
fullname = []
# This list acts as two different columns on one row
splitname = ["",""]
# This list gives us the original date in the original format.
olddate = []
# This list acts as three different columns on one row
splitdate = ["", "", ""]
# This list gives us the original state column
oldstate = []
# This list gives us the original SSN column
oldSSN = []
# THis list acts as three different columns on one row
splitSSN = []
# This list comprises the ID, the new name columns, the date columns
# the new state column and the new SSN column as one row.
newrow =[]

#First, a dictionary that converts full state names to their
# abbreviations.
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

# Declare a "read path" in the resources folder
csvpath = os.path.join('.', 'Resources', 'employee_data.csv')
# Declare a "write path in the Resources folder"
output_path = os.path.join('.', 'Resources', 'new_data.csv')
#open the csv file
with open(csvpath, newline='') as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter = ",")

    # Step 2 Go row-by-row and make the changes
    for row in csvreader:
		# Add each value from column A to the ID list
        ID.append(row[0])
		# Add each value from column B to the fullname list
        fullname.append(row[1])
		# Add each value from column C to the olddate list
        olddate.append(row[2])
		# Add each value from column D to the oldSSN list
        oldSSN.append(row[3])
		# Add each value from COlumn E to the oldstate list
        oldstate.append(row[4])
		# increase the linecounter by 1
        line_count += 1
    # Let us know how many lines there are                
    print(f"There are {line_count} distinct lines in this file.")
    
# Open the 'new data' file and start writing
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

	#Write the first row of the new data file
    csvwriter.writerow(['Emp ID', 'First Name', 'Last Name', 'DOB', 'SSN', 'State'])
    
	# Go through each row, declare a unique "new row", write that new row, then discard
    for i in range (1, line_count): 
        newrow.append(ID[i])
        # Split full name into firstname and last name
		# Split name is now a list with two strings - first and last name
		# Add each string to the new row
        splitname = fullname[i].split()
        newrow.append(splitname[0])
        newrow.append(splitname[1])
		# Split the date into month, date and year
		# concatenate each list string with '/'
        splitdate = olddate[i].split(sep = "-")
        newrow.append(splitdate[1] + "/" + splitdate[2] + "/" + splitdate[0])
        # Split SSN by the "-". Concatenate "***-**-" with last four digits
        splitSSN = oldSSN[i].split(sep="-")
        newrow.append("***-**-" + splitSSN[2])
		# Add the modified us states into new row
        newrow.append(us_states[oldstate[i]])
		# Write the new row
        csvwriter.writerow(newrow)
        # For good measure, we'll see the first 5 rows of data to see if it's printing right
        if i < 6:
            print(newrow)
		# Clear the new row.	
        newrow = []
		
