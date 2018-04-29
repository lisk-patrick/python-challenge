import csv
import os

budgetReader1 = []
budgetData = []
csvpath1 = os.path.join("..","HOMEWORK","Instructions","PyBank","raw_data", "budget_data_1.csv")
csvpath2 = os.path.join("..", "HOMEWORK", "Instructions", "PyBank", "raw_data", "budget_data_2.csv")

with open(csvpath1, newline="") as csvfile1:
    budgetReader1 = csv.reader(csvfile1, delimiter= ",")
    
    total_revenue = 0
    for row in budgetReader1:
        budgetHeader = [row[0]]
        row_count = sum(1 for row in budgetReader1)
        total_months = int(row_count)

       # for i in range(2, row_count):
           # total_revenue += float(i[1])
    print(total_months)
    print(total_revenue)

    with open(csvpath2, newline="") as csvfile2:
        budgetReader2 = csv.reader(csvfile2, delimiter=",")

        total_revenue = 0
        for row in budgetReader2:
            row_count = sum(1 for row in budgetReader2)
            total_months = int(row_count)
            #for i in range(2,row_count):
                #total_revenue += float(i[1])
        print(total_months)
        print(total_revenue)