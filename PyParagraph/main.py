# -*- coding: utf-8 -*-
"""
Created on Wed May 23 15:20:18 2018

@author: shangw
"""

# -*- coding: utf-8 -*-
"""
Created on Wed May 23 14:28:23 2018

@author: shangw
"""

import os
import csv
import re


file ='C:/Users/shangw/Desktop/21/DS/DataAnalysis Bootcamp/02-Homework/03- Python/PyParagraph/raw_data/paragraph_2.txt'


# Lists to store data
Txt_Count = []


with open(file, 'r') as txtfile:
    txtreader = txtfile.read()


    print("----------------------------")   


    for row in txtreader:     
            
        # Add Word_Count
        Word_Count = txtreader.count(" ")+1
      
        # Add Sent_Count
        Sent = row[0].split(".") + row[0].split("?") + row[0].split("!")
        Sent_Count = len(Sent) + 1
    
    
    
        # Add Letter_Count and Calculate Average_Letter
        Txt_Count.append(row[0])
        Letter_Count = len(Txt_Count) - txtreader.count(" ") - txtreader.count(".")
        - txtreader.count(",") - txtreader.count(">") - txtreader.count("!") - txtreader.count("?")
        - txtreader.count("(") - txtreader.count(")") - txtreader.count("-") - txtreader.count("'")
        
        Average_Letter = float(Letter_Count / Word_Count)
 
    
        # Add Letter_Count and Calculate Average_Letter
        Txt_Count.append(row[0])
        Sent_Length = float(Word_Count / Sent_Count)
    
    
    
    #print out all results 
    
    print ("Approximate Word Count: ",str(Word_Count))
    print ("Approximate Sentence Count: ",str(Sent_Count))
    print ("Average Letter Count: ",str(Average_Letter))
    print ("Average Sentence Length: ",str(Sent_Length))

"""
re.split("(?&lt;=[.!?]) +", txtreader)
"""        
        
  