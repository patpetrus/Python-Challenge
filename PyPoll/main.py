# total votes cast

import os
import csv
import operator 

election_data_csv = os.path.join("C:/Users/patpe/Desktop/Butler/Week-03-Python/Homework/Instructions/PyPoll/Resources/election_data.csv")
with open(election_data_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csv_reader)

    total_votes = 0
    candidate_list = []
    candidate_dict = {}
    stats = {}
    winner = ""
    max_votes = 0
    candidate_percent = {}

    for row in csv_reader:
        total_votes = total_votes + 1
        if row[2] not in candidate_list:
            candidate_list.append(row[2])
            candidate_dict[row[2]] = 0
        candidate_dict[row[2]] = candidate_dict[row[2]] + 1
    print("Election Results:")
    print("--------------------")
    print(f"Total Votes: {total_votes}")
    # print(f"All Candidates: " + str(candidate_list))

    for x in candidate_dict:
        candidate_percent[x] = round(candidate_dict[x] / total_votes * 100, 4)
        if candidate_dict[x] > max_votes:
            winner = x
            max_votes = candidate_dict[x]
        print(f"{x}, {candidate_percent[x]}%, {candidate_dict[x]}")

    print(f"Winner: {winner}")
    # print(max_votes)