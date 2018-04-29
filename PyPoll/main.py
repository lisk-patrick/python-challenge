import csv
import os

budgetReader = []
budgetData = []
csvpath1 = os.path.join("..","HOMEWORK","Instructions","PyBank","raw_data", "budget_data_1.csv")

with open(csvpath1, newline="") as csvfile:
    budgetReader = csv.reader(csvfile, delimiter= ",")
    
    total_revenue = 0
    for row in budgetReader:
        budgetHeader = [row[0]]
        row_count = sum(1 for row in budgetReader)
        total_months = int(row_count)

        for i in range(2, row_count):
            total_revenue += float(i[1])
    print(total_months)
    print(total_revenue)