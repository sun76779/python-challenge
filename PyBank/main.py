import os
import csv


#file ='C:/Users/shangw/Desktop/21/DS/DataAnalysis Bootcamp/02-Homework/03- Python/PyBank/raw_data/budget_data_2.csv'

os.chdir("/Users/shangw/Desktop/USCDATA/python-challenge/PyBank/raw_data")

csvpath=os.path.join('..','raw_data','budget_data_1.csv')


#print result title
print ("Financial Analysis")
print ("-----------------------------------")


# open and read raw file 
with open(csvpath, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    
    # skip header row    
    csv_header = next(csvfile)
    
    #Task 1 The total number of months included in the dataset
    #create month_counter list as empty    
    month_counter = []


    #Task 2 The total amount of revenue gained over the entire period
    # create revenue list as empty
    revenue = []
 
    #loop through all rows to count how many months, and sum total revenue  
    for row in csv_reader:


        #add each month to the list, and add each revenue to revenue list
        month_counter.append(row[0])
        revenue.append(float(row[1]))

 
    
    
    
    
    
    
    #print out results (length of Month list, and total of Revenue list)
    print("Total Months: " , len(month_counter))
    print("Total Revenue: $" + str(sum(revenue)))
    




    
    
#Task 3 The average change in revenue between months over the entire period

#create a empty list for revenue_change    
revenue_change = []


#loop through the list in revenue, starting from 2nd revenue
for line in range(1,len(revenue)):
    
    #Add each change to revenue_change list    
    revenue_change.append(revenue[line]-revenue[line-1])

#Average change by total revenuw change / item numbers in list revenue_change    
average_change = sum(revenue_change)/len(revenue_change)
        
    
#Task 4 The greatest increase in revenue (date and amount) over the entire period
#Task 5 The greatest decrease in revenue (date and amount) over the entire period


#Look for the max change, and the month       
max_change = max(revenue_change)
max_change_month = str(month_counter[revenue_change.index(max(revenue_change))])
        
#Look for the greatest decrease, and the month       
min_change = min(revenue_change)
min_change_month = str(month_counter[revenue_change.index(min(revenue_change))])   
    
    
#print results for Task 3-5
print("Average Revenue Change: $" + str(round(average_change,2)))
       
print("Greatst Increase in Revenue: " + str(max_change_month) + "  (" + str(max_change) +")")
        
print("Greatst Decrease in Revenue: " + str(min_change_month) + "  (" + str(min_change) +")")




#create path for output file
output = os.path.join('..','output','pybank_output_1.txt')

# opens the output destination in write mode and prints the summary
with open(output, 'w') as writefile:
    writefile.writelines("Financial Analysis\n")
    writefile.writelines("-----------------------------------" + "\n")
    writefile.writelines("Total Months: " + str(len(month_counter)) + "\n")
    writefile.writelines("Total Revenue: $" + str(sum(revenue)) + "\n")
    writefile.writelines("Average Revenue Change: $" + str(round(average_change,2)) + "\n")
    writefile.writelines("Greatst Increase in Revenue: " + str(max_change_month) + "  (" + str(max_change) +")" + "\n")
    writefile.writelines("Greatst Decrease in Revenue: " + str(min_change_month) + "  (" + str(min_change) +")")

