#%%
import csv
import os

#set csv file path
election_data = 'Resource\\election_data.csv'

#open file and read csv data
with open (election_data, encoding= 'UTF-8') as csvfile:
    data_reader = csv.DictReader(csvfile)    
    print (data_reader)

    #voter ID rows = total number of votes
    #voted_id = 0 because in a dictionary, the first row along with the header has values so not to ignore
    voter_id=0

    #set empty list to append unique names into later
    unique_candidate_list=[]
    #set candidate_counts as empty dictionary to count total number of votes per candidate later
    candidate_counts = {}

    #loop through each row of voter id, and append unique names into list as above
    for row in data_reader:
        voter_id+=1
        target_column = row['Candidate']
                      
        if  row['Candidate'] not in unique_candidate_list:
            unique_candidate_list.append(target_column)

       #if current candidate name is inside dictionary, add 1 to the count. 
        if target_column in candidate_counts:
            candidate_counts[target_column] += 1
        #Else, set value to 1 and move to next iteration
        else:
            candidate_counts[target_column] = 1
 

    print(f"Candidates : {unique_candidate_list}")
    print(f"Total votes : {voter_id}")
    print(f"Total votes per candidate: {candidate_counts}")

    winner = max(candidate_counts, key=candidate_counts.get)
    print(f"Winner:{winner}")
    
    message= (
        f"Election Results\n"
        f".....................\n"
        f"Total Votes: {voter_id}\n"
        f".....................\n"
        f"{candidate_counts}\n"
        f".....................\n")   
        
    
    for candidate, count in candidate_counts.items():
        percentage = round((count / voter_id) * 100, 3)
        print(f"{candidate}: {percentage}%")
        message+= (f"{candidate}:{percentage}%\n")
    message += (f".....................\n"
        f"Winner: {winner}")

     #create new text file with analysis
    with open("PyPoll.txt", "w") as f:
        f.write(message)
# %%
