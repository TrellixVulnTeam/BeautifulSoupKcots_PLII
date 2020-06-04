from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv

page = urlopen("http://www.nepalstock.com/main/todays_price")
pageSoup = BeautifulSoup(page, 'lxml')
pageDiv = pageSoup.find('div', class_= 'pager')
totalPages = int(pageDiv.get_text()[-1])

finalList = []
insideList = []

company = [] #'Bank of Kathmandu Ltd.', 'Chhimek Laghubitta Bikas Bank Limited'
totalCompany = 0


innerTuple = ()
outerList = []
addMore = input("Do you want to add more companies? (yes/no)").lower()
while (addMore == "yes"):
    newCompanyName = input("Enter the name of the company")
    #typeOfcompany = input("Enter the type of Company")
    noOfShare = input("Enter the number of Stock you possess:")
    purchasedValue = input("Enter the value of the share purchased :")
    company.append(newCompanyName)        
    innerTuple = ()
    innerTuple = innerTuple + (newCompanyName,noOfShare,purchasedValue,)
    outerList.append(innerTuple)
    addMore = input("Do you want to add more companies? (yes/no)").lower()

for data in company:
    totalCompany = totalCompany + 1



Table = pageSoup.find('table')   
def  getDate() :
    date = Table.find('label', {'class':'pull-left'}).text
    char = 6
    finalDate=''
    while char!=16:
        if (date[char]=='-'):
            finalDate = finalDate + "."
        else:
            finalDate = finalDate + date[char]
        char = char + 1
    return finalDate
Date = getDate()

def getCsvHeader():
    tableHeaderLink = Table.find('tr',{'class' : 'unique'})
    tableHeaderData = tableHeaderLink.find_all('td')
    tableHeaderTuple = ()
    a = 0
    for td in tableHeaderData:
        a = a + 1
        dataForTuple = td.get_text()
        if(a==2):
            tableHeaderTuple = tableHeaderTuple + ('Date',)
        tableHeaderTuple = tableHeaderTuple + (dataForTuple,)
    return tableHeaderTuple


for page in range(1,totalPages+2):
    link = urlopen("http://www.nepalstock.com/main/todays_price/index/{}/".format(page))
    soup = BeautifulSoup(link, 'lxml')
    table = soup.find('table', class_ = "table table-condensed table-hover")
    for row in table.find_all('tr'):        
        for data in row.find_all('td'):
            check = data.get_text()
            for noOfCompanies in company:
                    if(check==noOfCompanies):              
                        #print(row.get_text(),end="    ")      
                        #print (table.find_all('tr')[temp].get_text()) 
                        a=0
                        for finalData in row.find_all('td'):
                            a = a+1
                            temp1 = finalData.get_text()
                            if(a==2):
                                 insideList.append(Date)
                            insideList.append(temp1)
                        finalList.append(insideList)
                        insideList = []
#print(finalList)

                        
FinalList = []
finalTuple = ()            
print("total no of company ", totalCompany)
for i in range(totalCompany):
    data = finalList[i]
    tempp = int(float(data[6]))
    for j in outerList:
            if (j[0]==data[2]):
                finalTuple = ()                
                #typeOfcompany = j[3]
                currentDate = str(data[1])
                nameOfCompany = str(data[2])
                noOfShare = int(j[1])
                purchasedValuePerShare = int(j[2])
                totalPurchasedAmount = purchasedValuePerShare * noOfShare
                currentValuePerShare = tempp
                totalCurrentAmount = currentValuePerShare * noOfShare
                profitPerShare = int(currentValuePerShare) - purchasedValuePerShare
                totalProfit = profitPerShare*noOfShare
                profitPercent = (profitPerShare/purchasedValuePerShare)*100
                finalTuple = finalTuple + (nameOfCompany,currentDate,noOfShare,currentValuePerShare,totalCurrentAmount,purchasedValuePerShare,totalProfit,profitPercent,)
                break
            finalList.append(finalTuple)
    print(finalTuple)
    
#print(outerList)
"""

for d in outerListForExcel:
    

print(finalTuple)

"""

#code to create a csv
"""
fileName = "{}.csv".format(Date)
data = tableData
header = getCsvHeader()
def writer(header, data, filename):
    with open (filename, "w", newline = "") as csvfile:
        company =  csv.writer(csvfile)
        company.writerow(header)
        for dt in data:
            company.writerow(dt)
#writer(tableHeaderTuple, tableData, fileName)
"""


