from bs4 import BeautifulSoup
import requests
url='https://cn.tripadvisor.com/Attractions-g60763-Activities-New_York_City_New_York.html'
we_data=requests.get(url)
soup=BeautifulSoup(we_data.text,'lxml')
#print soup
titles=soup.select('#ATTR_ENTRY_105127 > div.property_title > a')
print(titles)