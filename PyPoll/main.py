#%%
import csv
import os

#set csv file path
election_data = 'Resource\\election_data.csv'

#open file and read csv data
with open (election_data, encoding= 'UTF-8') as csvfile:
    data_reader = csv.DictReader(csvfile)    
    print (data_reader)

    #read header in data
    csv_header = next(data_reader)
    print (f"(CSV Header: + {csv_header})")

    #total voters = total number of rows
    voter_id=1
    unique_candidate_list=[]
    candidate_counts = {}

    
    for row in data_reader:
        voter_id+=1
        target_column = row['Candidate']

        if  row['Candidate'] not in unique_candidate_list:
            unique_candidate_list.append(row['Candidate'])
            
        if target_column in candidate_counts:
            candidate_counts[target_column] += 1
        else:
            candidate_counts[target_column] = 1
 

    print(f"Candidates : {unique_candidate_list}")
    print(f"Total votes : {voter_id}")
    print(f"Total votes per candidate: {candidate_counts}")

    winner = max(candidate_counts, key=candidate_counts.get)

    for candidate, count in candidate_counts.items():
        percentage = round((count / voter_id)*100 , 2)
        print({candidate}: {percentage}%)

    print(winner)

    message= (
        f"Election Results\n"
        f".....................\n"
        f"Total Votes: {voter_id}\n"
        f".....................\n"
        f"{candidate_counts}\n"
        f"{candidate}:{percentage}%\n"
        f".....................\n"
        f"Winner: {winner}")

     #create new text file with analysis
    with open("PyPoll.txt", "a") as f:
        f.write(message)


    

        
# %%
