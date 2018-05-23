
import os
import csv
import string


file ='C:/Users/shangw/Desktop/21/DS/DataAnalysis Bootcamp/02-Homework/03- Python/PyPoll/raw_data/election_data_1.csv'

#print result title

print ("Election Results")
print ("----------------------")


# open and read raw file 
with open(file, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    
# skip header row    
    csv_header = next(csvfile)
    
#The total number of votes cast
# create vote_cast list as empty
    
    poll_dic ={}
    vote_cast = []
    candidate_list = []
    vote_count = []
    vote_percent = []
#loop through all rows to count how many vote by vote ID, and sum total revenue 
    for row in csv_reader:
 
#add each vote ID to the list
        vote_cast.append(row[0])
    
#print out results, by see how many Vote ID in the list   
        print ("Total Votes: " , len(vote_cast))
        print ("----------------------")
    
        
        if row[2] in poll_dic.keys():
            poll_dic[row[2]] = poll_dic[row[2]] + 1
        else:
            poll_dic[row[2]] = 1
        
    
        for key, value1 in poll_dic.items():
            candidate_list.append(key)
            vote_count.append(value1)
            
    
        for n in vote_count:   
            print (str(candidate_list[n]) + vote_count[n])/(vote_cast[n])*100,str(vote_count[n]))