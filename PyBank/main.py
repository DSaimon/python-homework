import pandas as pd
import csv
from statistics import mean 

budget_csv_address = 'C:/Users/Mohan/Documents/ColumbiaFinTech/CU-NYC-FIN-PT-12-2019-U-C-master/Homework/02-Python/Instructions/PyBank/Resources/budget_data.csv'


with open(budget_csv_address) as csvfile:
    budgetList = []
    csvReaderObj = csv.reader(csvfile)
    budgetHeader = next(csvReaderObj) # skips 1st row / column header
    for row in csvReaderObj:
        budgetList.append(row)
    
totalMonths = len(budgetList)

# loop uses iterator to peek 1 space ahead ( for change between month calc)
changeList = []
absChangeList = []
totalProfit = 0
changeSum = 0

dictMonthlyChanges = {}

for i in range(totalMonths-1):
    currAmount = int(budgetList[i][1])
    nextAmount = int(budgetList[i+1][1])
    currChange = nextAmount - currAmount
    changeSum += currChange
    changeList.append(currChange)
    absChangeList.append(abs(currChange))
    dictMonthlyChanges[budgetList[i][0]] = currChange
    
    totalProfit += currAmount
    
# this needs to run since loop does 1 less length
totalProfit += int(budgetList[totalMonths-1][1])

#Change calculations
averageChange = changeSum / (totalMonths - 1)
maxDec = 0
maxInc = 0
maxDecMonth = ""
maxIncMonth = ""
for change in dictMonthlyChanges:
    if int(dictMonthlyChanges[change]) > maxInc:
        maxInc = dictMonthlyChanges[change]
        maxIncMonth = change
    if int(dictMonthlyChanges[change]) < maxDec:
        maxDec = dictMonthlyChanges[change]
        maxDecMonth = change
        
print(maxDec)
print(maxDecMonth)
print(maxInc)
print(maxIncMonth)





########### Prep for printing
strOutput = ""
strOutput += "Financial Analysis\n"
strOutput += "----------------------------\n"
strOutput += f"Total Months: {totalMonths}\n"
strOutput += f"Total: ${totalProfit}\n"
strOutput += f"Average Change: ${round(averageChange,2)}\n"
strOutput += f"Greatest Increase in Profits: {maxIncMonth} (${max(changeList)})\n"
strOutput += f"Greatest Decrease in Profits: {maxDecMonth} (${min(changeList)})\n"

print(strOutput)


report_text_address = 'C:/Users/Mohan/Documents/ColumbiaFinTech/CU-NYC-FIN-PT-12-2019-U-C-master/Homework/02-Python/Instructions/PyBank/budgeReport.txt'
text_file = open(report_text_address, "w")
n = text_file.write(strOutput)
text_file.close()