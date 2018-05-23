# -*- coding: utf-8 -*-
"""
Created on Wed May 23 14:28:23 2018

@author: shangw
"""

import os
import csv


file ='C:/Users/shangw/Desktop/21/DS/DataAnalysis Bootcamp/02-Homework/03- Python/PyBoss/raw_data/employee_data1.csv'

#import state abbrev dictionary
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
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
    'Wyoming': 'WY',
}


# Lists to store data
Emp_ID = []
first_name = []
last_name = []
DOB = []
SSN = []
State = [] 



with open(file, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")


# print and skip header row  
    csv_header = next(csvfile)
    


    for row in csvreader:
        
        # Add ID
        Emp_ID.append(row[0])
        
        
        # Add first/last name
        fullname = row[1].split(" ")
        first_name.append(fullname[0])
        last_name.append(fullname[1])
        
            
        # Add DOB
        DOB.append(row[2])
        dobnumber = row[2].split("-")
        DOB.append(dobnumber[1] + '/' + dobnumber[2] + '/' + dobnumber[0])
        
        # Add SSN
        fullSSN = row[3].split("-")
        SSN.append("***-**-"+str(fullSSN[2]))

        
        # Add State
        State.append(us_state_abbrev[row[4]])
        
      
# Zip lists together
cleaned_csv = zip(Emp_ID, first_name, last_name, DOB, SSN, State)

# Set variable for output file
output_file = os.path.join("pyBoss")

#  Open the output file
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    # Write the header row
    writer.writerow(["Emp ID", "First Name", "Last Name", "DOB", "SSN", "State"])

    # Write in zipped rows
    writer.writerows(cleaned_csv)
