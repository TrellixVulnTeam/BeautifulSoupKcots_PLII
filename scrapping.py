from bs4 import BeautifulSoup
from urllib.request import urlopen


url = urlopen("http://www.nepalstock.com/todaysprice")

soup = BeautifulSoup(url, 'lxml')

table = soup.find('table', class_ = "table table-condensed table-hover")
#tr = 
select = table.find('select', {"name":"_limit"})
limit = int(select.find('option', {"value":"20"}).text)

#for row in tr:
#     print(row.find_all('td')[0].text)

data = []
a=0
for i in range(2,limit+2,1):    
    data.append(table.find_all('tr')[i].get_text())

print (data[10][1])

    

    
    

    
    