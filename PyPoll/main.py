# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 10:24:17 2024

@author: X579430
"""
import csv
import os

base_dir = os.path.dirname(__file__)

# Files to load and output (update with correct file paths)

file_to_load = os.path.join(base_dir, "Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join(base_dir, "analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast
candidate_options = []  # candidate names
candidate_votes = {}  # vote counts for each candidate

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:
        # Print a loading indicator (for large datasets)
        print(". ", end="")

        # Increment the total vote count for each row
        total_votes += 1

        # Get the candidate's name from the row
        candidate_name = row[2]

        # If the candidate is not already in the candidate list, add them
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0

        # Add a vote to the candidate's count
        candidate_votes[candidate_name] += 1

# Open a text file to save the output
with open(file_to_output, "w") as txt_file:
    # Print the total vote count (to terminal)
    election_results = (f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n")
    
    print(election_results, end="")
    txt_file.write(election_results)

    # Loop through the candidates to determine vote percentages and identify the winner
    for candidate in candidate_votes:
        # Get the vote count and calculate the percentage
        votes_count = candidate_votes[candidate]
        vote_percentage = float(votes_count) / float(total_votes) * 100

        # Update the winning candidate if this one has more votes
        if (votes_count > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes_count
            winning_candidate = candidate
            winning_percentage = vote_percentage

        # Print and save each candidate's vote count and percentage
        candidate_results = f"{candidate}: {vote_percentage:.3f}% ({votes_count})\n"
        print(candidate_results, end="")
        txt_file.write(candidate_results)

    # Generate and print the winning candidate summary
    winning_candidate_summary = (f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"-------------------------\n")
    
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)
