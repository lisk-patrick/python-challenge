import csv
import os

budgetReader1 = []
date = []
revenue = []
budgetData = []
csvpath1 = os.path.join("..","HOMEWORK","Instructions","PyBank","raw_data", "budget_data_1.csv")
#csvpath2 = os.path.join("..", "HOMEWORK", "Instructions", "PyBank", "raw_data", "budget_data_2.csv")

def csvReader():    
    with open(csvpath1, newline="") as csvfile1:
        budgetReader1 = csv.reader(csvfile1, delimiter= ",")
        budegetReader2 = csv.reader(csvfile2, delimiter= ",")
        for row in budgetReader1:
        
            def row2row_avg():
                rowbyrow = []
                row_change = row[1] - row.next[1]
                monthly_avg_change = float(row_change / 2)
                print(monthly_avg_change)

        total_rev = sum(row[1])
        month_count = sum(1 for row in budgetReader1)
        total_months = int(month_count)
        date.append(row[0])
        revenue.append(row[1])
        budgetData = zip(date,revenue)
        
        current_revenue = row[1]
        next_revenue = next(row[1])
        if next_revenue == 0:
            break
        else:
            month2month_difference = next_revenue - current_revenue
            sum_month2month_revenue += float(current_revenue)
            sum_month2month_revenue = 0
        
       # for i in range(2, row_count):
    
           # total_revenue += float(i[1])
    print(total_months)
    print(month2month_avg)
    print(budgetData)

    #with open(csvpath2, newline="") as csvfile2:
     #   budgetReader2 = csv.reader(csvfile2, delimiter=",")

      #  total_revenue = 0
       # for row in budgetReader2:
        #    row_count = sum(1 for row in budgetReader2)
         #   total_months = int(row_count)
            #for i in range(2,row_count):
                #total_revenue += float(i[1])
     #print(total_months)
        #print(total_revenue)
    
