import pandas as pd
import csv

###   FOR Jupyter    #############################
# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn
# %matplotlib inline
######################################   END FOR Jupyter

menu_csv_address = 'C:/Users/Mohan/Documents/ColumbiaFinTech/CU-NYC-FIN-PT-12-2019-U-C-master/Homework/02-Python/Instructions/PyRamen/Resources/menu_data.csv'
sales_csv_address = 'C:/Users/Mohan/Documents/ColumbiaFinTech/CU-NYC-FIN-PT-12-2019-U-C-master/Homework/02-Python/Instructions/PyRamen/Resources/sales_data.csv'
report_txt_address = 'C:/Users/Mohan/Documents/ColumbiaFinTech/CU-NYC-FIN-PT-12-2019-U-C-master/Homework/02-Python/Instructions/PyRamen/report.txt' 
with open(menu_csv_address) as csvfile:
    menu = []
    csvReaderObj = csv.reader(csvfile)
    menuHeader = next(csvReaderObj) # skips 1st row / column header
    for row in csvReaderObj:
        menu.append(row)
    

with open(sales_csv_address) as csvfile2:
    sales = []
    csvReaderObj2 = csv.reader(csvfile2)
    salesHeader = next(csvReaderObj2) # skips 1st row / column header
    for row in csvReaderObj2:
        sales.append(row)
    
# Need to Initialize empty Dictionary for multiple appends
report = {}


#### LOOP explanation; 

### 
for row in sales:
    if row[4] in report: #checks to see if Menu Item exist
        #Assumes key-value already exists, adds to existing "01-count" nested dict value
        report[row[4]]["01-count"] += int(row[3])
    else:# Menu item not found. Add it to Dictionary then also add quantities
        print(f"New Item Found. Adding to Dict {row[4]}")
        #Initializes new nested dict   
        report[row[4]] = {
            "01-count": 0,
            "02-revenue": 0,
            "03-cogs": 0,
            "04-profit": 0
        }
        report[row[4]]["01-count"] = int(row[3]) # sets initial revenue for 1st item
## Exit for loop - at this point the dict report obj has all the unique keys( item name )  within the sales list.  
# this loop will now check ea menu item to see if it exists in the report dict. If it does it will get the price and
# cost then use it to compute revenue, cogs and profit. it will ignore menu items that had no sales history
# More effecient to run this loop outside since it only needs 1 pass.
for item in menu:
    if item[0] in report:
        #found an item; grab price and cost and compute rev,cogs and profit. store in dict within apt key-value
        #item[3] # Price of current item
        #item[4] # Cost of current item
        
        #Compute Revenue
        report[item[0]]["02-revenue"] = int(item[3]) * int(report[item[0]]["01-count"])
        #Compute Cost

        report[item[0]]["03-cogs"] = int(item[4]) * int(report[item[0]]["01-count"])
        #Compute Profit
        report[item[0]]["04-profit"] = report[item[0]]["02-revenue"] - report[item[0]]["03-cogs"]
        
    else:
        print(f"{item[0]} not found!")
            

#Prep to Print to text file - report.txt
myList = []
for item in report:
    myStr = ""
    myStr += item
    myStr += str(report[item])
    myList.append(myStr)

repFileObj = open(report_txt_address, "w")

for line in myList:
    print(line,file=repFileObj)

repFileObj.close()

##### Jupyter #############################################
#set lists for Bar Charts
#pHeights = []
#pBars = []
#pLows = []
#for item in report:
#    pBars.append(item)
#    pHeights.append(report[item]['04-profit'])
#    pLows.append(report[item]['03-cogs'])
# Horizontal Bar charts with Profit and Cost overlap
# plt.rcdefaults()
# fig, ax = plt.subplots()
# y_pos = np.arange(len(pBars))
# error = np.random.rand(len(pBars))
# ax.barh(y_pos, pHeights, xerr=error, align='center')
# ax.barh(y_pos, pLows, xerr=error, align='center',alpha=0.5,color='r')
# ax.set_yticks(y_pos)
# ax.set_yticklabels(pBars)
# ax.invert_yaxis()  # labels read top-to-bottom
# ax.set_xlabel('Profits vs costs')
# plt.show()
#################################### END JUPYTER ONLY