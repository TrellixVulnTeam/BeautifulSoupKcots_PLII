from bs4 import BeautifulSoup
from urllib.request import urlopen

pages = [1,2,3,4]
Data = []
for page in pages:
    link = urlopen("http://www.nepalstock.com/main/todays_price/index/{}/".format(page))
    soup = BeautifulSoup(link, 'lxml')
    table = soup.find('table', class_ = "table table-condensed table-hover")
    temp = -1
    """for row in table.find_all('tr'):        
        temp = temp + 1
        for data in row.find_all('td'):
            check = data.get_text()
            if (check=='Chhimek Laghubitta Bikas Bank Limited' or check=='Bank of Kathmandu Ltd.' or check=='Upper Tamakoshi Hydropower Ltd'):
                #print(row.get_text(),end="    ")      
                print (table.find_all('tr')[temp].get_text())   """
    
date = table.find('label', {'class':'pull-left'}).text

char = 6
finalDate=''
while char!=16:
    if (date[char]=='-'):
        finalDate = finalDate + '/'
    else:
        finalDate = finalDate + date[char]
    char = char + 1
print(finalDate)
