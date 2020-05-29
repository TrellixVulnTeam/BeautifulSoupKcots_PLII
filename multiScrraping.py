from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv

page = urlopen("http://www.nepalstock.com/main/todays_price")
pageSoup = BeautifulSoup(page, 'lxml')
pageDiv = pageSoup.find('div', class_= 'pager')
totalPages = int(pageDiv.get_text()[-1])

finalList = []
innerTuple = ()

#date extraction
Table = pageSoup.find('table')
date = Table.find('label', {'class':'pull-left'}).text
char = 6
finalDate=''
while char!=16:
    if (date[char]=='-'):
        finalDate = finalDate + "."
    else:
        finalDate = finalDate + date[char]
    char = char + 1


#table header
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


for page in range(1,totalPages+2):
    link = urlopen("http://www.nepalstock.com/main/todays_price/index/{}/".format(page))
    soup = BeautifulSoup(link, 'lxml')
    table = soup.find('table', class_ = "table table-condensed table-hover")
     
    
    for row in table.find_all('tr'):        
        for data in row.find_all('td'):
            check = data.get_text()
            if (check=='Chhimek Laghubitta Bikas Bank Limited' or check=='Bank of Kathmandu Ltd.' or check=='Upper Tamakoshi Hydropower Ltd'):
                #print(row.get_text(),end="    ")      
                #print (table.find_all('tr')[temp].get_text()) 
                a=0
                for finalData in row.find_all('td'):
                    a = a+1
                    temp1 = finalData.get_text()
                    if(a==2):
                      innerTuple = innerTuple + (finalDate,)
                    innerTuple = innerTuple + (temp1,)
                finalList.append(innerTuple)
                innerTuple = ()
tableData = finalList
#print(result[0])

#code to create a csv
fileName = "{}.csv".format(finalDate)
data = tableData
header = tableHeaderTuple
def writer(header, data, filename):
    with open (filename, "w", newline = "") as csvfile:
        company =  csv.writer(csvfile)
        company.writerow(header)
        for dt in data:
            company.writerow(dt)
    
    
writer(header, data, fileName)


#writer(tableHeaderTuple, tableData, fileName)

