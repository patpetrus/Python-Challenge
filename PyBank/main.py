

# total number of months in dataset DONE
# net total DONE
# average change DONE
# min/max DONE

import os
import csv

budget_data_csv = os.path.join("C:/Users/patpe/Desktop/Butler/Python-Challenge/PyBank/Resources/budget_data.csv") 
with open(budget_data_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csv_reader)

    row_number = 0
    net_total = 0
    change_list = []
    previous = 0
    average_change = 0
    max_list = ["", 0]
    min_list = ["", 999999]

    for row in csv_reader:
        row_number = row_number + 1
        net_total = net_total + int(row[1])
        change = int(row[1]) - previous
        change_list.append(change)
        previous = int(row[1])
        
        if change > max_list[1]:
            max_list[1] = change
            max_list[0] = row[0]
        
        if change < min_list[1]:
            min_list[1] = change
            min_list[0] = row[0]

    average_change = sum(change_list[1:]) / (len(change_list) - 1)
    print("Financial Analysis:")
    print("--------------------")
    print(f"Total Months: " + str(row_number))
    print(f"Total Net Profit: " + str(net_total))
    print(f"Average Change: " + str(average_change))
    print(f"Greatest Increase in Profits: " + max_list[0], max_list[1])
    print(f"Greatest Decrease in Profits: " + min_list[0], min_list[1])

# --------------------------------------------------------------------