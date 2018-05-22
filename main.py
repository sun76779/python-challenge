# -*- coding: utf-8 -*-
"""
Created on Tue May 22 10:16:39 2018

@author: shangw
"""
import os
import csv
import string


file ='C:/Users/shangw/Desktop/21/DS/DataAnalysis Bootcamp/02-Homework/03- Python/PyBank/raw_data/budget_data_2.csv'



#print result title

print ("Financial Analysis")
print ("-----------------------------------")


# open and read raw file 
with open(file, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    
# print and skip header row    
    csv_header = next(csvfile)
    
#The total number of months included in the dataset
#create month_counter list as empty    
    month_counter = []


#The total amount of revenue gained over the entire period
# create revenue list as empty
    revenue = []
 
#loop through all rows to count how many month by row number, and sum total revenue  
    
    for row in csv_reader:


#add each month to the list, and add each revenue to revenue list
        
        month_counter.append(row[0])
        revenue.append(float(row[1]))



#print out results      
    print("Total Months: " , len(month_counter))
    print("Total Revenue: $" + str(sum(revenue)))
    
    
    
#The average change in revenue between months over the entire period
#The greatest increase in revenue (date and amount) over the entire period
#The greatest decrease in revenue (date and amount) over the entire period


#create a empty list for revenue_change    
revenue_change = []


#loop through the list in revenue, starting from 2nd revenue
for line in range(1,len(revenue)):
    
#Add each change to revenue_change list    
    revenue_change.append(revenue[line]-revenue[line-1])

#Average change by total revenuw change / item numbers in list revenue_change    
average_change = sum(revenue_change)/len(revenue_change)
    
#Look for the max change, and the month       
max_change = max(revenue_change)
max_change_month = str(month_counter[revenue_change.index(max(revenue_change))])
    
#Look for the greatest decrease, and the month       
min_change = min(revenue_change)
min_change_month = str(month_counter[revenue_change.index(min(revenue_change))])   


#print results    
print("Average Revenue Change: $" + str(round(average_change,2)))
    
print("Greatst Increase in Revenue: " + str(max_change_month) + "  (" + str(max_change) +")")
    
print("Greatst Decrease in Revenue: " + str(min_change_month) + "  (" + str(min_change) +")")







    

      

    
    
    
    
    
    
    