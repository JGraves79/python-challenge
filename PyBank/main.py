# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 10:11:51 2024

@author: X579430
"""
import os
import csv
from datetime import datetime

# Files to load and output (update with correct file paths)
file_to_load = "C:\\Users\\X579430\\Documents\\Python Scripts\\python-challenge\\PyBank\\Resources\\budget_data.csv"
# file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path 
# file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path
file_to_output = "C:\\Users\\X579430\\Documents\\Python Scripts\\python-challenge\\PyBank\\analysis\\budget_analysis.txt"

# Define variables to track the financial data
total_months = 0
total_net = 0
net_change_list = []
month_of_change = []
greatest_increase = ["", 0]
greatest_decrease = ["", 0]
previous_net = 0
# Add more variables to track other necessary financial data

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    first_row = next(reader)
    total_months += 1
    total_net += int(first_row[1])
    previous_net = int(first_row[1])

    # Track the total and net change


    # Process each row of data
    for row in reader:
        # Track the total

        total_months += 1
        total_net += int(row[1])



        # Track the net change
        net_change = int(row[1]) - previous_net
        previous_net = int(row[1])
        net_change_list.append(net_change)
        month_of_change.append(row[0])


        # Calculate the greatest increase in profits (month and amount)
        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change

        # Calculate the greatest decrease in losses (month and amount)
        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change


# Calculate the average net change across the months
average_change = sum(net_change_list) / len(net_change_list)

# Generate the output summary
output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Losses: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
)

# Print the output
print(output)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
