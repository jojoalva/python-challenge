#%%
import csv
import os

#set path of csv file
data_file = 'Resource\\budget_data.csv'

#open file and read csv data
with open (data_file, encoding= 'UTF-8') as csvfile:
    data_reader = csv.reader(csvfile, delimiter =",")
    print(data_reader)

    #read header in data
    csv_header = next(data_reader)

    #print header
    print (f"(CSV Header: + {csv_header})")

    # read data in line 2
    row_2_data = next(data_reader)

    #set first comparison value
    row_2_value = int(row_2_data[1])

    #set month to begin counting at 1
    total_months = 1

    #set total profit loss value outside loop so it includes the first row of data
    total_pl = row_2_value

    #set first comparison value for the net change between two values
    prev_value = row_2_value  

    #set net change as list 
    net_change = []

    #set month and profit/loss change as dictionary
    Month_and_PL = {}


# start for loop to compare 
    for row in data_reader:
        month,value = row
        total_months += 1       
        total_pl += int(row[1])       
        current_value = int(row[1])
        #find change between current value and new value
        new_value = current_value-prev_value
        #append this to a new list
        net_change.append(new_value)
        #enter new value and corresponding month into dictionary
        Month_and_PL[month] = new_value
        #reset previous value to the current value
        prev_value = current_value
    
    #max and minimum values inside dictionary
    max_value = max(Month_and_PL.values())  
    min_value = min(Month_and_PL.values())
   
    #find the corresponding month to the max and min values
    for month, value in Month_and_PL.items():
        if value == max_value:
            max_month = month
        elif value == min_value:
            min_month = month               
        
    #average of the total net_change list, divided by month - 1 because we had to ignore the first month of data
    average = sum(net_change)/(total_months-1)

    #define function to call analysis
    message =(f"Financial Analysis\n"
        f".................................................\n"
        f"Total months: {total_months}\n"
        f"Total Profit/Losses: {total_pl}\n"
        f"Average Change: {round(average, 2)}\n"
        f"Greatest Increase in Profits: {max_month} (${max_value})\n"
        f"Greatest Decrease in Profits: {min_month} (${min_value})")
    
    print(message)

    #create new text file with analysis
    with open("PyBank.txt", "w") as f:
        f.write(message)
# %%
