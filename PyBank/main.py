import os
import csv
import sys

budget_csv = os.path.join('budget_data.csv')
# Py_bank = open("Py_bank.txt","w")
# sys.stdout = Py_bank

print("Financial Analysis")
print("----------------------------------")

with open(budget_csv,newline="") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    csv_header = next(csvfile)

    count = 0
    total = 0
    previous_value=0
    sum1=0
    max1=0 
    max_row=None 
    min_row=None 
    low1=sys.maxsize
    
    for row in csvreader:
        
        count=count+1                          #Calculate's the total number of months
        total=total + int(row[1])              #Calculate's the total amount of Profit/Loss
        
        if previous_value != 0:             
            sum1+=int(row[1])-previous_value   #Calculate's the average change of profit/loss
            
            change=int(row[1])-previous_value

            if max1<change:                    #Compares current change value to previous max
                max1=max(change,max1)
                max_row=row
            if low1>change:                    #Compares current change value to previous low
                low1=min(change,low1)
                min_row=row
            
            previous_value=int(row[1])         #Assigns the current row value to previous value
        else:
            previous_value=int(row[1])

                        
    print(f'Total Months: {count}')
    print(f'Total: ${total}')
    print(f'Average Change: {round(sum1/(count-1),2)}')
    print(f'Greatest Increase in Profits: {max_row[0]}  (${max1})')
    print(f'Greatest Decrease in Profits: {min_row[0]}  (${low1})')
    
    

    

