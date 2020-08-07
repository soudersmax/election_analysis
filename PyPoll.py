#import dependencies
import csv
import os
#Assign a variable for the file to load from the path
file_to_load = os.path.join("Resources","election_results.csv")
#Assign a variable to save the file to the path
file_to_save = os.path.join("analysis", "election_analysis.txt")

#initialize accumulator
total_votes = 0

#Declare candidate options list
candidate_options = []
#Declare empty dictionary
candidate_votes = {}

#Winning Candidate and Winning Count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Open the election results and read the file
with open(file_to_load) as election_data:
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    # Read the header row.
    headers = next(file_reader)
    # Print each row in the CSV file.
    for row in file_reader:
        #increment total_votes
        total_votes += 1
        #print candidate name from each row
        candidate_name = row[2]

        #Determine unique candidate_name
        if candidate_name not in candidate_options:
            #append candidate_options to include candidate_name
            candidate_options.append(candidate_name)
            #Begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0
        #Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

#save the results to text file
with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)
    
    #Determine Percentage of votes
    #iterate through the list of candidates
    for candidate_name in candidate_votes:
        #retrieve vote count
        votes = candidate_votes[candidate_name]
        #calculate percentage (convert vote to floats)
        vote_percentage = float(votes)/float(total_votes) * 100
        candidate_results = (f"{candidate_name} received {votes:,} votes, for {vote_percentage:.1f}% of the vote.\n")
        #printe each candidate, their vote count and percentage to terminal
        print(candidate_results)
        #save the candidate results to text file
        txt_file.write(candidate_results)        
        
        #Determine winning Vote Count and Candidate
        #Determine if the votes are greater than the winning count
        if(votes > winning_count) and (vote_percentage > winning_percentage):
            #if true then set winning count to votes and winning percent to vote percent
            winning_count = votes
            winning_percentage = vote_percentage
            #set winning_candidate equal to the candidate's name
            winning_candidate = candidate_name
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")     
    print(winning_candidate_summary) 
    #save the winning candidate's name to text file
    txt_file.write(winning_candidate_summary)