#%%
import csv
import os
#set path of csv file
data_file = 'Resource\\budget_data.csv'

#open file and read csv data
with open (data_file, encoding= 'UTF-8') as csvfile:
    data_reader =csv.reader(csvfile, delimiter =",")
    
    print(data_reader)

    #read through rows in data
    
    csv_header = next(data_reader)
    print (f"CSV Header: {csv_header}")
    rowcount = 0
    for row in data_reader:
        rowcount += 1
        print("Number of months:", rowcount)

        




    
    #for row in data_reader:

# %%
