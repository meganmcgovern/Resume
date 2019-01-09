#Import dependecies

import os
import csv

#Create variables

total_votes = 0
votes_khan = 0
votes_correy = 0
votes_li = 0
votes_otooley = 0

#Import file
csvpath = os.path.join('election_data.csv')

#Read in file
with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    #skip header
    csv_header = next(csvreader)

    #go through csv rows
    for row in csvreader:

        #Count voter ids to find number of votes cast
        total_votes +=1

        #Now cycle through to find counts for each candidate
        if row[2] == "Khan":
            votes_khan +=1
        elif row[2] == "Correy":
            votes_correy +=1
        elif row[2] == "Li":
            votes_li +=1
        elif row[2] == "O'Tooley":
            votes_otooley +=1

#Summarize the results
percent_khan = (votes_khan/total_votes) *100
percent_correy = (votes_correy/total_votes) *100
percent_li = (votes_li/total_votes) *100
percent_otooley = (votes_otooley/total_votes) *100

#Find the winner with dictionaries of lists
candidates = ["Khan", "Correy", "Li", "OTooley"]
votes_cast = [votes_khan, votes_correy, votes_li, votes_otooley]

#Zip lists to match the candidate with their vote total
candidates_votes = dict(zip(candidates,votes_cast))

#Find winner with max of zipped dictionary
key = max(candidates_votes, key=candidates_votes.get)

#Print all results in terminal
print("Election Results")
print("----------")
print(f"Total Votes Cast: {total_votes}")
print("------------")
print(f"Khan Votes: {percent_khan:.2f}% ({votes_khan})")
print(f"Correy Votes: {percent_correy:.2f}% ({votes_correy})")
print(f"Li Votes: {percent_li:.2f}% ({votes_li})")
print(f"OTooley Votes: {percent_otooley:.2f}% ({votes_otooley})")
print(f"Winner: {key}!")

#Create an output file location
output_path = os.path.join("new_py_poll.txt")

with open(output_path, 'w', newline='') as txtfile:

    txtfile.write("Election Results")
    txtfile.write("\n")
    txtfile.write("----------------")
    txtfile.write("\n")
    txtfile.write(f"Total Votes: {total_votes}")
    txtfile.write("\n")
    txtfile.write("----------------")
    txtfile.write("\n")
    txtfile.write(f"Khan Votes: {percent_khan:.2f}% ({votes_khan})")
    txtfile.write("\n")
    txtfile.write(f"Correy Votes: {percent_correy:.2f}% ({votes_correy})")
    txtfile.write("\n")
    txtfile.write(f"Li Votes: {percent_li:.2f}% ({votes_li})")
    txtfile.write("\n")
    txtfile.write(f"OTooley Votes: {percent_otooley:.2f}% ({votes_otooley})")
    txtfile.write("\n")
    txtfile.write(f"Winner: {key}!")
    txtfile.write("----------------")